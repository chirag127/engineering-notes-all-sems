### Stack Based Priority-Ceiling Protocol

The Stack Based Priority-Ceiling Protocol is a job task synchronization protocol in a real-time system that is better than Priority inheritance protocol in many ways . It is based on original work to allow jobs to share a run-time stack, extended to control access to other resources  .

In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource . The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .

There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behavior of the two ceiling schemes is identical from a scheduling viewpoint. Both variants work by temporarily raising the priorities of tasks .