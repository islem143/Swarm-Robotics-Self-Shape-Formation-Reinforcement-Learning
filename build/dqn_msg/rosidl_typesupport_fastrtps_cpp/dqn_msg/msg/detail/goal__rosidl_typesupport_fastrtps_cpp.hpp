// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__MSG__DETAIL__GOAL__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define DQN_MSG__MSG__DETAIL__GOAL__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "dqn_msg/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "dqn_msg/msg/detail/goal__struct.hpp"

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

#include "fastcdr/Cdr.h"

namespace dqn_msg
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_dqn_msg
cdr_serialize(
  const dqn_msg::msg::Goal & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_dqn_msg
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  dqn_msg::msg::Goal & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_dqn_msg
get_serialized_size(
  const dqn_msg::msg::Goal & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_dqn_msg
max_serialized_size_Goal(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace dqn_msg

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_dqn_msg
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, dqn_msg, msg, Goal)();

#ifdef __cplusplus
}
#endif

#endif  // DQN_MSG__MSG__DETAIL__GOAL__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
