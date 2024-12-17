Lab 1 tasks:

The task is to create an asynchronous version of an array function (eg map, filter, some, find, findIndex). It is also necessary to add a function that provides an additional execution delay if the task completes in less time than a certain limit.

## Explanation of the code:

#### Debounce:

This function adds an additional delay to the execution if the operation took less time than specified by the delay parameter.
It takes a function to debounce (ie add a delay) and a delay time. The function is executed first, and if it executes faster than the limit, then additional delay is added.

Async_map:

This is an asynchronous version of map that takes an asynchronous function and a list of values ​​to apply the function to.
All operations are performed in parallel because we use asyncio.gather to run asynchronous tasks for each element of the list.

### Async_square:

This is an example of an asynchronous function that simply returns the square of a number with a delay of 2 seconds (simulating an asynchronous operation)

### Demo:

This is a demo function that shows how both functions work: async_map for asynchronous execution and debounce to add extra delay if a task is running too fast.
