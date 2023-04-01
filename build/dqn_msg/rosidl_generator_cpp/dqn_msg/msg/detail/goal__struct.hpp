// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__MSG__DETAIL__GOAL__STRUCT_HPP_
#define DQN_MSG__MSG__DETAIL__GOAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__dqn_msg__msg__Goal __attribute__((deprecated))
#else
# define DEPRECATED__dqn_msg__msg__Goal __declspec(deprecated)
#endif

namespace dqn_msg
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Goal_
{
  using Type = Goal_<ContainerAllocator>;

  explicit Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _goal_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    dqn_msg::msg::Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const dqn_msg::msg::Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dqn_msg::msg::Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dqn_msg::msg::Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dqn_msg::msg::Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::msg::Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dqn_msg::msg::Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::msg::Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dqn_msg::msg::Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dqn_msg::msg::Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dqn_msg__msg__Goal
    std::shared_ptr<dqn_msg::msg::Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dqn_msg__msg__Goal
    std::shared_ptr<dqn_msg::msg::Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Goal_ & other) const
  {
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Goal_

// alias to use template instance with default allocator
using Goal =
  dqn_msg::msg::Goal_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace dqn_msg

#endif  // DQN_MSG__MSG__DETAIL__GOAL__STRUCT_HPP_
