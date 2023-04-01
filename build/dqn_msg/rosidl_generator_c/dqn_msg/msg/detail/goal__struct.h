// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef DQN_MSG__MSG__DETAIL__GOAL__STRUCT_H_
#define DQN_MSG__MSG__DETAIL__GOAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'goal'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/Goal in the package dqn_msg.
typedef struct dqn_msg__msg__Goal
{
  rosidl_runtime_c__double__Sequence goal;
} dqn_msg__msg__Goal;

// Struct for a sequence of dqn_msg__msg__Goal.
typedef struct dqn_msg__msg__Goal__Sequence
{
  dqn_msg__msg__Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} dqn_msg__msg__Goal__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DQN_MSG__MSG__DETAIL__GOAL__STRUCT_H_
