// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dqn_msg:srv/Mac.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__MAC__TRAITS_HPP_
#define DQN_MSG__SRV__DETAIL__MAC__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dqn_msg/srv/detail/mac__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Mac_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: actions
  {
    if (msg.actions.size() == 0) {
      out << "actions: []";
    } else {
      out << "actions: [";
      size_t pending_items = msg.actions.size();
      for (auto item : msg.actions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: init
  {
    out << "init: ";
    rosidl_generator_traits::value_to_yaml(msg.init, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Mac_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: actions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.actions.size() == 0) {
      out << "actions: []\n";
    } else {
      out << "actions:\n";
      for (auto item : msg.actions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: init
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "init: ";
    rosidl_generator_traits::value_to_yaml(msg.init, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Mac_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_generator_traits
{

[[deprecated("use dqn_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dqn_msg::srv::Mac_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Mac_Request & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Mac_Request>()
{
  return "dqn_msg::srv::Mac_Request";
}

template<>
inline const char * name<dqn_msg::srv::Mac_Request>()
{
  return "dqn_msg/srv/Mac_Request";
}

template<>
struct has_fixed_size<dqn_msg::srv::Mac_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dqn_msg::srv::Mac_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dqn_msg::srv::Mac_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Mac_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: states
  {
    if (msg.states.size() == 0) {
      out << "states: []";
    } else {
      out << "states: [";
      size_t pending_items = msg.states.size();
      for (auto item : msg.states) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: rewards
  {
    if (msg.rewards.size() == 0) {
      out << "rewards: []";
    } else {
      out << "rewards: [";
      size_t pending_items = msg.rewards.size();
      for (auto item : msg.rewards) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: dones
  {
    if (msg.dones.size() == 0) {
      out << "dones: []";
    } else {
      out << "dones: [";
      size_t pending_items = msg.dones.size();
      for (auto item : msg.dones) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Mac_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: states
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.states.size() == 0) {
      out << "states: []\n";
    } else {
      out << "states:\n";
      for (auto item : msg.states) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: rewards
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.rewards.size() == 0) {
      out << "rewards: []\n";
    } else {
      out << "rewards:\n";
      for (auto item : msg.rewards) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: dones
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.dones.size() == 0) {
      out << "dones: []\n";
    } else {
      out << "dones:\n";
      for (auto item : msg.dones) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Mac_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_generator_traits
{

[[deprecated("use dqn_msg::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const dqn_msg::srv::Mac_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Mac_Response & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Mac_Response>()
{
  return "dqn_msg::srv::Mac_Response";
}

template<>
inline const char * name<dqn_msg::srv::Mac_Response>()
{
  return "dqn_msg/srv/Mac_Response";
}

template<>
struct has_fixed_size<dqn_msg::srv::Mac_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dqn_msg::srv::Mac_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dqn_msg::srv::Mac_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<dqn_msg::srv::Mac>()
{
  return "dqn_msg::srv::Mac";
}

template<>
inline const char * name<dqn_msg::srv::Mac>()
{
  return "dqn_msg/srv/Mac";
}

template<>
struct has_fixed_size<dqn_msg::srv::Mac>
  : std::integral_constant<
    bool,
    has_fixed_size<dqn_msg::srv::Mac_Request>::value &&
    has_fixed_size<dqn_msg::srv::Mac_Response>::value
  >
{
};

template<>
struct has_bounded_size<dqn_msg::srv::Mac>
  : std::integral_constant<
    bool,
    has_bounded_size<dqn_msg::srv::Mac_Request>::value &&
    has_bounded_size<dqn_msg::srv::Mac_Response>::value
  >
{
};

template<>
struct is_service<dqn_msg::srv::Mac>
  : std::true_type
{
};

template<>
struct is_service_request<dqn_msg::srv::Mac_Request>
  : std::true_type
{
};

template<>
struct is_service_response<dqn_msg::srv::Mac_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DQN_MSG__SRV__DETAIL__MAC__TRAITS_HPP_
