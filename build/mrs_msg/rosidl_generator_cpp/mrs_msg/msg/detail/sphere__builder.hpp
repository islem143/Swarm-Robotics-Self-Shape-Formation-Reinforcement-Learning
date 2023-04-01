// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mrs_msg:msg/Sphere.idl
// generated code does not contain a copyright notice

#ifndef MRS_MSG__MSG__DETAIL__SPHERE__BUILDER_HPP_
#define MRS_MSG__MSG__DETAIL__SPHERE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mrs_msg/msg/detail/sphere__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mrs_msg
{

namespace msg
{

namespace builder
{

class Init_Sphere_radius
{
public:
  explicit Init_Sphere_radius(::mrs_msg::msg::Sphere & msg)
  : msg_(msg)
  {}
  ::mrs_msg::msg::Sphere radius(::mrs_msg::msg::Sphere::_radius_type arg)
  {
    msg_.radius = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mrs_msg::msg::Sphere msg_;
};

class Init_Sphere_center
{
public:
  Init_Sphere_center()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Sphere_radius center(::mrs_msg::msg::Sphere::_center_type arg)
  {
    msg_.center = std::move(arg);
    return Init_Sphere_radius(msg_);
  }

private:
  ::mrs_msg::msg::Sphere msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mrs_msg::msg::Sphere>()
{
  return mrs_msg::msg::builder::Init_Sphere_center();
}

}  // namespace mrs_msg

#endif  // MRS_MSG__MSG__DETAIL__SPHERE__BUILDER_HPP_
