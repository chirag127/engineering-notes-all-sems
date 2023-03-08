### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance and Priority-Ceiling Protocols are two methods for solving the problem of unbounded priority inversion in real-time systems.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Priority-Inheritance Protocol (PIP) is a method that allows a low-priority task to temporarily inherit the priority of the highest-priority task that is blocked by it, until it releases the resource.
- Priority-Ceiling Protocol (PCP) is a method that assigns a ceiling priority to each resource, which is the highest priority of any task that can access the resource. A task can only lock a resource if its priority is higher than the ceiling priority of all the resources that are currently locked by other tasks.
- The advantages of PIP are:
  - It is simple to implement and understand.
  - It guarantees that a high-priority task will not be blocked for more than the duration of one critical section of a lower-priority task.
  - It prevents deadlocks that involve circular waits for resources.
- The disadvantages of PIP are:
  - It can cause unnecessary priority inheritance, when a low-priority task inherits the priority of a high-priority task that is not blocked by it, but by another task that holds a different resource.
  - It can cause chain blocking, when a high-priority task is blocked by a sequence of lower-priority tasks that inherit each other's priorities.
  - It can cause priority inversion to occur more than once for the same high-priority task, if it is blocked by different low-priority tasks at different times.
- The advantages of PCP are:
  - It minimizes the blocking time of a high-priority task to at most the duration of one critical section of a lower-priority task.
  - It prevents unnecessary priority inheritance and chain blocking, by allowing a low-priority task to lock a resource only if it does not block any higher-priority task.
  - It prevents deadlocks that involve circular waits for resources, as well as deadlocks that involve nested resource locking.
- The disadvantages of PCP are:
  - It requires a priori knowledge of the ceiling priorities of all the resources, which may not be available or may change dynamically.
  - It can cause blocking of a low-priority task by a higher-priority task that does not need the resource, but has a priority higher than the ceiling priority of the resource.
  - It can cause blocking of a high-priority task by a lower-priority task that holds a resource with a higher ceiling priority than the task's priority, even if the resource is not needed by any other task.

- An example of PIP and PCP is shown in the following table, where three tasks T1, T2, and T3 have priorities 3, 2, and 1 respectively, and two resources R1 and R2 have ceiling priorities 3 and 2 respectively.

| Time | PIP | PCP |
|------|-----|-----|
| 0    | T1 locks R1 | T1 locks R1 |
| 1    | T2 arrives and preempts T1 | T2 arrives and preempts T1 |
| 2    | T2 locks R2 | T2 locks R2 |
| 3    | T3 arrives and preempts T2 | T3 arrives and preempts T2 |
| 4    | T3 tries to lock R1, but is blocked by T1 | T3 tries to lock R1, but is blocked by the ceiling priority of R1 (3) |
| 5    | T1 inherits the priority of T3 (1) and preempts T3 | T1 preempts T3 |
| 6    | T1 releases R1 and reverts to its original priority (3) | T1 releases R1 |
| 7    | T3 resumes and locks R1 | T3 resumes and locks R1 |
| 8    | T3 releases R1 | T3 releases R1 |
| 9    | T2 resumes and releases R2 | T2 resumes and releases R2 |
| 10   | T1 resumes | T1 resumes |

- In this example, PIP causes T1 to inherit the priority of T3, which is unnecessary, since T3 is not blocked by T1, but by T2. PCP prevents this

Mnemonics are memory tricks that can help you remember new information by connecting it to something you already know. There are different types of mnemonics, such as rhymes, acronyms, diagrams, or images. For example, you can use the acronym HOMES to remember the names of the Great Lakes: Huron, Ontario, Michigan, Erie, and Superior. 

Some tips for using mnemonics effectively are  :

- Choose the appropriate mnemonic for your situation. For example, if you want to learn how to spell a word, you may want to use a spelling mnemonic, such as "there is a rat in separate".
- Practice the mnemonic several times to help you remember it. You can also repeat it to others or write it down.
- Use visual and/or acoustic cues to make the mnemonic more vivid and memorable. For example, you can imagine a picture of a rat in the word separate, or sing a song with the mnemonic in it.
- Use humor, exaggeration, or emotion to make the mnemonic more interesting and fun. For example, you can use a silly rhyme, such as "My very eager mother just served us nine pizzas" to remember the order of the planets in the solar system (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto).
- Review the mnemonic periodically to keep it fresh in your mind. You can also test yourself on the information you want to remember using the mnemonic as a cue.