// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dqn_msg:srv/Dqnn.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__DQNN__STRUCT_H_
#define DQN_MSG__SRV__DETAIL__DQNN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Dqnn in the package dqn_msg.
typedef struct dqn_msg__srv__Dqnn_Request
{
  float action;
  uint8_t id;
  bool init;
} dqn_msg__srv__Dqnn_Request;

// Struct for a sequence of dqn_msg__srv__Dqnn_Request.
typedef struct dqn_msg__srv__Dqnn_Request__Sequence
{
  dqn_msg__srv__Dqnn_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Dqnn_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'state'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/Dqnn in the package dqn_msg.
typedef struct dqn_msg__srv__Dqnn_Response
{
  rosidl_runtime_c__float__Sequence state;
  float reward;
  bool done;
} dqn_msg__srv__Dqnn_Response;

// Struct for a sequence of dqn_msg__srv__Dqnn_Response.
typedef struct dqn_msg__srv__Dqnn_Response__Sequence
{
  dqn_msg__srv__Dqnn_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Dqnn_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DQN_MSG__SRV__DETAIL__DQNN__STRUCT_H_
