// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__MSG__DETAIL__GOAL__TRAITS_HPP_
#define DQN_MSG__MSG__DETAIL__GOAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dqn_msg/msg/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dqn_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal
  {
    if (msg.goal.size() == 0) {
      out << "goal: []";
    } else {
      out << "goal: [";
      size_t pending_items = msg.goal.size();
      for (auto item : msg.goal) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.goal.size() == 0) {
      out << "goal: []\n";
    } else {
      out << "goal:\n";
      for (auto item : msg.goal) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace dqn_msg

namespace rosidl_generator_traits
{

[[deprecated("use dqn_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dqn_msg::msg::Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::msg::Goal & msg)
{
  return dqn_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::msg::Goal>()
{
  return "dqn_msg::msg::Goal";
}

template<>
inline const char * name<dqn_msg::msg::Goal>()
{
  return "dqn_msg/msg/Goal";
}

template<>
struct has_fixed_size<dqn_msg::msg::Goal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dqn_msg::msg::Goal>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dqn_msg::msg::Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DQN_MSG__MSG__DETAIL__GOAL__TRAITS_HPP_
