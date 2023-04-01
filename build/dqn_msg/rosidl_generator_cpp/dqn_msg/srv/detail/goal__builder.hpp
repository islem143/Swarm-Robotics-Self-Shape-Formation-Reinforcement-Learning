// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dqn_msg:srv/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__GOAL__BUILDER_HPP_
#define DQN_MSG__SRV__DETAIL__GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dqn_msg/srv/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dqn_msg
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Goal_Request>()
{
  return ::dqn_msg::srv::Goal_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace dqn_msg


namespace dqn_msg
{

namespace srv
{

namespace builder
{

class Init_Goal_Response_y
{
public:
  explicit Init_Goal_Response_y(::dqn_msg::srv::Goal_Response & msg)
  : msg_(msg)
  {}
  ::dqn_msg::srv::Goal_Response y(::dqn_msg::srv::Goal_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::srv::Goal_Response msg_;
};

class Init_Goal_Response_x
{
public:
  Init_Goal_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Goal_Response_y x(::dqn_msg::srv::Goal_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Goal_Response_y(msg_);
  }

private:
  ::dqn_msg::srv::Goal_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Goal_Response>()
{
  return dqn_msg::srv::builder::Init_Goal_Response_x();
}

}  // namespace dqn_msg

#endif  // DQN_MSG__SRV__DETAIL__GOAL__BUILDER_HPP_
