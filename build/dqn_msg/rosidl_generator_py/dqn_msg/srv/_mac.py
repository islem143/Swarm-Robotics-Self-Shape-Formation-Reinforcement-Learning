# generated from rosidl_generator_py/resource/_idl.py.em
# with input from dqn_msg:srv/Mac.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'actions'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Mac_Request(type):
    """Metaclass of message 'Mac_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('dqn_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'dqn_msg.srv.Mac_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mac__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mac__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mac__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mac__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mac__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mac_Request(metaclass=Metaclass_Mac_Request):
    """Message class 'Mac_Request'."""

    __slots__ = [
        '_actions',
        '_init',
    ]

    _fields_and_field_types = {
        'actions': 'sequence<float>',
        'init': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.actions = array.array('f', kwargs.get('actions', []))
        self.init = kwargs.get('init', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.actions != other.actions:
            return False
        if self.init != other.init:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def actions(self):
        """Message field 'actions'."""
        return self._actions

    @actions.setter
    def actions(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'actions' array.array() must have the type code of 'f'"
            self._actions = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'actions' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._actions = array.array('f', value)

    @builtins.property
    def init(self):
        """Message field 'init'."""
        return self._init

    @init.setter
    def init(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'init' field must be of type 'bool'"
        self._init = value


# Import statements for member types

# Member 'states'
# Member 'rewards'
# already imported above
# import array

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_Mac_Response(type):
    """Metaclass of message 'Mac_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('dqn_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'dqn_msg.srv.Mac_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__mac__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__mac__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__mac__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__mac__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__mac__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Mac_Response(metaclass=Metaclass_Mac_Response):
    """Message class 'Mac_Response'."""

    __slots__ = [
        '_states',
        '_rewards',
        '_dones',
    ]

    _fields_and_field_types = {
        'states': 'sequence<float>',
        'rewards': 'sequence<float>',
        'dones': 'sequence<boolean>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('float')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('boolean')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.states = array.array('f', kwargs.get('states', []))
        self.rewards = array.array('f', kwargs.get('rewards', []))
        self.dones = kwargs.get('dones', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.states != other.states:
            return False
        if self.rewards != other.rewards:
            return False
        if self.dones != other.dones:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def states(self):
        """Message field 'states'."""
        return self._states

    @states.setter
    def states(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'states' array.array() must have the type code of 'f'"
            self._states = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'states' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._states = array.array('f', value)

    @builtins.property
    def rewards(self):
        """Message field 'rewards'."""
        return self._rewards

    @rewards.setter
    def rewards(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'f', \
                "The 'rewards' array.array() must have the type code of 'f'"
            self._rewards = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -3.402823466e+38 or val > 3.402823466e+38) or math.isinf(val) for val in value)), \
                "The 'rewards' field must be a set or sequence and each value of type 'float' and each float in [-340282346600000016151267322115014000640.000000, 340282346600000016151267322115014000640.000000]"
        self._rewards = array.array('f', value)

    @builtins.property
    def dones(self):
        """Message field 'dones'."""
        return self._dones

    @dones.setter
    def dones(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, bool) for v in value) and
                 True), \
                "The 'dones' field must be a set or sequence and each value of type 'bool'"
        self._dones = value


class Metaclass_Mac(type):
    """Metaclass of service 'Mac'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('dqn_msg')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'dqn_msg.srv.Mac')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__mac

            from dqn_msg.srv import _mac
            if _mac.Metaclass_Mac_Request._TYPE_SUPPORT is None:
                _mac.Metaclass_Mac_Request.__import_type_support__()
            if _mac.Metaclass_Mac_Response._TYPE_SUPPORT is None:
                _mac.Metaclass_Mac_Response.__import_type_support__()


class Mac(metaclass=Metaclass_Mac):
    from dqn_msg.srv._mac import Mac_Request as Request
    from dqn_msg.srv._mac import Mac_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
