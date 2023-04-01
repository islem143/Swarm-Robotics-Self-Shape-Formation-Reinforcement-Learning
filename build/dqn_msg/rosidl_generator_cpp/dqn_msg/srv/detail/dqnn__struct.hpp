// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from dqn_msg:srv/Dqnn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__DQNN__STRUCT_HPP_
#define DQN_MSG__SRV__DETAIL__DQNN__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__dqn_msg__srv__Dqnn_Request __attribute__((deprecated))
#else
# define DEPRECATED__dqn_msg__srv__Dqnn_Request __declspec(deprecated)
#endif

namespace dqn_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Dqnn_Request_
{
  using Type = Dqnn_Request_<ContainerAllocator>;

  explicit Dqnn_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->action = 0.0f;
      this->id = 0;
      this->init = false;
    }
  }

  explicit Dqnn_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->action = 0.0f;
      this->id = 0;
      this->init = false;
    }
  }

  // field types and members
  using _action_type =
    float;
  _action_type action;
  using _id_type =
    uint8_t;
  _id_type id;
  using _init_type =
    bool;
  _init_type init;

  // setters for named parameter idiom
  Type & set__action(
    const float & _arg)
  {
    this->action = _arg;
    return *this;
  }
  Type & set__id(
    const uint8_t & _arg)
  {
    this->id = _arg;
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
    dqn_msg::srv::Dqnn_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const dqn_msg::srv::Dqnn_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Dqnn_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Dqnn_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dqn_msg__srv__Dqnn_Request
    std::shared_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dqn_msg__srv__Dqnn_Request
    std::shared_ptr<dqn_msg::srv::Dqnn_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dqnn_Request_ & other) const
  {
    if (this->action != other.action) {
      return false;
    }
    if (this->id != other.id) {
      return false;
    }
    if (this->init != other.init) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dqnn_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dqnn_Request_

// alias to use template instance with default allocator
using Dqnn_Request =
  dqn_msg::srv::Dqnn_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace dqn_msg


#ifndef _WIN32
# define DEPRECATED__dqn_msg__srv__Dqnn_Response __attribute__((deprecated))
#else
# define DEPRECATED__dqn_msg__srv__Dqnn_Response __declspec(deprecated)
#endif

namespace dqn_msg
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Dqnn_Response_
{
  using Type = Dqnn_Response_<ContainerAllocator>;

  explicit Dqnn_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reward = 0.0f;
      this->done = false;
    }
  }

  explicit Dqnn_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reward = 0.0f;
      this->done = false;
    }
  }

  // field types and members
  using _state_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _state_type state;
  using _reward_type =
    float;
  _reward_type reward;
  using _done_type =
    bool;
  _done_type done;

  // setters for named parameter idiom
  Type & set__state(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__reward(
    const float & _arg)
  {
    this->reward = _arg;
    return *this;
  }
  Type & set__done(
    const bool & _arg)
  {
    this->done = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    dqn_msg::srv::Dqnn_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const dqn_msg::srv::Dqnn_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Dqnn_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      dqn_msg::srv::Dqnn_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__dqn_msg__srv__Dqnn_Response
    std::shared_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__dqn_msg__srv__Dqnn_Response
    std::shared_ptr<dqn_msg::srv::Dqnn_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Dqnn_Response_ & other) const
  {
    if (this->state != other.state) {
      return false;
    }
    if (this->reward != other.reward) {
      return false;
    }
    if (this->done != other.done) {
      return false;
    }
    return true;
  }
  bool operator!=(const Dqnn_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Dqnn_Response_

// alias to use template instance with default allocator
using Dqnn_Response =
  dqn_msg::srv::Dqnn_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace dqn_msg

namespace dqn_msg
{

namespace srv
{

struct Dqnn
{
  using Request = dqn_msg::srv::Dqnn_Request;
  using Response = dqn_msg::srv::Dqnn_Response;
};

}  // namespace srv

}  // namespace dqn_msg

#endif  // DQN_MSG__SRV__DETAIL__DQNN__STRUCT_HPP_
