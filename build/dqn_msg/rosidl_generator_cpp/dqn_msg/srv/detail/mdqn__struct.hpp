// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from dqn_msg:srv/Mdqn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__MDQN__STRUCT_HPP_
#define DQN_MSG__SRV__DETAIL__MDQN__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__dqn_msg__srv__Mdqn_Request __attribute__((deprecated))
#else
# define DEPRECATED__dqn_msg__srv__Mdqn_Request __declspec(deprecated)
#endif

namespace dqn_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Mdqn_Request_
{
  using Type = Mdqn_Request_<ContainerAllocator>;

  explicit Mdqn_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->init = false;
    }
  }

  explicit Mdqn_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->init = false;
    }
  }

  // field types and members
  using _actions_type =
    std::vector<int8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int8_t>>;
  _actions_type actions;
  using _init_type =
    bool;
  _init_type init;

  // setters for named parameter idiom
  Type & set__actions(
    const std::vector<int8_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<int8_t>> & _arg)
  {
    this->actions = _arg;
    return *this;
  }
  Type & set__init(
    const bool & _arg)
  {
    this->init = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    dqn_msg::srv::Mdqn_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const dqn_msg::srv::Mdqn_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Mdqn_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Mdqn_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dqn_msg__srv__Mdqn_Request
    std::shared_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dqn_msg__srv__Mdqn_Request
    std::shared_ptr<dqn_msg::srv::Mdqn_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mdqn_Request_ & other) const
  {
    if (this->actions != other.actions) {
      return false;
    }
    if (this->init != other.init) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mdqn_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mdqn_Request_

// alias to use template instance with default allocator
using Mdqn_Request =
  dqn_msg::srv::Mdqn_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace dqn_msg


#ifndef _WIN32
# define DEPRECATED__dqn_msg__srv__Mdqn_Response __attribute__((deprecated))
#else
# define DEPRECATED__dqn_msg__srv__Mdqn_Response __declspec(deprecated)
#endif

namespace dqn_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Mdqn_Response_
{
  using Type = Mdqn_Response_<ContainerAllocator>;

  explicit Mdqn_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit Mdqn_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _states_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _states_type states;
  using _rewards_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _rewards_type rewards;
  using _dones_type =
    std::vector<bool, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<bool>>;
  _dones_type dones;

  // setters for named parameter idiom
  Type & set__states(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->states = _arg;
    return *this;
  }
  Type & set__rewards(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->rewards = _arg;
    return *this;
  }
  Type & set__dones(
    const std::vector<bool, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<bool>> & _arg)
  {
    this->dones = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    dqn_msg::srv::Mdqn_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const dqn_msg::srv::Mdqn_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Mdqn_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Mdqn_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dqn_msg__srv__Mdqn_Response
    std::shared_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dqn_msg__srv__Mdqn_Response
    std::shared_ptr<dqn_msg::srv::Mdqn_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Mdqn_Response_ & other) const
  {
    if (this->states != other.states) {
      return false;
    }
    if (this->rewards != other.rewards) {
      return false;
    }
    if (this->dones != other.dones) {
      return false;
    }
    return true;
  }
  bool operator!=(const Mdqn_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Mdqn_Response_

// alias to use template instance with default allocator
using Mdqn_Response =
  dqn_msg::srv::Mdqn_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace dqn_msg

namespace dqn_msg
{

namespace srv
{

struct Mdqn
{
  using Request = dqn_msg::srv::Mdqn_Request;
  using Response = dqn_msg::srv::Mdqn_Response;
};

}  // namespace srv

}  // namespace dqn_msg

#endif  // DQN_MSG__SRV__DETAIL__MDQN__STRUCT_HPP_
