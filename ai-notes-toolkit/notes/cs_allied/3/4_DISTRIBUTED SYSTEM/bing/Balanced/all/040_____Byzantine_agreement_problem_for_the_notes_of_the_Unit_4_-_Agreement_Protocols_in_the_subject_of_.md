# Byzantine Agreement Problem

The Byzantine agreement problem is a fundamental problem in fault-tolerant distributed computing. It requires a set of parties in a distributed environment to agree on a value even if some of the parties are corrupted or faulty. The corrupted parties may behave arbitrarily, sending conflicting or misleading messages to different parties, or remaining silent. The problem is also known as the Byzantine generals problem, the interactive consistency problem, or the source congruency problem.

The problem was first defined and solved by Lamport et al. in 1982, using the analogy of several divisions of the Byzantine army camped outside an enemy city, each division commanded by its own general. The generals can communicate with one another only by messenger. After observing the enemy, they must decide upon a common plan of action, such as attack or retreat. However, some of the generals may be traitors, who try to prevent the loyal generals from reaching agreement. The problem is to find a protocol that allows the loyal generals to agree on the same plan, while tolerating a certain number of traitors.

Some of the main concepts and results related to the Byzantine agreement problem are:

- A protocol for Byzantine agreement is a set of rules that specify how the parties exchange messages and decide on a value, given their initial values and the messages they receive.
- A protocol is said to achieve Byzantine agreement if it satisfies the following properties:
  - **Termination**: Every loyal party eventually decides on a value.
  - **Agreement**: All loyal parties decide on the same value.
  - **Validity**: If all parties start with the same value, then all loyal parties decide on that value.
- A protocol is said to be **t-resilient** if it achieves Byzantine agreement even if up to t parties are corrupted.
- A protocol is said to be **synchronous** if it assumes that messages are delivered within a known bounded time, and parties have synchronized clocks. A protocol is said to be **asynchronous** if it makes no assumptions about message delivery time or clock synchronization.
- A protocol is said to be **authenticated** if it assumes that parties can verify the identity and authenticity of the messages they receive. A protocol is said to be **unauthenticated** if it makes no such assumptions.
- A fundamental result by Lamport et al. is that no protocol can achieve Byzantine agreement in a synchronous system with unauthenticated messages if t > n/3, where n is the number of parties and t is the number of corrupted parties. This is known as the **FLP impossibility** result.
- Another fundamental result by Pease et al. is that Byzantine agreement is possible in a synchronous system with authenticated messages if t < n/3. They also presented a protocol that achieves Byzantine agreement in this setting, using **quorums** of size at least 2t+1 and **signed messages**. This protocol requires O(n^2) messages and O(n) rounds of communication.
- Byzantine agreement is also possible in an asynchronous system with authenticated messages if t < n/3, using **randomization** or **cryptographic techniques**. However, these protocols are more complex and less efficient than the synchronous ones.
- Byzantine agreement is also possible in a synchronous or asynchronous system with unauthenticated messages if t < n/4, using **common coins** or **common randomness**. These are sources of randomness that are accessible and consistent for all parties, but unpredictable for the corrupted parties. However, these protocols also require additional assumptions and complexity.