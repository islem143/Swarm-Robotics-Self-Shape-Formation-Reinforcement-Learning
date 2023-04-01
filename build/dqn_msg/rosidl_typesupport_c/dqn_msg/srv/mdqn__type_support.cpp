// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from dqn_msg:srv/Mdqn.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "dqn_msg/srv/detail/mdqn__struct.h"
#include "dqn_msg/srv/detail/mdqn__type_support.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _Mdqn_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Mdqn_Request_type_support_ids_t;

static const _Mdqn_Request_type_support_ids_t _Mdqn_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _Mdqn_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Mdqn_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Mdqn_Request_type_support_symbol_names_t _Mdqn_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mdqn_Request)),
  }
};

typedef struct _Mdqn_Request_type_support_data_t
{
  void * data[2];
} _Mdqn_Request_type_support_data_t;

static _Mdqn_Request_type_support_data_t _Mdqn_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Mdqn_Request_message_typesupport_map = {
  2,
  "dqn_msg",
  &_Mdqn_Request_message_typesupport_ids.typesupport_identifier[0],
  &_Mdqn_Request_message_typesupport_symbol_names.symbol_name[0],
  &_Mdqn_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Mdqn_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Mdqn_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace dqn_msg

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, dqn_msg, srv, Mdqn_Request)() {
  return &::dqn_msg::srv::rosidl_typesupport_c::Mdqn_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "dqn_msg/srv/detail/mdqn__struct.h"
// already included above
// #include "dqn_msg/srv/detail/mdqn__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _Mdqn_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Mdqn_Response_type_support_ids_t;

static const _Mdqn_Response_type_support_ids_t _Mdqn_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _Mdqn_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Mdqn_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Mdqn_Response_type_support_symbol_names_t _Mdqn_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mdqn_Response)),
  }
};

typedef struct _Mdqn_Response_type_support_data_t
{
  void * data[2];
} _Mdqn_Response_type_support_data_t;

static _Mdqn_Response_type_support_data_t _Mdqn_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Mdqn_Response_message_typesupport_map = {
  2,
  "dqn_msg",
  &_Mdqn_Response_message_typesupport_ids.typesupport_identifier[0],
  &_Mdqn_Response_message_typesupport_symbol_names.symbol_name[0],
  &_Mdqn_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t Mdqn_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Mdqn_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace dqn_msg

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, dqn_msg, srv, Mdqn_Response)() {
  return &::dqn_msg::srv::rosidl_typesupport_c::Mdqn_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "dqn_msg/srv/detail/mdqn__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace dqn_msg
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _Mdqn_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _Mdqn_type_support_ids_t;

static const _Mdqn_type_support_ids_t _Mdqn_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _Mdqn_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _Mdqn_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _Mdqn_type_support_symbol_names_t _Mdqn_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, dqn_msg, srv, Mdqn)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, dqn_msg, srv, Mdqn)),
  }
};

typedef struct _Mdqn_type_support_data_t
{
  void * data[2];
} _Mdqn_type_support_data_t;

static _Mdqn_type_support_data_t _Mdqn_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _Mdqn_service_typesupport_map = {
  2,
  "dqn_msg",
  &_Mdqn_service_typesupport_ids.typesupport_identifier[0],
  &_Mdqn_service_typesupport_symbol_names.symbol_name[0],
  &_Mdqn_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t Mdqn_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_Mdqn_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace dqn_msg

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, dqn_msg, srv, Mdqn)() {
  return &::dqn_msg::srv::rosidl_typesupport_c::Mdqn_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif
