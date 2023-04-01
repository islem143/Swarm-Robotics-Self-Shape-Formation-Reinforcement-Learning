// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dqn_msg:srv/Mdqn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__MDQN__BUILDER_HPP_
#define DQN_MSG__SRV__DETAIL__MDQN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dqn_msg/srv/detail/mdqn__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dqn_msg
{

namespace srv
{

namespace builder
{

class Init_Mdqn_Request_init
{
public:
  explicit Init_Mdqn_Request_init(::dqn_msg::srv::Mdqn_Request & msg)
  : msg_(msg)
  {}
  ::dqn_msg::srv::Mdqn_Request init(::dqn_msg::srv::Mdqn_Request::_init_type arg)
  {
    msg_.init = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::srv::Mdqn_Request msg_;
};

class Init_Mdqn_Request_actions
{
public:
  Init_Mdqn_Request_actions()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Mdqn_Request_init actions(::dqn_msg::srv::Mdqn_Request::_actions_type arg)
  {
    msg_.actions = std::move(arg);
    return Init_Mdqn_Request_init(msg_);
  }

private:
  ::dqn_msg::srv::Mdqn_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Mdqn_Request>()
{
  return dqn_msg::srv::builder::Init_Mdqn_Request_actions();
}

}  // namespace dqn_msg


namespace dqn_msg
{

namespace srv
{

namespace builder
{

class Init_Mdqn_Response_dones
{
public:
  explicit Init_Mdqn_Response_dones(::dqn_msg::srv::Mdqn_Response & msg)
  : msg_(msg)
  {}
  ::dqn_msg::srv::Mdqn_Response dones(::dqn_msg::srv::Mdqn_Response::_dones_type arg)
  {
    msg_.dones = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::srv::Mdqn_Response msg_;
};

class Init_Mdqn_Response_rewards
{
public:
  explicit Init_Mdqn_Response_rewards(::dqn_msg::srv::Mdqn_Response & msg)
  : msg_(msg)
  {}
  Init_Mdqn_Response_dones rewards(::dqn_msg::srv::Mdqn_Response::_rewards_type arg)
  {
    msg_.rewards = std::move(arg);
    return Init_Mdqn_Response_dones(msg_);
  }

private:
  ::dqn_msg::srv::Mdqn_Response msg_;
};

class Init_Mdqn_Response_states
{
public:
  Init_Mdqn_Response_states()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Mdqn_Response_rewards states(::dqn_msg::srv::Mdqn_Response::_states_type arg)
  {
    msg_.states = std::move(arg);
    return Init_Mdqn_Response_rewards(msg_);
  }

private:
  ::dqn_msg::srv::Mdqn_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Mdqn_Response>()
{
  return dqn_msg::srv::builder::Init_Mdqn_Response_states();
}

}  // namespace dqn_msg

#endif  // DQN_MSG__SRV__DETAIL__MDQN__BUILDER_HPP_
