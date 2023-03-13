 Here is the content written in markdown format on the topic ### Congestion control algorithms in cn:

### Congestion control algorithms in cn

The following are the major congestion control algorithms used in computer networks:

1. **Slow start:** It is used by TCP. The sender starts with a low transmission rate and slowly increases it over time as long as there are no packet losses indicating congestion. The key goal is to slowly probe the network to determine the optimal transmission rate.
2. **Congestion avoidance:** It is used by TCP after slow start. The sender addsitively increases transmission rate but at a slower rate than slow start. This is to cautiously probe the network and avoid congestion.
3. **Fast retransmit:** When multiple duplicate ACKs are received, it indicates packet loss due to congestion. The sender then retransmits the lost packet without waiting for the timeout. This speeds up recovery from congestion.
4. **Fast recovery:** After fast retransmit sends the lost packet, the sender reduces its transmission rate to alleviate congestion. It then gradually increases the rate to determine if the reduction was sufficient. This avoids unnecessary throttling of the transmission rate.

**Mnemonics:**

- Slow start: Like cautiously starting a car, slowly increase speed.
- Congestion avoidance: Carefully driving to avoid accidents, slowly increase speed.
- Fast retransmit: Emergency braking when seeing warning signs of congestion.
- Fast recovery: Regaining speed cautiously after braking for congestion.

**Advantages:** These algorithms help in efficiently utilizing network bandwidth while avoiding and recovering from congestion. This improves throughput and reduces delay.
**Disadvantages:** The algorithms do not respond well to fluctuating network conditions and may lead to underutilization or congestion. Fine-tuning of parameters is required for good performance.
**Examples:** TCP implements all these algorithms.
**Applications:** Web traffic, file transfers, etc. use TCP and benefit from these algorithms.

[Detailed diagrams and examples can be added if required.]