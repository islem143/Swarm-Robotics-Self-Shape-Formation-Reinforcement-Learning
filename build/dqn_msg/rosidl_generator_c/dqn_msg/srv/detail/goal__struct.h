// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dqn_msg:srv/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__SRV__DETAIL__GOAL__STRUCT_H_
#define DQN_MSG__SRV__DETAIL__GOAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Goal in the package dqn_msg.
typedef struct dqn_msg__srv__Goal_Request
{
  uint8_t structure_needs_at_least_one_member;
} dqn_msg__srv__Goal_Request;

// Struct for a sequence of dqn_msg__srv__Goal_Request.
typedef struct dqn_msg__srv__Goal_Request__Sequence
{
  dqn_msg__srv__Goal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Goal_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Goal in the package dqn_msg.
typedef struct dqn_msg__srv__Goal_Response
{
  float x;
  float y;
} dqn_msg__srv__Goal_Response;

// Struct for a sequence of dqn_msg__srv__Goal_Response.
typedef struct dqn_msg__srv__Goal_Response__Sequence
{
  dqn_msg__srv__Goal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__srv__Goal_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DQN_MSG__SRV__DETAIL__GOAL__STRUCT_H_
