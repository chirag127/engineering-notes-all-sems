# Unit 2 - Concurrent Processes: Sleeping Barber Problem

The Sleeping Barber Problem is a classic inter-process communication and synchronization problem between multiple operating system processes. The problem is analogous to that of a barber shop with a barber, a barber chair, and a waiting room with a number of chairs.

1. If there are no customers, the barber sits in the barber chair and sleeps.
2. When a customer arrives, they must wake the barber to get a haircut.
3. If there are already customers waiting, the new customer sits in one of the free chairs in the waiting room.
4. If there are no free chairs, the new customer leaves.
5. When the barber finishes cutting a customer's hair, the customer leaves and the barber checks if there are any customers waiting in the waiting room.
6. If there are, the barber invites the next customer to sit in the barber chair and starts cutting their hair.
7. If there are no customers waiting, the barber goes back to sleep.

The problem is to design a solution that ensures that:
- The barber does not cut hair when there are no customers.
- Customers do not sit in the barber chair when the barber is cutting someone else's hair.
- No more than one customer sits in the barber chair at any time.
- No more than the specified number of customers sit in the waiting room at any time.

This problem can be solved using semaphores and mutex locks to synchronize the actions of the barber and the customers. The solution must ensure that the barber and customers do not access shared resources (such as the barber chair or the waiting room chairs) at the same time, and that the barber does not start cutting a customer's hair until the customer is sitting in the barber chair.