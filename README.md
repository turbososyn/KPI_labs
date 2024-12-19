# Lab 1 task:

The task is to create an asynchronous version of an array function (eg map, filter, some, find, findIndex). It is also necessary to add a function that provides an additional execution delay if the task completes in less time than a certain limit.

## Explanation of the code:

#### Debounce:

This function adds an additional delay to the execution if the operation took less time than specified by the delay parameter.
It takes a function to debounce (ie add a delay) and a delay time. The function is executed first, and if it executes faster than the limit, then additional delay is added.

### Async_map:

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

# Lab 3 task:

Task 3 is about integrating a cancellation mechanism into asynchronous operations, allowing tasks to be aborted if needed.

In JavaScript, you use AbortController to cancel tasks, while in Python, we use asyncio.CancelledError and task.cancel() to cancel ongoing async tasks.

### Key points:

Cancellation Support: You can cancel tasks (e.g., network requests, long computations) before they finish.

Graceful Handling: When a task is cancelled, it raises an error like CancelledError to stop execution cleanly.

## Explanation of the code:

### Async_map Function:

This function processes each element in an array asynchronously using the async_fn function (which simulates an asynchronous operation). It creates tasks for each item in the array, runs them concurrently, and collects the results.
The try block waits for all tasks to complete using asyncio.gather. If any task is cancelled, it catches the CancelledError and prints a cancellation message.

### Async_operation Function:

This function simulates an asynchronous task (e.g., multiplying a number) that can be cancelled. It sleeps for 1 second to simulate a delay, and if the task is cancelled, it raises a CancelledError to stop further execution.

### Cancel_operation Function:

This function waits for 1.5 seconds (to allow some tasks to run) and then cancels all tasks by calling task.cancel(). This simulates cancelling the operation prematurely.

### Main Function:

This function is the entry point of the program. It sets up the array of data, creates tasks, and calls the async_map function. It also starts the task to cancel the operation after 1.5 seconds.

### Running the Code:

The asyncio.run(main()) line runs the entire program. It schedules all tasks and waits for them to finish or be cancelled.