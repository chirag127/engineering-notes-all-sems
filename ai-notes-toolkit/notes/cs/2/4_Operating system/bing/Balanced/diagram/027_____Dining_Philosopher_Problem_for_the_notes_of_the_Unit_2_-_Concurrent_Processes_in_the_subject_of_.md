### Dining Philosopher Problem

- The dining philosopher problem is a classic synchronization problem in computer science, which illustrates the challenges of managing concurrent processes that share resources .
- The problem was originally formulated by Edsger Dijkstra in 1965 as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals.
- The problem can be described as follows    :
  - There are five philosophers sitting around a circular table, each with a plate of noodles in front of them.
  - There are five chopsticks on the table, one between each pair of adjacent philosophers.
  - Each philosopher alternates between thinking and eating. To eat, a philosopher needs to pick up both chopsticks on either side of their plate.
  - A chopstick can be used by only one philosopher at a time. If a chopstick is unavailable, the philosopher has to wait until it is free.
  - The problem is to design a protocol that allows each philosopher to eat without causing a deadlock or starvation.
- A deadlock occurs when all philosophers pick up the chopstick on their left (or right) and wait for the chopstick on their right (or left), thus preventing anyone from eating  .
- A starvation occurs when one or more philosophers are unable to eat for an indefinite period of time, because the chopsticks are always occupied by their neighbors  .
- The problem can be generalized to N philosophers and N chopsticks, or to other scenarios involving multiple processes and shared resources .
- The problem can be solved using various synchronization techniques, such as semaphores, monitors, locks, or message passing   .
- The problem can also be used to illustrate the trade-offs between fairness, efficiency, and simplicity in concurrent algorithm design .

The following diagram shows the dining philosopher problem with five philosophers and five chopsticks:

```
   P1
 C4   C0
P4     P2
 C3   C1
   P3
```

P: Philosopher
C: Chopstick

: https://zerobone.net/blog/cs/dining-philosophers-problem/
: https://www.javatpoint.com/os-dining-philosophers-problem
: https://www.studytonight.com/operating-system/dining-philosophers-problem
: https://en.wikipedia.org/wiki/Dining_philosophers_problem
: https://www.geeksforgeeks.org/dining-philosophers-problem/