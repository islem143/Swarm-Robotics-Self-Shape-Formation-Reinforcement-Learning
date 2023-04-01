// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dqn_msg:srv/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__GOAL__TRAITS_HPP_
#define DQN_MSG__SRV__DETAIL__GOAL__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dqn_msg/srv/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Goal_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Goal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Goal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_generator_traits
{

[[deprecated("use dqn_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dqn_msg::srv::Goal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Goal_Request & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Goal_Request>()
{
  return "dqn_msg::srv::Goal_Request";
}

template<>
inline const char * name<dqn_msg::srv::Goal_Request>()
{
  return "dqn_msg/srv/Goal_Request";
}

template<>
struct has_fixed_size<dqn_msg::srv::Goal_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<dqn_msg::srv::Goal_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<dqn_msg::srv::Goal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Goal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Goal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Goal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_generator_traits
{

[[deprecated("use dqn_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dqn_msg::srv::Goal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Goal_Response & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Goal_Response>()
{
  return "dqn_msg::srv::Goal_Response";
}

template<>
inline const char * name<dqn_msg::srv::Goal_Response>()
{
  return "dqn_msg/srv/Goal_Response";
}

template<>
struct has_fixed_size<dqn_msg::srv::Goal_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<dqn_msg::srv::Goal_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<dqn_msg::srv::Goal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<dqn_msg::srv::Goal>()
{
  return "dqn_msg::srv::Goal";
}

template<>
inline const char * name<dqn_msg::srv::Goal>()
{
  return "dqn_msg/srv/Goal";
}

template<>
struct has_fixed_size<dqn_msg::srv::Goal>
  : std::integral_constant<
    bool,
    has_fixed_size<dqn_msg::srv::Goal_Request>::value &&
    has_fixed_size<dqn_msg::srv::Goal_Response>::value
  >
{
};

template<>
struct has_bounded_size<dqn_msg::srv::Goal>
  : std::integral_constant<
    bool,
    has_bounded_size<dqn_msg::srv::Goal_Request>::value &&
    has_bounded_size<dqn_msg::srv::Goal_Response>::value
  >
{
};

template<>
struct is_service<dqn_msg::srv::Goal>
  : std::true_type
{
};

template<>
struct is_service_request<dqn_msg::srv::Goal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<dqn_msg::srv::Goal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DQN_MSG__SRV__DETAIL__GOAL__TRAITS_HPP_
