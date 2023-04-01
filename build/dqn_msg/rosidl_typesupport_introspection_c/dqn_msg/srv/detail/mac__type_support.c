// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from dqn_msg:srv/Mac.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "dqn_msg/srv/detail/mac__rosidl_typesupport_introspection_c.h"
#include "dqn_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "dqn_msg/srv/detail/mac__functions.h"
#include "dqn_msg/srv/detail/mac__struct.h"


// Include directives for member types
// Member `actions`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  dqn_msg__srv__Mac_Request__init(message_memory);
}

void dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_fini_function(void * message_memory)
{
  dqn_msg__srv__Mac_Request__fini(message_memory);
}

size_t dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__size_function__Mac_Request__actions(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_const_function__Mac_Request__actions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_function__Mac_Request__actions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__fetch_function__Mac_Request__actions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_const_function__Mac_Request__actions(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__assign_function__Mac_Request__actions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_function__Mac_Request__actions(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__resize_function__Mac_Request__actions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_member_array[2] = {
  {
    "actions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__srv__Mac_Request, actions),  // bytes offset in struct
    NULL,  // default value
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__size_function__Mac_Request__actions,  // size() function pointer
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_const_function__Mac_Request__actions,  // get_const(index) function pointer
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__get_function__Mac_Request__actions,  // get(index) function pointer
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__fetch_function__Mac_Request__actions,  // fetch(index, &value) function pointer
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__assign_function__Mac_Request__actions,  // assign(index, value) function pointer
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__resize_function__Mac_Request__actions  // resize(index) function pointer
  },
  {
    "init",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__srv__Mac_Request, init),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_members = {
  "dqn_msg__srv",  // message namespace
  "Mac_Request",  // message name
  2,  // number of fields
  sizeof(dqn_msg__srv__Mac_Request),
  dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_member_array,  // message members
  dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_type_support_handle = {
  0,
  &dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_dqn_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Request)() {
  if (!dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_type_support_handle.typesupport_identifier) {
    dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &dqn_msg__srv__Mac_Request__rosidl_typesupport_introspection_c__Mac_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "dqn_msg/srv/detail/mac__rosidl_typesupport_introspection_c.h"
// already included above
// #include "dqn_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "dqn_msg/srv/detail/mac__functions.h"
// already included above
// #include "dqn_msg/srv/detail/mac__struct.h"


// Include directives for member types
// Member `states`
// Member `rewards`
// Member `dones`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  dqn_msg__srv__Mac_Response__init(message_memory);
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_fini_function(void * message_memory)
{
  dqn_msg__srv__Mac_Response__fini(message_memory);
}

size_t dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__states(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__states(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__states(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__states(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__states(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__states(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__states(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__states(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__rewards(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__rewards(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__rewards(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__rewards(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__rewards(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__rewards(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__rewards(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__rewards(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__dones(
  const void * untyped_member)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return member->size;
}

const void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__dones(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__boolean__Sequence * member =
    (const rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void * dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__dones(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  return &member->data[index];
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__dones(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const bool * item =
    ((const bool *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__dones(untyped_member, index));
  bool * value =
    (bool *)(untyped_value);
  *value = *item;
}

void dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__dones(
  void * untyped_member, size_t index, const void * untyped_value)
{
  bool * item =
    ((bool *)
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__dones(untyped_member, index));
  const bool * value =
    (const bool *)(untyped_value);
  *item = *value;
}

bool dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__dones(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__boolean__Sequence * member =
    (rosidl_runtime_c__boolean__Sequence *)(untyped_member);
  rosidl_runtime_c__boolean__Sequence__fini(member);
  return rosidl_runtime_c__boolean__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_member_array[3] = {
  {
    "states",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__srv__Mac_Response, states),  // bytes offset in struct
    NULL,  // default value
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__states,  // size() function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__states,  // get_const(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__states,  // get(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__states,  // fetch(index, &value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__states,  // assign(index, value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__states  // resize(index) function pointer
  },
  {
    "rewards",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__srv__Mac_Response, rewards),  // bytes offset in struct
    NULL,  // default value
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__rewards,  // size() function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__rewards,  // get_const(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__rewards,  // get(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__rewards,  // fetch(index, &value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__rewards,  // assign(index, value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__rewards  // resize(index) function pointer
  },
  {
    "dones",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(dqn_msg__srv__Mac_Response, dones),  // bytes offset in struct
    NULL,  // default value
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__size_function__Mac_Response__dones,  // size() function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_const_function__Mac_Response__dones,  // get_const(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__get_function__Mac_Response__dones,  // get(index) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__fetch_function__Mac_Response__dones,  // fetch(index, &value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__assign_function__Mac_Response__dones,  // assign(index, value) function pointer
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__resize_function__Mac_Response__dones  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_members = {
  "dqn_msg__srv",  // message namespace
  "Mac_Response",  // message name
  3,  // number of fields
  sizeof(dqn_msg__srv__Mac_Response),
  dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_member_array,  // message members
  dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_type_support_handle = {
  0,
  &dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_dqn_msg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Response)() {
  if (!dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_type_support_handle.typesupport_identifier) {
    dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &dqn_msg__srv__Mac_Response__rosidl_typesupport_introspection_c__Mac_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "dqn_msg/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "dqn_msg/srv/detail/mac__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_members = {
  "dqn_msg__srv",  // service namespace
  "Mac",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_Request_message_type_support_handle,
  NULL  // response message
  // dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_Response_message_type_support_handle
};

static rosidl_service_type_support_t dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_type_support_handle = {
  0,
  &dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_dqn_msg
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac)() {
  if (!dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_type_support_handle.typesupport_identifier) {
    dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mac_Response)()->data;
  }

  return &dqn_msg__srv__detail__mac__rosidl_typesupport_introspection_c__Mac_service_type_support_handle;
}
