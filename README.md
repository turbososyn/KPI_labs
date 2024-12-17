# Lab 1 tasks:

The task is to create an asynchronous version of an array function (eg map, filter, some, find, findIndex). It is also necessary to add a function that provides an additional execution delay if the task completes in less time than a certain limit.

## Explanation of the code:

#### Debounce:

This function adds an additional delay to the execution if the operation took less time than specified by the delay parameter.
It takes a function to debounce (ie add a delay) and a delay time. The function is executed first, and if it executes faster than the limit, then additional delay is added.

#### Async_map:

This is an asynchronous version of map that takes an asynchronous function and a list of values ​​to apply the function to.
All operations are performed in parallel because we use asyncio.gather to run asynchronous tasks for each element of the list.

### Async_square:

This is an example of an asynchronous function that simply returns the square of a number with a delay of 2 seconds (simulating an asynchronous operation)

### Demo:

This is a demo function that shows how both functions work: async_map for asynchronous execution and debounce to add extra delay if a task is running too fast.

# Lab 2 task:

Create a Promise-based alternative to the async_map function and then write examples using both Promise-based and Async-Await solutions.

## Explanation of the code:

### Creating a Promise-based Alternative:
Python doesn't have a native Promise object like JavaScript, but we can use asyncio.create_task() to simulate the asynchronous behavior of Promises. This creates a task that can run concurrently with other tasks.
I created a helper function called promise_delay to wrap the asynchronous function and simulate the "Promise-like" behavior in Python. This wrapper is like the Promise constructor in JavaScript, which resolves the result asynchronously.

### Implement the promise_map Function:
The promise_map function is designed to map an asynchronous function (like async_square) onto an iterable and execute the functions concurrently.

### Creating the Async-Await Solution:
In the async-await solution, we simply use asyncio.gather (similar to Promise.all in JavaScript) to handle concurrent execution.
The async_map function is an asynchronous version of map that runs all tasks concurrently.

### Demonstrating the Promise and Async-Await Solutions:
To demonstrate the Promise-based solution, we create a list of "promises" using promise_map, and then we wait for all of them to resolve using handle_promises.
