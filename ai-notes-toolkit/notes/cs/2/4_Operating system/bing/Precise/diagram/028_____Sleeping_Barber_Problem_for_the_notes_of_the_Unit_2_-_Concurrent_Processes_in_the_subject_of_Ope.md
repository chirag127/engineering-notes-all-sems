### Sleeping Barber Problem

The Sleeping Barber Problem is a classic inter-process communication and synchronization problem between multiple operating system processes. It is a part of the subject of Operating System, under the unit of Concurrent Processes.

The problem describes a scenario involving a barber shop with a barber, a barber chair, and a waiting room with a number of chairs. The barber can only cut one person's hair at a time, so when there are no customers, the barber goes to sleep in the barber chair. When a customer arrives, they must wake the barber to get their hair cut. If there are already customers waiting, the new customer sits in one of the waiting room chairs. If all the waiting room chairs are full, the new customer leaves.

The problem is to design a solution that coordinates the actions of the barber and the customers to ensure that:

1. Customers do not enter the barber shop if all the waiting room chairs are full.
2. The barber only cuts the hair of one customer at a time.
3. The barber sleeps if there are no customers.
4. A customer must wake the barber if the barber is sleeping.

This problem can be solved using semaphores and mutex locks to synchronize the actions of the barber and the customers. The solution must ensure that the barber and the customers do not access shared resources, such as the barber chair, at the same time.