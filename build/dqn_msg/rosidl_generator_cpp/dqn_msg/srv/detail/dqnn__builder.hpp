// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from dqn_msg:srv/Dqnn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__DQNN__BUILDER_HPP_
#define DQN_MSG__SRV__DETAIL__DQNN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "dqn_msg/srv/detail/dqnn__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace dqn_msg
{

namespace srv
{

namespace builder
{

class Init_Dqnn_Request_init
{
public:
  explicit Init_Dqnn_Request_init(::dqn_msg::srv::Dqnn_Request & msg)
  : msg_(msg)
  {}
  ::dqn_msg::srv::Dqnn_Request init(::dqn_msg::srv::Dqnn_Request::_init_type arg)
  {
    msg_.init = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Request msg_;
};

class Init_Dqnn_Request_id
{
public:
  explicit Init_Dqnn_Request_id(::dqn_msg::srv::Dqnn_Request & msg)
  : msg_(msg)
  {}
  Init_Dqnn_Request_init id(::dqn_msg::srv::Dqnn_Request::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Dqnn_Request_init(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Request msg_;
};

class Init_Dqnn_Request_action
{
public:
  Init_Dqnn_Request_action()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Dqnn_Request_id action(::dqn_msg::srv::Dqnn_Request::_action_type arg)
  {
    msg_.action = std::move(arg);
    return Init_Dqnn_Request_id(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Dqnn_Request>()
{
  return dqn_msg::srv::builder::Init_Dqnn_Request_action();
}

}  // namespace dqn_msg


namespace dqn_msg
{

namespace srv
{

namespace builder
{

class Init_Dqnn_Response_done
{
public:
  explicit Init_Dqnn_Response_done(::dqn_msg::srv::Dqnn_Response & msg)
  : msg_(msg)
  {}
  ::dqn_msg::srv::Dqnn_Response done(::dqn_msg::srv::Dqnn_Response::_done_type arg)
  {
    msg_.done = std::move(arg);
    return std::move(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Response msg_;
};

class Init_Dqnn_Response_reward
{
public:
  explicit Init_Dqnn_Response_reward(::dqn_msg::srv::Dqnn_Response & msg)
  : msg_(msg)
  {}
  Init_Dqnn_Response_done reward(::dqn_msg::srv::Dqnn_Response::_reward_type arg)
  {
    msg_.reward = std::move(arg);
    return Init_Dqnn_Response_done(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Response msg_;
};

class Init_Dqnn_Response_state
{
public:
  Init_Dqnn_Response_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Dqnn_Response_reward state(::dqn_msg::srv::Dqnn_Response::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_Dqnn_Response_reward(msg_);
  }

private:
  ::dqn_msg::srv::Dqnn_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::dqn_msg::srv::Dqnn_Response>()
{
  return dqn_msg::srv::builder::Init_Dqnn_Response_state();
}

}  // namespace dqn_msg

#endif  // DQN_MSG__SRV__DETAIL__DQNN__BUILDER_HPP_
