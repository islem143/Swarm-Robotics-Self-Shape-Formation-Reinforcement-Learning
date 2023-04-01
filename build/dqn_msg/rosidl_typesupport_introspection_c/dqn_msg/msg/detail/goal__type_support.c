// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "dqn_msg/msg/detail/goal__rosidl_typesupport_introspection_c.h"
#include "dqn_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "dqn_msg/msg/detail/goal__functions.h"
#include "dqn_msg/msg/detail/goal__struct.h"


// Include directives for member types
// Member `goal`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  dqn_msg__msg__Goal__init(message_memory);
}

void dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_fini_function(void * message_memory)
{
  dqn_msg__msg__Goal__fini(message_memory);
}

size_t dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__size_function__Goal__goal(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_const_function__Goal__goal(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_function__Goal__goal(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__fetch_function__Goal__goal(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_const_function__Goal__goal(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__assign_function__Goal__goal(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_function__Goal__goal(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__resize_function__Goal__goal(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_member_array[1] = {
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__msg__Goal, goal),  // bytes offset in struct
    NULL,  // default value
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__size_function__Goal__goal,  // size() function pointer
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_const_function__Goal__goal,  // get_const(index) function pointer
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__get_function__Goal__goal,  // get(index) function pointer
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__fetch_function__Goal__goal,  // fetch(index, &value) function pointer
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__assign_function__Goal__goal,  // assign(index, value) function pointer
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__resize_function__Goal__goal  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_members = {
  "dqn_msg__msg",  // message namespace
  "Goal",  // message name
  1,  // number of fields
  sizeof(dqn_msg__msg__Goal),
  dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_member_array,  // message members
  dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_init_function,  // function to initialize message memory (memory has to be allocated)
  dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_type_support_handle = {
  0,
  &dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_dqn_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, msg, Goal)() {
  if (!dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_type_support_handle.typesupport_identifier) {
    dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &dqn_msg__msg__Goal__rosidl_typesupport_introspection_c__Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
