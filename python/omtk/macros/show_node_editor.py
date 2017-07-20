from omtk.core.macros import BaseMacro
from omtk.vendor.Qt import QtWidgets
from omtk.qt_widgets import nodegraph_widget

_gui = None  # workaround garbage collection bug


class ShowNodeEditor(BaseMacro):
    def run(self):
        cls = nodegraph_widget.nodegraph_widget.NodeGraphWidget
        global _gui
        _gui = QtWidgets.QMainWindow()
        _gui.setCentralWidget(cls(_gui))
        _gui.show()


def register_plugin():
    return ShowNodeEditor