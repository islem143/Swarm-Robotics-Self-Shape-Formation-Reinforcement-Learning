// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mrs_msg:srv/AddThreeInts.idl
// generated code does not contain a copyright notice

#ifndef MRS_MSG__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_
#define MRS_MSG__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mrs_msg/srv/detail/add_three_ints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mrs_msg
{

namespace srv
{

namespace builder
{

class Init_AddThreeInts_Request_c
{
public:
  explicit Init_AddThreeInts_Request_c(::mrs_msg::srv::AddThreeInts_Request & msg)
  : msg_(msg)
  {}
  ::mrs_msg::srv::AddThreeInts_Request c(::mrs_msg::srv::AddThreeInts_Request::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mrs_msg::srv::AddThreeInts_Request msg_;
};

class Init_AddThreeInts_Request_b
{
public:
  explicit Init_AddThreeInts_Request_b(::mrs_msg::srv::AddThreeInts_Request & msg)
  : msg_(msg)
  {}
  Init_AddThreeInts_Request_c b(::mrs_msg::srv::AddThreeInts_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_AddThreeInts_Request_c(msg_);
  }

private:
  ::mrs_msg::srv::AddThreeInts_Request msg_;
};

class Init_AddThreeInts_Request_a
{
public:
  Init_AddThreeInts_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddThreeInts_Request_b a(::mrs_msg::srv::AddThreeInts_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_AddThreeInts_Request_b(msg_);
  }

private:
  ::mrs_msg::srv::AddThreeInts_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mrs_msg::srv::AddThreeInts_Request>()
{
  return mrs_msg::srv::builder::Init_AddThreeInts_Request_a();
}

}  // namespace mrs_msg


namespace mrs_msg
{

namespace srv
{

namespace builder
{

class Init_AddThreeInts_Response_sum
{
public:
  Init_AddThreeInts_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mrs_msg::srv::AddThreeInts_Response sum(::mrs_msg::srv::AddThreeInts_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mrs_msg::srv::AddThreeInts_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mrs_msg::srv::AddThreeInts_Response>()
{
  return mrs_msg::srv::builder::Init_AddThreeInts_Response_sum();
}

}  // namespace mrs_msg

#endif  // MRS_MSG__SRV__DETAIL__ADD_THREE_INTS__BUILDER_HPP_
