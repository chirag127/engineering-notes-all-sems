### POSIX Threads

- POSIX Threads, or **pthreads**, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- Pthreads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- Pthreads is **independent** from a programming language, but it is mainly used with **C/C++** .
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same **address space**, **file descriptors**, **stack**, and other attributes with the process that created them.
- Threads can communicate with each other using **shared variables**, **mutexes**, **condition variables**, and other **synchronization primitives** .
- Threads can also create, join, detach, and cancel other threads .
- Threads can have different **scheduling policies** and **priorities** that affect their execution order and performance .
- Pthreads provides a set of **functions**, **header files**, and **data types** for threaded programming.
- Some of the common functions are:

  - `pthread_create()` - creates a new thread
  - `pthread_join()` - waits for a thread to terminate
  - `pthread_exit()` - terminates the calling thread
  - `pthread_detach()` - detaches a thread from the process
  - `pthread_cancel()` - requests the cancellation of a thread
  - `pthread_mutex_init()` - initializes a mutex
  - `pthread_mutex_lock()` - locks a mutex
  - `pthread_mutex_unlock()` - unlocks a mutex
  - `pthread_cond_init()` - initializes a condition variable
  - `pthread_cond_wait()` - waits on a condition variable
  - `pthread_cond_signal()` - signals a condition variable
  - `pthread_cond_broadcast()` - broadcasts a condition variable
  - `pthread_attr_init()` - initializes a thread attribute object
  - `pthread_attr_setdetachstate()` - sets the detach state of a thread attribute object
  - `pthread_attr_setschedpolicy()` - sets the scheduling policy of a thread attribute object
  - `pthread_attr_setschedparam()` - sets the scheduling parameters of a thread attribute object
  - `pthread_attr_destroy()` - destroys a thread attribute object
  - `pthread_self()` - returns the thread ID of the calling thread
  - `pthread_equal()` - compares two thread IDs
  - `pthread_getschedparam()` - gets the scheduling parameters of a thread
  - `pthread_setschedparam()` - sets the scheduling parameters of a thread
  - `pthread_once()` - executes a function only once in a process
  - `pthread_key_create()` - creates a thread-specific data key
  - `pthread_key_delete()` - deletes a thread-specific data key
  - `pthread_getspecific()` - gets the value of a thread-specific data key
  - `pthread_setspecific()` - sets the value of a thread-specific data key

- Some of the common header files are:

  - `<pthread.h>` - defines the pthreads API
  - `<sched.h>` - defines the scheduling policies and parameters
  - `<time.h>` - defines the time structures and functions

- Some of the common data types are:

  - `pthread_t` - represents a thread ID
  - `pthread_attr_t` - represents a thread attribute object
  - `pthread_mutex_t` - represents a mutex
  - `pthread_mutexattr_t` - represents a mutex attribute object
  - `pthread_cond_t` - represents a condition variable
  - `pthread_condattr_t` - represents a condition variable attribute object
  - `pthread_once_t` - represents a one-time initialization control
  - `pthread_key_t` - represents a thread-specific data key
  - `sched_param` - represents a scheduling parameter structure
  - `timespec` - represents a time structure

- A simple example of using pthreads is:

```c
#include <stdio.h>
#include <pthread.h>

// A function to be executed by a thread
void *hello(void *arg) {
  printf("Hello, %s!\n", (char *)arg);
  pthread_exit(NULL); // terminate the thread
}

int main() {