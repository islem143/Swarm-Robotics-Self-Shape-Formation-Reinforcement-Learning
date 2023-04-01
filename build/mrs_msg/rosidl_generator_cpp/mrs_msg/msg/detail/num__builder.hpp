// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mrs_msg:msg/Num.idl
// generated code does not contain a copyright notice

#ifndef MRS_MSG__MSG__DETAIL__NUM__BUILDER_HPP_
#define MRS_MSG__MSG__DETAIL__NUM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mrs_msg/msg/detail/num__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mrs_msg
{

namespace msg
{

namespace builder
{

class Init_Num_num
{
public:
  Init_Num_num()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mrs_msg::msg::Num num(::mrs_msg::msg::Num::_num_type arg)
  {
    msg_.num = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mrs_msg::msg::Num msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mrs_msg::msg::Num>()
{
  return mrs_msg::msg::builder::Init_Num_num();
}

}  // namespace mrs_msg

#endif  // MRS_MSG__MSG__DETAIL__NUM__BUILDER_HPP_
