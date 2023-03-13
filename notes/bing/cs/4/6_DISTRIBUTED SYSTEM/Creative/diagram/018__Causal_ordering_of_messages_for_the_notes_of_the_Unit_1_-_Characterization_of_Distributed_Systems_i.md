Causal ordering of messages is a partial ordering of messages in a distributed computing environment. It places a restriction on communication between processes by requiring that if the transmission of message mi to process pk necessarily preceded the transmission of message mj to the same process, then the delivery of these messages to that process must be ordered such that mi is delivered before mj .

The following diagram illustrates the basic architecture of a distributed system with causal ordering of messages. It shows four processes (P1, P2, P3, P4) that communicate with each other by sending and receiving messages. The arrows represent the messages and their direction. The numbers on the arrows indicate the logical timestamps of the messages, which are used to enforce the causal ordering. The dashed lines represent the potential causal dependencies between messages. For example, m1 -> m2 means that m1 causally precedes m2, and m2 -> m3 means that m2 causally precedes m3. Therefore, m1 -> m3 is also true by transitivity. However, m1 and m4 are causally independent, as they are sent by different processes and do not depend on each other.

```
    P1          P2          P3          P4
    |           |           |           |
    |---m1(1)-->|           |           |
    |           |           |           |
    |           |---m2(2)-->|           |
    |           |           |           |
    |           |           |---m3(3)-->|
    |           |           |           |
    |           |           |<--m4(4)---|
    |           |           |           |
    |           |<--m5(5)---|           |
    |           |           |           |
    |<--m6(6)---|           |           |
    |           |           |           |
    |           |           |---m7(7)-->|
    |           |           |           |
    |           |           |<--m8(8)---|
    |           |           |           |
    |           |           |---m9(9)-->|
    |           |           |           |
    |           |           |<--m10(10)-|
    |           |           |           |
    |           |           |---m11(11)->|
    |           |           |           |
    |           |           |<--m12(12)-|
    |           |           |           |
    |           |           |---m13(13)->|
    |           |           |           |
    |           |           |<--m14(14)-|
    |           |           |           |
    |           |           |---m15(15)->|
    |           |           |           |
    |           |           |<--m16(16)-|
    |           |           |           |
    |           |           |---m17(17)->|
    |           |           |           |
    |           |           |<--m18(18)-|
    |           |           |           |
    |           |           |---m19(19)->|
    |           |           |           |
    |           |           |<--m20(20)-|
    |           |           |           |
    |           |           |---m21(21)->|
    |           |           |           |
    |           |           |<--m22(22)-|
    |           |           |           |
    |           |           |---m23(23)->|
    |           |           |           |
    |           |           |<--m24(24)-|
    |           |           |           |
    |           |           |---m25(25)->|
    |           |           |           |
    |           |           |<--m26(26)-|
    |           |           |           |
    |           |           |---m27(27)->|
    |           |           |           |
    |           |           |<--m28(28)-|
    |           |           |           |
    |           |           |---m29(29)->|
    |           |           |           |
    |           |           |<--m30(30)-|
    |           |           |           |
    |           |           |---m31(31)->|
    |           |           |           |
    |           |           |<--m32(32)-|