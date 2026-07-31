# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time.
- The priority ceiling protocol can be used to control resource accesses in dynamic systems, provided the priority ceiling of each resource and the ceiling of the system are updated each time task priorities change.
- The protocol specifies a dynamic priority ceiling for each critical section, which is the earliest deadline of jobs that are currently in or will enter the critical section. Jobs trying to enter a critical section will be blocked if they do not have a priority higher than the priority ceiling of any critical section that is in use.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
