### Weighted Round Robin Approach

- Weighted round robin (WRR) is a scheduling algorithm for tasks or data flows that generalizes the round robin algorithm by assigning different weights to different tasks or queues.
- WRR is a preemptive algorithm that can be used for scheduling real-time traffic in high-speed switched networks or for scheduling processes in a CPU .
- WRR approximates the generalized processor sharing (GPS) algorithm in a less computationally intensive way than weighted fair queueing (WFQ) by transmitting an amount of packets or executing an amount of instructions proportional to the weight of each task or queue in every round.
- WRR retains the advantage of round robin in eliminating starvation and also integrates priority scheduling by giving higher weights to higher priority tasks or queues.
- WRR is designed for maximum throughput in most scenarios, but it may increase the waiting time and response time for longer or heavier tasks or queues as they have to wait for their turn in every round.
- WRR can be implemented using several techniques, such as static or dynamic weights, deficit counters, or virtual clock.