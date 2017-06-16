"""
A ComponentAttribute is the link between internal data and the gui.
It deal with typing and validation (used for drag and drop events for now)
"""


class ComponentAttribute(object):
    def __init__(self, name, is_input=True, is_output=True, val=None):
        self.name = name
        self._val = val
        self.is_input = is_input
        self.is_output = is_output

    def get(self):
        return self._val

    def set(self, val):
        # todo: late validation?
        self._val = val
        return True

    def validate(self, val):
        """
        Check if a provided value can be set on this ComponentAttribute.
        :param val: An object instance or a basic value.
        :return: True if the value can be set. False otherwise.
        """
        return True


class ComponentAttributeTyped(ComponentAttribute):
    def __init__(self, valid_types, *args, **kwargs):
        self._valid_types = valid_types
        super(ComponentAttributeTyped, self).__init__(*args, **kwargs)

    def validate(self, val):
        print val, self._valid_types
        return isinstance(val, self._valid_types)


class ComponentAttributeTypedCollection(ComponentAttributeTyped):
    def validate(self, val):
        # Validate iterable values
        if isinstance(val, (list, tuple, set)):
            return all(super(ComponentAttributeTypedCollection, self).validate(entry) for entry in val)
        # Otherwise validate single values
        else:
            return super(ComponentAttributeTypedCollection, self).validate(val)
