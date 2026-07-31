Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Embedded Systems and Real Time Operating Systems. Here are some notes on the topic of Cancellation for the Unit 1 - Embedded OS Internals.

### Cancellation

- Cancellation is the mechanism by which a thread can terminate the execution of another thread before it completes normally.
- Cancellation can be either **asynchronous** or **deferred**.
- Asynchronous cancellation means that the target thread is terminated immediately when the cancellation request is issued.
- Deferred cancellation means that the target thread periodically checks a flag to see if it should terminate itself.
- The advantages of asynchronous cancellation are that it is fast and simple, but the disadvantages are that it can leave the system in an inconsistent state and cause resource leaks.
- The advantages of deferred cancellation are that it is safer and more predictable, but the disadvantages are that it requires the cooperation of the target thread and can introduce delays and overhead.
- The POSIX standard defines two types of cancellation points: **mandatory** and **optional**.
- Mandatory cancellation points are functions that must check for cancellation requests and act accordingly. Some examples are pthread_join, pthread_cond_wait, and read.
- Optional cancellation points are functions that may or may not check for cancellation requests, depending on the implementation. Some examples are printf, malloc, and sleep.
- A thread can control its own cancellation behavior by using the functions pthread_setcancelstate and pthread_setcanceltype.
- A thread can also create cancellation handlers, which are functions that are executed when the thread is cancelled. Cancellation handlers are useful for cleaning up resources and restoring the system state. They are registered and deregistered by using the functions pthread_cleanup_push and pthread_cleanup_pop.