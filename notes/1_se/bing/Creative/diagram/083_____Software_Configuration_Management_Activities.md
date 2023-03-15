Software Configuration Management (SCM) is a process to systematically manage, organize, and control the changes in the documents, codes, and other entities during the Software Development Life Cycle. The primary goal is to increase productivity with minimal mistakes.

SCM includes following activities :

- Configuration identification – Identifying configurations, configuration items and baselines
- Configuration control – Implementing a controlled change process
- Configuration status accounting – Recording and reporting all the necessary information on the status of the development process
- Configuration auditing – Ensuring that configurations contain all their intended parts and are sound with respect to their specifying documents, including requirements, architectural specifications and user manuals
- Release management and delivery – Managing, storing, testing and delivering the configuration items

A possible diagram for SCM activities is:

### Software Configuration Management Activities

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Configuration   |     | Configuration   |     | Configuration   |
| Identification  |---->| Control         |---->| Status          |
|                 |     |                 |     | Accounting      |
+-----------------+     +-----------------+     +-----------------+
       ^                      ^    |                      |
       |                      |    |                      |
       |                      |    v                      |
       |                      | +-----------------+       |
       |                      | |                 |       |
       |                      | | Configuration   |       |
       |                      | | Auditing        |       |
       |                      | |                 |       |
       |                      | +-----------------+       |
       |                      |    |                      |
       |                      |    v                      |
       |                      | +-----------------+       |
       |                      | |                 |       |
       |                      | | Release         |       |
       |                      +-| Management and  |-------+
       |                        | Delivery        |
       +------------------------|                 |
                                +-----------------+
```