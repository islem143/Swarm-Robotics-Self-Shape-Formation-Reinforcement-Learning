// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__MSG__DETAIL__GOAL__BUILDER_HPP_
#define DQN_MSG__MSG__DETAIL__GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dqn_msg/msg/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dqn_msg
{

namespace msg
{

namespace builder
{

class Init_Goal_goal
{
public:
  Init_Goal_goal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::dqn_msg::msg::Goal goal(::dqn_msg::msg::Goal::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::msg::Goal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::msg::Goal>()
{
  return dqn_msg::msg::builder::Init_Goal_goal();
}

}  // namespace dqn_msg

#endif  // DQN_MSG__MSG__DETAIL__GOAL__BUILDER_HPP_
