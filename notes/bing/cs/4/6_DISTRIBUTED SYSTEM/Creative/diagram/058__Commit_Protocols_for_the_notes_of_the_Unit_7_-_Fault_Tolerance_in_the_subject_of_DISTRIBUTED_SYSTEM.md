Commit protocols are algorithms that ensure the atomicity of transactions in a distributed system, meaning that either all the sites involved in a transaction agree to commit or abort it, even in the presence of failures. There are different types of commit protocols, such as one-phase, two-phase, and three-phase commit protocols, each with its own advantages and disadvantages.

The following is a detailed ASCII diagram of the two-phase commit protocol, which is a widely accepted standard protocol for distributed transactions. It consists of two phases: the voting phase and the commit phase. In the voting phase, a coordinator site sends a prepare message to all the participant sites, asking them to vote on whether they are ready to commit or abort the transaction. The participant sites reply with either a yes or a no vote, depending on their local state. In the commit phase, the coordinator site decides whether to commit or abort the transaction based on the votes received. If all the votes are yes, the coordinator sends a commit message to all the participants, instructing them to commit the transaction. If any of the votes are no, or if the coordinator does not receive a vote from a participant within a timeout period, the coordinator sends an abort message to all the participants, instructing them to abort the transaction. The participant sites then acknowledge the coordinator's decision by sending an ack message.

```
+------------+     prepare     +------------+
| Coordinator|---------------->| Participant|
+------------+                 +------------+
      |                            |
      |<---------------------------| yes/no
      |                            |
      |     commit/abort          |
      |-------------------------->|
      |                            |
      |<---------------------------| ack
      |                            |
```

The following is a detailed ASCII diagram of the three-phase commit protocol, which is an extension of the two-phase commit protocol that aims to overcome the blocking problem. The blocking problem occurs when the coordinator site fails after sending a prepare message, leaving the participant sites in an uncertain state, waiting for the coordinator's decision. The three-phase commit protocol adds an extra phase called the pre-commit phase, which makes the protocol non-blocking, but also increases the number of messages exchanged. In the pre-commit phase, the coordinator site sends a pre-commit message to all the participant sites that voted yes in the voting phase, indicating that the transaction will be committed. The participant sites reply with an ack message, and enter a prepared state, where they are ready to commit the transaction. In the commit phase, the coordinator site sends a commit message to all the participant sites in the prepared state, instructing them to commit the transaction. The participant sites then acknowledge the coordinator's decision by sending an ack message. If the coordinator site fails before sending a pre-commit message, or if any of the participant sites vote no in the voting phase, the coordinator sends an abort message to all the participants, instructing them to abort the transaction. The participant sites then acknowledge the coordinator's decision by sending an ack message.

```
+------------+     prepare     +------------+
| Coordinator|---------------->| Participant|
+------------+                 +------------+
      |                            |
      |<---------------------------| yes/no
      |                            |
      |     pre-commit/abort      |
      |-------------------------->|
      |                            |
      |<---------------------------| ack
      |                            |
      |     commit/abort          |
      |-------------------------->|
      |                            |
      |<---------------------------| ack
      |                            |
```

I hope this helps you understand the commit protocols in distributed systems. If you have any questions, please let me know.😊