import logging

import pymel.core as pymel
from omtk import constants, api
from omtk.core import rig
from omtk.core import preferences
from omtk.libs import libPython
from omtk.vendor import libSerialization
from omtk.vendor.Qt import QtCore
from omtk.vendor.libSerialization import cache as libSerializationCache

log = logging.getLogger('omtk')


class AutoRigManager(QtCore.QObject):
    """
    Manager class than handle possible user actions in omtk.
    """
    # todo: move AutoRig class logic to the manager and implement unit tests

    # Used when a new Rig instance is added to the scene.
    onRigCreated = QtCore.Signal(object)

    # Trigger a complete redraw
    onSceneChanged = QtCore.Signal()

    def __init__(self):
        super(AutoRigManager, self).__init__()
        self._root = None
        self._roots = []

        self._components = []

        self.preferences = preferences.get_preferences()

        # Initialize libSerialization cache.
        # This will allow to re-use data.
        # Note that we will reset the cache at each import.
        self._serialization_cache = None
        self.clear_cache()

        # Note: This should be done in a lazy way and linked to the current scene.
        self.import_components()

        self.import_networks()

    def _add_rig(self, rig):
        self._roots.append(rig)
        if self._root is None:
            self._root = next(iter(self._roots), None)
        libSerialization.export_network(rig, cache=self._serialization_cache)

    def clear_cache(self):
        self._serialization_cache = libSerializationCache.Cache()

    def import_components(self):
        """
        Fill the component registry with any serialized components in the scene.
        """
        from omtk.core import component
        cls_name = component.Component.__name__
        networks = libSerialization.get_networks_from_class(cls_name)
        results = [libSerialization.import_network(network, module='omtk', cache=self._serialization_cache) for network
                   in networks]
        results = filter(None, results)
        self._components = results
        return results

    def import_network(self, network, **kwargs):
        return libSerialization.import_network(network, cache=self._serialization_cache, **kwargs)

    def export_network(self, data, **kwargs):
        return libSerialization.export_network(data, cache=self._serialization_cache, **kwargs)

    def import_networks(self):
        """
        Re-import everything from the scene.
        Warning, this is a SLOW operation.
        :return:
        """
        from omtk.vendor.libSerialization import cache
        self._serialization_cache = cache.Cache()
        self._roots = api.find(cache=self._serialization_cache)
        self._root = next(iter(self._roots), None)

    def export_networks(self):
        """
        Re-export everything in the scene.
        Warning, this is a SLOW operation.
        :return:
        """
        for root in self._roots:
            try:
                network = root._network
                if network and network.exists():
                    pymel.delete(network)
            except AttributeError:
                pass

        self.clear_cache()
        for root in self._roots:
            self.export_network(root)

    def get_rigs(self):
        return self._roots

    def create_rig(self, rig_type=None):
        if rig_type is None:
            # todo: get default rig definition
            raise NotImplementedError
        # rig_type = self.get_selected_rig_definition()

        # Initialize the scene
        rig_ = api.create(cls=rig_type)
        rig_.build()
        self._add_rig(rig_)
        libSerialization.export_network(rig_)

        self.onRigCreated.emit(rig_)

        return rig_

    def execute_actions(self, actions):
        need_export_network = False
        # entities = self.get_selected_components()
        # action_map = self._get_actions(entities)
        for action in actions:
            action.execute()
            if constants.ComponentActionFlags.trigger_network_export in action.iter_flags():
                need_export_network = True

        if need_export_network:
            self.export_networks()

            self.onSceneChanged.emit()
            # todo: update node editor?


@libPython.memoized
def get_session():
    # type: () -> AutoRigManager
    return AutoRigManager()