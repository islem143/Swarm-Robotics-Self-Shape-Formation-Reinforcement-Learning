// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from dqn_msg:srv/Mac.idl
// generated code does not contain a copyright notice
#include "dqn_msg/srv/detail/mac__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `actions`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
dqn_msg__srv__Mac_Request__init(dqn_msg__srv__Mac_Request * msg)
{
  if (!msg) {
    return false;
  }
  // actions
  if (!rosidl_runtime_c__float__Sequence__init(&msg->actions, 0)) {
    dqn_msg__srv__Mac_Request__fini(msg);
    return false;
  }
  // init
  return true;
}

void
dqn_msg__srv__Mac_Request__fini(dqn_msg__srv__Mac_Request * msg)
{
  if (!msg) {
    return;
  }
  // actions
  rosidl_runtime_c__float__Sequence__fini(&msg->actions);
  // init
}

bool
dqn_msg__srv__Mac_Request__are_equal(const dqn_msg__srv__Mac_Request * lhs, const dqn_msg__srv__Mac_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // actions
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->actions), &(rhs->actions)))
  {
    return false;
  }
  // init
  if (lhs->init != rhs->init) {
    return false;
  }
  return true;
}

bool
dqn_msg__srv__Mac_Request__copy(
  const dqn_msg__srv__Mac_Request * input,
  dqn_msg__srv__Mac_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // actions
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->actions), &(output->actions)))
  {
    return false;
  }
  // init
  output->init = input->init;
  return true;
}

dqn_msg__srv__Mac_Request *
dqn_msg__srv__Mac_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Request * msg = (dqn_msg__srv__Mac_Request *)allocator.allocate(sizeof(dqn_msg__srv__Mac_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(dqn_msg__srv__Mac_Request));
  bool success = dqn_msg__srv__Mac_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
dqn_msg__srv__Mac_Request__destroy(dqn_msg__srv__Mac_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    dqn_msg__srv__Mac_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
dqn_msg__srv__Mac_Request__Sequence__init(dqn_msg__srv__Mac_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Request * data = NULL;

  if (size) {
    data = (dqn_msg__srv__Mac_Request *)allocator.zero_allocate(size, sizeof(dqn_msg__srv__Mac_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = dqn_msg__srv__Mac_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        dqn_msg__srv__Mac_Request__fini(&data[i - 1]);
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
dqn_msg__srv__Mac_Request__Sequence__fini(dqn_msg__srv__Mac_Request__Sequence * array)
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
      dqn_msg__srv__Mac_Request__fini(&array->data[i]);
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

dqn_msg__srv__Mac_Request__Sequence *
dqn_msg__srv__Mac_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Request__Sequence * array = (dqn_msg__srv__Mac_Request__Sequence *)allocator.allocate(sizeof(dqn_msg__srv__Mac_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = dqn_msg__srv__Mac_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
dqn_msg__srv__Mac_Request__Sequence__destroy(dqn_msg__srv__Mac_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    dqn_msg__srv__Mac_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
dqn_msg__srv__Mac_Request__Sequence__are_equal(const dqn_msg__srv__Mac_Request__Sequence * lhs, const dqn_msg__srv__Mac_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!dqn_msg__srv__Mac_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
dqn_msg__srv__Mac_Request__Sequence__copy(
  const dqn_msg__srv__Mac_Request__Sequence * input,
  dqn_msg__srv__Mac_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(dqn_msg__srv__Mac_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    dqn_msg__srv__Mac_Request * data =
      (dqn_msg__srv__Mac_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!dqn_msg__srv__Mac_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          dqn_msg__srv__Mac_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!dqn_msg__srv__Mac_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `states`
// Member `rewards`
// Member `dones`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
dqn_msg__srv__Mac_Response__init(dqn_msg__srv__Mac_Response * msg)
{
  if (!msg) {
    return false;
  }
  // states
  if (!rosidl_runtime_c__float__Sequence__init(&msg->states, 0)) {
    dqn_msg__srv__Mac_Response__fini(msg);
    return false;
  }
  // rewards
  if (!rosidl_runtime_c__float__Sequence__init(&msg->rewards, 0)) {
    dqn_msg__srv__Mac_Response__fini(msg);
    return false;
  }
  // dones
  if (!rosidl_runtime_c__boolean__Sequence__init(&msg->dones, 0)) {
    dqn_msg__srv__Mac_Response__fini(msg);
    return false;
  }
  return true;
}

void
dqn_msg__srv__Mac_Response__fini(dqn_msg__srv__Mac_Response * msg)
{
  if (!msg) {
    return;
  }
  // states
  rosidl_runtime_c__float__Sequence__fini(&msg->states);
  // rewards
  rosidl_runtime_c__float__Sequence__fini(&msg->rewards);
  // dones
  rosidl_runtime_c__boolean__Sequence__fini(&msg->dones);
}

bool
dqn_msg__srv__Mac_Response__are_equal(const dqn_msg__srv__Mac_Response * lhs, const dqn_msg__srv__Mac_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // states
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->states), &(rhs->states)))
  {
    return false;
  }
  // rewards
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->rewards), &(rhs->rewards)))
  {
    return false;
  }
  // dones
  if (!rosidl_runtime_c__boolean__Sequence__are_equal(
      &(lhs->dones), &(rhs->dones)))
  {
    return false;
  }
  return true;
}

bool
dqn_msg__srv__Mac_Response__copy(
  const dqn_msg__srv__Mac_Response * input,
  dqn_msg__srv__Mac_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // states
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->states), &(output->states)))
  {
    return false;
  }
  // rewards
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->rewards), &(output->rewards)))
  {
    return false;
  }
  // dones
  if (!rosidl_runtime_c__boolean__Sequence__copy(
      &(input->dones), &(output->dones)))
  {
    return false;
  }
  return true;
}

dqn_msg__srv__Mac_Response *
dqn_msg__srv__Mac_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Response * msg = (dqn_msg__srv__Mac_Response *)allocator.allocate(sizeof(dqn_msg__srv__Mac_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(dqn_msg__srv__Mac_Response));
  bool success = dqn_msg__srv__Mac_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
dqn_msg__srv__Mac_Response__destroy(dqn_msg__srv__Mac_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    dqn_msg__srv__Mac_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
dqn_msg__srv__Mac_Response__Sequence__init(dqn_msg__srv__Mac_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Response * data = NULL;

  if (size) {
    data = (dqn_msg__srv__Mac_Response *)allocator.zero_allocate(size, sizeof(dqn_msg__srv__Mac_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = dqn_msg__srv__Mac_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        dqn_msg__srv__Mac_Response__fini(&data[i - 1]);
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
dqn_msg__srv__Mac_Response__Sequence__fini(dqn_msg__srv__Mac_Response__Sequence * array)
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
      dqn_msg__srv__Mac_Response__fini(&array->data[i]);
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

dqn_msg__srv__Mac_Response__Sequence *
dqn_msg__srv__Mac_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  dqn_msg__srv__Mac_Response__Sequence * array = (dqn_msg__srv__Mac_Response__Sequence *)allocator.allocate(sizeof(dqn_msg__srv__Mac_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = dqn_msg__srv__Mac_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
dqn_msg__srv__Mac_Response__Sequence__destroy(dqn_msg__srv__Mac_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    dqn_msg__srv__Mac_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
dqn_msg__srv__Mac_Response__Sequence__are_equal(const dqn_msg__srv__Mac_Response__Sequence * lhs, const dqn_msg__srv__Mac_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!dqn_msg__srv__Mac_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
dqn_msg__srv__Mac_Response__Sequence__copy(
  const dqn_msg__srv__Mac_Response__Sequence * input,
  dqn_msg__srv__Mac_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(dqn_msg__srv__Mac_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    dqn_msg__srv__Mac_Response * data =
      (dqn_msg__srv__Mac_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!dqn_msg__srv__Mac_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          dqn_msg__srv__Mac_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!dqn_msg__srv__Mac_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
