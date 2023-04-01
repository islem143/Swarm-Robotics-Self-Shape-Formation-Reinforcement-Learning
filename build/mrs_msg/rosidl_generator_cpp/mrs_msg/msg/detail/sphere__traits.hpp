// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mrs_msg:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef MRS_MSG__MSG__DETAIL__SPHERE__TRAITS_HPP_
#define MRS_MSG__MSG__DETAIL__SPHERE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mrs_msg/msg/detail/sphere__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'center'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace mrs_msg
{

namespace msg
{

inline void to_flow_style_yaml(
  const Sphere & msg,
  std::ostream & out)
{
  out << "{";
  // member: center
  {
    out << "center: ";
    to_flow_style_yaml(msg.center, out);
    out << ", ";
  }

  // member: radius
  {
    out << "radius: ";
    rosidl_generator_traits::value_to_yaml(msg.radius, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Sphere & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: center
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "center:\n";
    to_block_style_yaml(msg.center, out, indentation + 2);
  }

  // member: radius
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "radius: ";
    rosidl_generator_traits::value_to_yaml(msg.radius, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Sphere & msg, bool use_flow_style = false)
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

}  // namespace mrs_msg

namespace rosidl_generator_traits
{

[[deprecated("use mrs_msg::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mrs_msg::msg::Sphere & msg,
  std::ostream & out, size_t indentation = 0)
{
  mrs_msg::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mrs_msg::msg::to_yaml() instead")]]
inline std::string to_yaml(const mrs_msg::msg::Sphere & msg)
{
  return mrs_msg::msg::to_yaml(msg);
}

template<>
inline const char * data_type<mrs_msg::msg::Sphere>()
{
  return "mrs_msg::msg::Sphere";
}

template<>
inline const char * name<mrs_msg::msg::Sphere>()
{
  return "mrs_msg/msg/Sphere";
}

template<>
struct has_fixed_size<mrs_msg::msg::Sphere>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<mrs_msg::msg::Sphere>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<mrs_msg::msg::Sphere>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MRS_MSG__MSG__DETAIL__SPHERE__TRAITS_HPP_
