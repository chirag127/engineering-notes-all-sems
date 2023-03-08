### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that prevents priority inversion and deadlock  .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are as follows :
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at that time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and it inherits the locks of all the lower-priority tasks that are blocked on that resource or any other resource with a lower or equal priority ceiling.
  - When a task unlocks a resource, its priority is restored to its original value, and it releases the locks of all the lower-priority tasks that it inherited.
- The advantages of SBPCP are  :
  - It prevents priority inversion by ensuring that a higher-priority task can always preempt a lower-priority task that holds a resource that it needs.
  - It prevents deadlock by ensuring that a task can lock a resource only if it does not cause a circular wait among the tasks.
  - It reduces blocking time by allowing a task to lock multiple resources at once, and by avoiding unnecessary priority inheritance.
  - It allows nested resource access by using a stack to store the original priorities and inherited locks of the tasks.
- The disadvantages of SBPCP are  :
  - It requires a priori knowledge of the resource usage and the task priorities to assign the priority ceilings.
  - It may cause unnecessary priority raising if a task locks a resource that is not needed by any higher-priority task.
  - It may cause unnecessary context switches if a task unlocks a resource that is needed by a lower-priority task that it inherited.
- An example of SBPCP is shown in the following table :

| Time | Task 1 | Task 2 | Task 3 | Resource A | Resource B | System Ceiling |
|------|--------|--------|--------|------------|------------|----------------|
| 0    | Ready  | Ready  | Ready  | Free       | Free       | -              |
| 1    | Run    | Ready  | Ready  | Free       | Free       | -              |
| 2    | Lock A | Ready  | Ready  | Locked by 1| Free       | 1              |
| 3    | Run    | Ready  | Ready  | Locked by 1| Free       | 1              |
| 4    | Run    | Preempt| Ready  | Locked by 1| Free       | 1              |
| 5    | Run    | Blocked| Ready  | Locked by 1| Free       | 1              |
| 6    | Run    | Blocked| Preempt| Locked by 1| Free       | 1              |
| 7    | Run    | Blocked| Blocked| Locked by 1| Free       | 1              |
| 8    | Lock B | Blocked| Blocked| Locked by 1| Locked by 1| 1              |
| 9    | Run    | Blocked| Blocked| Locked by 1| Locked by 1| 1              |
| 10   | Unlock B| Blocked| Blocked| Locked by 1| Free       | 1              |
| 11   | Run    | Blocked| Blocked| Locked by 1| Free       | 1              |
| 12   | Unlock A| Run    | Blocked| Free       | Free       | -              |
| 13   | Ready  | Run    | Blocked| Free       | Free       | -              |
| 14   | Ready  | Lock A | Blocked| Locked by 2| Free       | 2              |
| 15   | Ready  | Run    | Blocked| Locked by 2| Free       | 2              |
|

I'm not sure what topic you are referring to, but I can try to help you find some good mnemonics and learning tricks if you tell me more. What are you studying or trying to learn?