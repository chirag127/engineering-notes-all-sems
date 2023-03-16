## Unit 7 - Fault Tolerance

Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as redundancy, replication, recovery, and reconfiguration.

- Redundancy: The provision of extra components or resources that can take over the function of a failed component or resource. Redundancy can be static (predefined) or dynamic (allocated on demand).
- Replication: The creation of multiple copies of data or services that can be accessed in parallel or in case of failure. Replication can be passive (one primary and multiple backups) or active (all replicas are equal).
- Recovery: The process of restoring a system to a consistent and correct state after a failure. Recovery can be backward (undoing the effects of a failure) or forward (compensating for the effects of a failure).
- Reconfiguration: The process of changing the structure or parameters of a system to adapt to a failure or a changing environment. Reconfiguration can be manual (initiated by a human) or automatic (initiated by the system).

Fault tolerance can be measured by metrics such as availability, reliability, and mean time to failure (MTTF).

- Availability: The probability that a system is operational at a given time. Availability can be calculated as the ratio of the mean time between failures (MTBF) to the sum of the MTBF and the mean time to repair (MTTR).
- Reliability: The probability that a system performs its intended function correctly for a given period of time. Reliability can be calculated as the exponential function of the negative product of the failure rate and the time period.
- Mean time to failure (MTTF): The expected time until the first failure of a system. MTTF can be calculated as the inverse of the failure rate.