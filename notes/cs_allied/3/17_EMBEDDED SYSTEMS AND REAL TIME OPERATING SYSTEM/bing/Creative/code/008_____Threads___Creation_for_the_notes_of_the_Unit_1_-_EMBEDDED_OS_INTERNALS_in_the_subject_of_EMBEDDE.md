### Threads – Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread is also known as a lightweight process because it shares the same memory and resources as the program that created it.
- Threads can improve the performance and responsiveness of a program by dividing the workload among multiple execution units.
- Threads can also enable a program to take advantage of multiprocessor or multicore systems by running different threads on different cores or processors.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the program itself (user-level threads).
- Kernel-supported threads have the advantage of being recognized and scheduled by the operating system, but they incur more overhead and system calls than user-level threads.
- User-level threads have the advantage of being faster and more flexible than kernel-supported threads, but they are not visible to the operating system and may suffer from blocking or starvation issues.
- Some systems support a hybrid approach that combines both kernel-supported and user-level threads (e.g., POSIX threads or pthreads).
- To create a thread, a program typically needs to specify the following information:
  - The function or code segment that the thread will execute (also known as the entry point or the start routine).
  - The arguments or parameters that the thread will receive (if any).
  - The attributes or properties of the thread (e.g., priority, stack size, scheduling policy, etc.).
  - The identifier or handle of the thread (used to refer to the thread later).
- Depending on the system and the library used, the syntax and the semantics of thread creation may vary, but the general idea is similar.
- For example, in C using the pthread library, a thread can be created using the following function:

```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine) (void *), void *arg);
```

- The function returns 0 on success or an error code on failure.
- The first argument is a pointer to a variable that will store the thread identifier.
- The second argument is a pointer to a structure that contains the thread attributes (or NULL for default attributes).
- The third argument is a pointer to the function that the thread will execute.
- The fourth argument is a pointer to the argument that the thread will receive (or NULL if none).
- For example, the following code creates a thread that prints "Hello, world!" and passes the thread identifier as the argument:

```c
#include <stdio.h>
#include <pthread.h>

void *print_hello(void *arg) {
  pthread_t tid = (pthread_t) arg;
  printf("Hello, world! from thread %ld\n", tid);
  return NULL;
}

int main() {
  pthread_t thread;
  int rc = pthread_create(&thread, NULL, print_hello, (void *) thread);
  if (rc != 0) {
    printf("Error creating thread: %d\n", rc);
    return -1;
  }
  pthread_exit(NULL);
  return 0;
}
```

- The main function creates the thread and then exits, leaving the thread to run independently.
- The thread function prints the message and then returns NULL, indicating that it has finished its execution.
- Note that the thread identifier is passed as a void pointer and then cast back to a pthread_t type inside the thread function.