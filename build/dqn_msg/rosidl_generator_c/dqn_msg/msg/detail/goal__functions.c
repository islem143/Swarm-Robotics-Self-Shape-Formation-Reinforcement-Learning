// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from dqn_msg:msg/Goal.idl
// generated code does not contain a copyright notice
#include "dqn_msg/msg/detail/goal__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `goal`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
dqn_msg__msg__Goal__init(dqn_msg__msg__Goal * msg)
{
  if (!msg) {
    return false;
  }
  // goal
  if (!rosidl_runtime_c__double__Sequence__init(&msg->goal, 0)) {
    dqn_msg__msg__Goal__fini(msg);
    return false;
  }
  return true;
}

void
dqn_msg__msg__Goal__fini(dqn_msg__msg__Goal * msg)
{
  if (!msg) {
    return;
  }
  // goal
  rosidl_runtime_c__double__Sequence__fini(&msg->goal);
}

bool
dqn_msg__msg__Goal__are_equal(const dqn_msg__msg__Goal * lhs, const dqn_msg__msg__Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
dqn_msg__msg__Goal__copy(
  const dqn_msg__msg__Goal * input,
  dqn_msg__msg__Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // goal
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

dqn_msg__msg__Goal *
dqn_msg__msg__Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__msg__Goal * msg = (dqn_msg__msg__Goal *)allocator.allocate(sizeof(dqn_msg__msg__Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(dqn_msg__msg__Goal));
  bool success = dqn_msg__msg__Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
dqn_msg__msg__Goal__destroy(dqn_msg__msg__Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    dqn_msg__msg__Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
dqn_msg__msg__Goal__Sequence__init(dqn_msg__msg__Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__msg__Goal * data = NULL;

  if (size) {
    data = (dqn_msg__msg__Goal *)allocator.zero_allocate(size, sizeof(dqn_msg__msg__Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = dqn_msg__msg__Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        dqn_msg__msg__Goal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
dqn_msg__msg__Goal__Sequence__fini(dqn_msg__msg__Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      dqn_msg__msg__Goal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

dqn_msg__msg__Goal__Sequence *
dqn_msg__msg__Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__msg__Goal__Sequence * array = (dqn_msg__msg__Goal__Sequence *)allocator.allocate(sizeof(dqn_msg__msg__Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = dqn_msg__msg__Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
dqn_msg__msg__Goal__Sequence__destroy(dqn_msg__msg__Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    dqn_msg__msg__Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
dqn_msg__msg__Goal__Sequence__are_equal(const dqn_msg__msg__Goal__Sequence * lhs, const dqn_msg__msg__Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!dqn_msg__msg__Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
dqn_msg__msg__Goal__Sequence__copy(
  const dqn_msg__msg__Goal__Sequence * input,
  dqn_msg__msg__Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(dqn_msg__msg__Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    dqn_msg__msg__Goal * data =
      (dqn_msg__msg__Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!dqn_msg__msg__Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          dqn_msg__msg__Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!dqn_msg__msg__Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
