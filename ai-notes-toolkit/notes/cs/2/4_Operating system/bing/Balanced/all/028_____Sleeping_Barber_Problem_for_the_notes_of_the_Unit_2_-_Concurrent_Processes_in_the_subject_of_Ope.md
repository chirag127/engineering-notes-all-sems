# Sleeping Barber Problem

The sleeping barber problem is a classic inter-process communication and synchronization problem that illustrates the complexities that arise when there are multiple operating system processes. The problem was originally proposed by Edsger Dijkstra in 1965.

## Problem Statement

The problem is based on a hypothetical barber shop with one barber, one barber chair, and n chairs for waiting customers. The barber has two states: sleeping or cutting hair. When the shop is empty, the barber sleeps on the barber chair. When a customer arrives, he either wakes up the barber or waits on one of the chairs if the barber is busy. If all the chairs are occupied, the customer leaves the shop.

The problem is to synchronize the barber and the customers using semaphores or mutexes, so that the barber does not sleep when there is a customer waiting, and the customers do not enter the shop when there is no available chair.

## Solution

One possible solution is to use three semaphores: customers, barber, and mutex. The customers semaphore counts the number of customers waiting in the shop. The barber semaphore is a signal for the barber to wake up and start cutting hair. The mutex is used to ensure mutual exclusion when accessing the shared variable waiting, which represents the number of customers waiting on the chairs.

The pseudocode for the barber and customer processes are as follows:

```
barber:
  while true:
    wait(customers) // wait for a customer
    wait(mutex) // lock the access to waiting
    waiting = waiting - 1 // decrement the number of waiting customers
    signal(barber) // signal the barber to start cutting hair
    signal(mutex) // unlock the access to waiting
    cut_hair() // cut hair for some time

customer:
  wait(mutex) // lock the access to waiting
  if waiting < n: // if there is an available chair
    waiting = waiting + 1 // increment the number of waiting customers
    signal(customers) // signal that there is a customer
    signal(mutex) // unlock the access to waiting
    wait(barber) // wait for the barber to cut hair
    get_haircut() // get haircut for some time
  else: // if there is no available chair
    signal(mutex) // unlock the access to waiting
    leave_shop() // leave the shop without haircut
```

## Analysis

The solution ensures that the barber and the customers are synchronized correctly. The barber sleeps when there are no customers, and wakes up when there is at least one customer. The customers enter the shop only when there is an available chair, and wait for their turn to get a haircut. The mutex prevents race conditions when accessing the shared variable waiting.

The solution also avoids deadlock and starvation. Deadlock occurs when two or more processes are waiting for each other to release a resource, and none of them can proceed. Starvation occurs when a process is indefinitely postponed by other processes with higher priority or frequency. In the solution, deadlock is avoided because the barber and the customers do not hold any resources while waiting for each other. Starvation is avoided because the customers are served in a first-come first-served order, and no customer can be skipped or delayed indefinitely.

## References

: Sleeping barber problem - Wikipedia. https://en.wikipedia.org/wiki/Sleeping_barber_problem