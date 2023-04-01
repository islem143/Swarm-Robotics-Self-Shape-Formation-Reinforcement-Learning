// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from dqn_msg:srv/Mdqn.idl
// generated code does not contain a copyright notice
#include "dqn_msg/srv/detail/mdqn__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "dqn_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "dqn_msg/srv/detail/mdqn__struct.h"
#include "dqn_msg/srv/detail/mdqn__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // actions
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // actions

// forward declare type support functions


using _Mdqn_Request__ros_msg_type = dqn_msg__srv__Mdqn_Request;

static bool _Mdqn_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Mdqn_Request__ros_msg_type * ros_message = static_cast<const _Mdqn_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: actions
  {
    size_t size = ros_message->actions.size;
    auto array_ptr = ros_message->actions.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: init
  {
    cdr << (ros_message->init ? true : false);
  }

  return true;
}

static bool _Mdqn_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Mdqn_Request__ros_msg_type * ros_message = static_cast<_Mdqn_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: actions
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->actions.data) {
      rosidl_runtime_c__int8__Sequence__fini(&ros_message->actions);
    }
    if (!rosidl_runtime_c__int8__Sequence__init(&ros_message->actions, size)) {
      fprintf(stderr, "failed to create array for field 'actions'");
      return false;
    }
    auto array_ptr = ros_message->actions.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: init
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->init = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dqn_msg
size_t get_serialized_size_dqn_msg__srv__Mdqn_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Mdqn_Request__ros_msg_type * ros_message = static_cast<const _Mdqn_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name actions
  {
    size_t array_size = ros_message->actions.size;
    auto array_ptr = ros_message->actions.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name init
  {
    size_t item_size = sizeof(ros_message->init);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Mdqn_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_dqn_msg__srv__Mdqn_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dqn_msg
size_t max_serialized_size_dqn_msg__srv__Mdqn_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: actions
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: init
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _Mdqn_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_dqn_msg__srv__Mdqn_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Mdqn_Request = {
  "dqn_msg::srv",
  "Mdqn_Request",
  _Mdqn_Request__cdr_serialize,
  _Mdqn_Request__cdr_deserialize,
  _Mdqn_Request__get_serialized_size,
  _Mdqn_Request__max_serialized_size
};

static rosidl_message_type_support_t _Mdqn_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Mdqn_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Request)() {
  return &_Mdqn_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "dqn_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "dqn_msg/srv/detail/mdqn__struct.h"
// already included above
// #include "dqn_msg/srv/detail/mdqn__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"  // dones, rewards, states
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"  // dones, rewards, states

// forward declare type support functions


using _Mdqn_Response__ros_msg_type = dqn_msg__srv__Mdqn_Response;

static bool _Mdqn_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Mdqn_Response__ros_msg_type * ros_message = static_cast<const _Mdqn_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: states
  {
    size_t size = ros_message->states.size;
    auto array_ptr = ros_message->states.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: rewards
  {
    size_t size = ros_message->rewards.size;
    auto array_ptr = ros_message->rewards.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: dones
  {
    size_t size = ros_message->dones.size;
    auto array_ptr = ros_message->dones.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _Mdqn_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Mdqn_Response__ros_msg_type * ros_message = static_cast<_Mdqn_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: states
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->states.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->states);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->states, size)) {
      fprintf(stderr, "failed to create array for field 'states'");
      return false;
    }
    auto array_ptr = ros_message->states.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: rewards
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->rewards.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->rewards);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->rewards, size)) {
      fprintf(stderr, "failed to create array for field 'rewards'");
      return false;
    }
    auto array_ptr = ros_message->rewards.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: dones
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->dones.data) {
      rosidl_runtime_c__boolean__Sequence__fini(&ros_message->dones);
    }
    if (!rosidl_runtime_c__boolean__Sequence__init(&ros_message->dones, size)) {
      fprintf(stderr, "failed to create array for field 'dones'");
      return false;
    }
    auto array_ptr = ros_message->dones.data;
    for (size_t i = 0; i < size; ++i) {
      uint8_t tmp;
      cdr >> tmp;
      array_ptr[i] = tmp ? true : false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dqn_msg
size_t get_serialized_size_dqn_msg__srv__Mdqn_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Mdqn_Response__ros_msg_type * ros_message = static_cast<const _Mdqn_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name states
  {
    size_t array_size = ros_message->states.size;
    auto array_ptr = ros_message->states.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name rewards
  {
    size_t array_size = ros_message->rewards.size;
    auto array_ptr = ros_message->rewards.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dones
  {
    size_t array_size = ros_message->dones.size;
    auto array_ptr = ros_message->dones.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Mdqn_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_dqn_msg__srv__Mdqn_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_dqn_msg
size_t max_serialized_size_dqn_msg__srv__Mdqn_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: states
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: rewards
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: dones
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _Mdqn_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_dqn_msg__srv__Mdqn_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Mdqn_Response = {
  "dqn_msg::srv",
  "Mdqn_Response",
  _Mdqn_Response__cdr_serialize,
  _Mdqn_Response__cdr_deserialize,
  _Mdqn_Response__get_serialized_size,
  _Mdqn_Response__max_serialized_size
};

static rosidl_message_type_support_t _Mdqn_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Mdqn_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Response)() {
  return &_Mdqn_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "dqn_msg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "dqn_msg/srv/mdqn.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t Mdqn__callbacks = {
  "dqn_msg::srv",
  "Mdqn",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Response)(),
};

static rosidl_service_type_support_t Mdqn__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &Mdqn__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn)() {
  return &Mdqn__handle;
}

#if defined(__cplusplus)
}
#endif
