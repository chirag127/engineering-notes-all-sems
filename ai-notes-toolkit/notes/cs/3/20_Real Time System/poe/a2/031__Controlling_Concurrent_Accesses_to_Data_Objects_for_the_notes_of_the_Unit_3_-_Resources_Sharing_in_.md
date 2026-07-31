 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Controlling Concurrent Accesses to Data Objects

1. Mutual Exclusion - Only one process can access the shared data at a time. This prevents concurrently accessing and corrupting the data. This can be achieved using semaphores, monitors, message passing, etc.
2. Bounded Waiting - A process waiting to access the shared data must have a guaranteed upper bound on how long it has to wait. This can be ensured using priority inheritance protocols, lock protocols, etc.
3. No Starvation - A process must not be starved of access to the shared data. Each process must get a fair share of access. This can be ensured using timing wheel, aging techniques, randomized algorithms, etc.

The above measures ensure correct synchronization and control of concurrent accesses to shared data objects in a Real-Time System. This is crucial for predictability and timeliness of a system.

How's this? I have written the content in points in a formal tone without any emojis or external links as instructed. Let me know if you would like me to modify or expand the answer.