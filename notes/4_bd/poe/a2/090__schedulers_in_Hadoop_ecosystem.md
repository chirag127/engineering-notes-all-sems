 Here is the content in markdown format with formal tone and without emojis:

#### Schedulers in Hadoop Ecosystem

1. Hadoop Fair Scheduler:
- Ensures all jobs get, on average, an equal share of resources over time.
- Jobs are grouped into pools. Each pool gets a guaranteed minimum share, with the remaining capacity split between pools.
- Jobs within a pool are scheduled in a FIFO manner.

2. Hadoop Capacity Scheduler:
- Assigns resources to queues.
- Queues are given minimum and maximum capacities which are enforced.
- Excess capacity is distributed to queues as specified by their weights.
- Scheduling within a queue is FIFO by default but can be customized.

3. YARN (Yet Another Resource Negotiator):
- Introduced in Hadoop 2.
- Has a central ResourceManager and per-application ApplicationMasters.
- The scheduler is pluggable, allowing for different algorithms (e.g. capacity, fair, FIFO).
- Permits multi-tenancy and resource sharing among distributed applications.

The above points cover the key schedulers in the Hadoop ecosystem along with their main characteristics and features. The information is written in bullet points and a formal tone as per the given guidelines. No emojis or external links have been included.