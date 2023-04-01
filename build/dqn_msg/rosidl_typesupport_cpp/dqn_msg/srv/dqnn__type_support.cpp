// generated from rosidl_typesupport_cpp/resource/idl__type_support.cpp.em
// with input from dqn_msg:srv/Dqnn.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "dqn_msg/srv/detail/dqnn__struct.hpp"
#include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
#include "rosidl_typesupport_cpp/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Dqnn_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Dqnn_Request_type_support_ids_t;

static const _Dqnn_Request_type_support_ids_t _Dqnn_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Dqnn_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Dqnn_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Dqnn_Request_type_support_symbol_names_t _Dqnn_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, dqn_msg, srv, Dqnn_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, dqn_msg, srv, Dqnn_Request)),
  }
};

typedef struct _Dqnn_Request_type_support_data_t
{
  void * data[2];
} _Dqnn_Request_type_support_data_t;

static _Dqnn_Request_type_support_data_t _Dqnn_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Dqnn_Request_message_typesupport_map = {
  2,
  "dqn_msg",
  &_Dqnn_Request_message_typesupport_ids.typesupport_identifier[0],
  &_Dqnn_Request_message_typesupport_symbol_names.symbol_name[0],
  &_Dqnn_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Dqnn_Request_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Dqnn_Request_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<dqn_msg::srv::Dqnn_Request>()
{
  return &::dqn_msg::srv::rosidl_typesupport_cpp::Dqnn_Request_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, dqn_msg, srv, Dqnn_Request)() {
  return get_message_type_support_handle<dqn_msg::srv::Dqnn_Request>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "dqn_msg/srv/detail/dqnn__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Dqnn_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Dqnn_Response_type_support_ids_t;

static const _Dqnn_Response_type_support_ids_t _Dqnn_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Dqnn_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Dqnn_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Dqnn_Response_type_support_symbol_names_t _Dqnn_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, dqn_msg, srv, Dqnn_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, dqn_msg, srv, Dqnn_Response)),
  }
};

typedef struct _Dqnn_Response_type_support_data_t
{
  void * data[2];
} _Dqnn_Response_type_support_data_t;

static _Dqnn_Response_type_support_data_t _Dqnn_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Dqnn_Response_message_typesupport_map = {
  2,
  "dqn_msg",
  &_Dqnn_Response_message_typesupport_ids.typesupport_identifier[0],
  &_Dqnn_Response_message_typesupport_symbol_names.symbol_name[0],
  &_Dqnn_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Dqnn_Response_message_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Dqnn_Response_message_typesupport_map),
  ::rosidl_typesupport_cpp::get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<dqn_msg::srv::Dqnn_Response>()
{
  return &::dqn_msg::srv::rosidl_typesupport_cpp::Dqnn_Response_message_type_support_handle;
}

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_cpp, dqn_msg, srv, Dqnn_Response)() {
  return get_message_type_support_handle<dqn_msg::srv::Dqnn_Response>();
}

#ifdef __cplusplus
}
#endif
}  // namespace rosidl_typesupport_cpp

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "dqn_msg/srv/detail/dqnn__struct.hpp"
// already included above
// #include "rosidl_typesupport_cpp/identifier.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_cpp/service_type_support_dispatch.hpp"
// already included above
// #include "rosidl_typesupport_cpp/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_cpp
{

typedef struct _Dqnn_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Dqnn_type_support_ids_t;

static const _Dqnn_type_support_ids_t _Dqnn_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_cpp",  // ::rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
    "rosidl_typesupport_introspection_cpp",  // ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  }
};

typedef struct _Dqnn_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Dqnn_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Dqnn_type_support_symbol_names_t _Dqnn_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, dqn_msg, srv, Dqnn)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, dqn_msg, srv, Dqnn)),
  }
};

typedef struct _Dqnn_type_support_data_t
{
  void * data[2];
} _Dqnn_type_support_data_t;

static _Dqnn_type_support_data_t _Dqnn_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Dqnn_service_typesupport_map = {
  2,
  "dqn_msg",
  &_Dqnn_service_typesupport_ids.typesupport_identifier[0],
  &_Dqnn_service_typesupport_symbol_names.symbol_name[0],
  &_Dqnn_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t Dqnn_service_type_support_handle = {
  ::rosidl_typesupport_cpp::typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Dqnn_service_typesupport_map),
  ::rosidl_typesupport_cpp::get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_cpp

}  // namespace srv

}  // namespace dqn_msg

namespace rosidl_typesupport_cpp
{

template<>
ROSIDL_TYPESUPPORT_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<dqn_msg::srv::Dqnn>()
{
  return &::dqn_msg::srv::rosidl_typesupport_cpp::Dqnn_service_type_support_handle;
}

}  // namespace rosidl_typesupport_cpp
