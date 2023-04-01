// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dqn_msg:srv/Dqnn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__DQNN__TRAITS_HPP_
#define DQN_MSG__SRV__DETAIL__DQNN__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "dqn_msg/srv/detail/dqnn__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Dqnn_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: action
  {
    out << "action: ";
    rosidl_generator_traits::value_to_yaml(msg.action, out);
    out << ", ";
  }

  // member: id
  {
    out << "id: ";
    rosidl_generator_traits::value_to_yaml(msg.id, out);
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
  const Dqnn_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: action
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "action: ";
    rosidl_generator_traits::value_to_yaml(msg.action, out);
    out << "\n";
  }

  // member: id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "id: ";
    rosidl_generator_traits::value_to_yaml(msg.id, out);
    out << "\n";
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

inline std::string to_yaml(const Dqnn_Request & msg, bool use_flow_style = false)
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
  const dqn_msg::srv::Dqnn_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Dqnn_Request & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Dqnn_Request>()
{
  return "dqn_msg::srv::Dqnn_Request";
}

template<>
inline const char * name<dqn_msg::srv::Dqnn_Request>()
{
  return "dqn_msg/srv/Dqnn_Request";
}

template<>
struct has_fixed_size<dqn_msg::srv::Dqnn_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<dqn_msg::srv::Dqnn_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<dqn_msg::srv::Dqnn_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace dqn_msg
{

namespace srv
{

inline void to_flow_style_yaml(
  const Dqnn_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    if (msg.state.size() == 0) {
      out << "state: []";
    } else {
      out << "state: [";
      size_t pending_items = msg.state.size();
      for (auto item : msg.state) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: reward
  {
    out << "reward: ";
    rosidl_generator_traits::value_to_yaml(msg.reward, out);
    out << ", ";
  }

  // member: done
  {
    out << "done: ";
    rosidl_generator_traits::value_to_yaml(msg.done, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Dqnn_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.state.size() == 0) {
      out << "state: []\n";
    } else {
      out << "state:\n";
      for (auto item : msg.state) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: reward
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reward: ";
    rosidl_generator_traits::value_to_yaml(msg.reward, out);
    out << "\n";
  }

  // member: done
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "done: ";
    rosidl_generator_traits::value_to_yaml(msg.done, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Dqnn_Response & msg, bool use_flow_style = false)
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
  const dqn_msg::srv::Dqnn_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  dqn_msg::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use dqn_msg::srv::to_yaml() instead")]]
inline std::string to_yaml(const dqn_msg::srv::Dqnn_Response & msg)
{
  return dqn_msg::srv::to_yaml(msg);
}

template<>
inline const char * data_type<dqn_msg::srv::Dqnn_Response>()
{
  return "dqn_msg::srv::Dqnn_Response";
}

template<>
inline const char * name<dqn_msg::srv::Dqnn_Response>()
{
  return "dqn_msg/srv/Dqnn_Response";
}

template<>
struct has_fixed_size<dqn_msg::srv::Dqnn_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dqn_msg::srv::Dqnn_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dqn_msg::srv::Dqnn_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<dqn_msg::srv::Dqnn>()
{
  return "dqn_msg::srv::Dqnn";
}

template<>
inline const char * name<dqn_msg::srv::Dqnn>()
{
  return "dqn_msg/srv/Dqnn";
}

template<>
struct has_fixed_size<dqn_msg::srv::Dqnn>
  : std::integral_constant<
    bool,
    has_fixed_size<dqn_msg::srv::Dqnn_Request>::value &&
    has_fixed_size<dqn_msg::srv::Dqnn_Response>::value
  >
{
};

template<>
struct has_bounded_size<dqn_msg::srv::Dqnn>
  : std::integral_constant<
    bool,
    has_bounded_size<dqn_msg::srv::Dqnn_Request>::value &&
    has_bounded_size<dqn_msg::srv::Dqnn_Response>::value
  >
{
};

template<>
struct is_service<dqn_msg::srv::Dqnn>
  : std::true_type
{
};

template<>
struct is_service_request<dqn_msg::srv::Dqnn_Request>
  : std::true_type
{
};

template<>
struct is_service_response<dqn_msg::srv::Dqnn_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DQN_MSG__SRV__DETAIL__DQNN__TRAITS_HPP_
