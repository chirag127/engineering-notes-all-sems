### Sleeping Barber Problem

The Sleeping Barber Problem is a classic inter-process communication and synchronization problem between multiple operating system processes. The problem is analogous to that of keeping a barber working when there are customers, resting when there are none, and doing so in an orderly manner.

The problem can be described as follows:
- There is a barber shop with a barber, a barber chair, and a waiting room with a certain number of chairs.
- If there are no customers, the barber sits in the barber chair and sleeps.
- When a customer arrives, they must wake the barber.
- If there are available chairs in the waiting room, customers can sit and wait for their turn.
- If there are no available chairs, the customer leaves.
- When the barber finishes with a customer, they dismiss the customer and check if there are others waiting.
- If there are customers waiting, the barber calls the next customer and starts cutting their hair.
- If there are no customers waiting, the barber goes back to sleep.

The problem is to design a solution that ensures that:
- Customers are served in the order they arrive.
- The barber is not cutting hair when there are no customers.
- No customers are waiting when the barber is available.

This problem can be solved using semaphores and mutex locks to synchronize the actions of the barber and the customers. The solution must ensure that the barber and the customers do not access shared resources (such as the waiting room chairs) at the same time, and that the barber is not woken up unnecessarily.