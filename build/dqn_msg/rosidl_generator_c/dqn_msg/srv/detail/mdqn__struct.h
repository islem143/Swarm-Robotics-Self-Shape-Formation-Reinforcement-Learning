// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dqn_msg:srv/Mdqn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__MDQN__STRUCT_H_
#define DQN_MSG__SRV__DETAIL__MDQN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'actions'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/Mdqn in the package dqn_msg.
typedef struct dqn_msg__srv__Mdqn_Request
{
  rosidl_runtime_c__int8__Sequence actions;
  bool init;
} dqn_msg__srv__Mdqn_Request;

// Struct for a sequence of dqn_msg__srv__Mdqn_Request.
typedef struct dqn_msg__srv__Mdqn_Request__Sequence
{
  dqn_msg__srv__Mdqn_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Mdqn_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'states'
// Member 'rewards'
// Member 'dones'
// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/Mdqn in the package dqn_msg.
typedef struct dqn_msg__srv__Mdqn_Response
{
  rosidl_runtime_c__float__Sequence states;
  rosidl_runtime_c__float__Sequence rewards;
  rosidl_runtime_c__boolean__Sequence dones;
} dqn_msg__srv__Mdqn_Response;

// Struct for a sequence of dqn_msg__srv__Mdqn_Response.
typedef struct dqn_msg__srv__Mdqn_Response__Sequence
{
  dqn_msg__srv__Mdqn_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Mdqn_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DQN_MSG__SRV__DETAIL__MDQN__STRUCT_H_
