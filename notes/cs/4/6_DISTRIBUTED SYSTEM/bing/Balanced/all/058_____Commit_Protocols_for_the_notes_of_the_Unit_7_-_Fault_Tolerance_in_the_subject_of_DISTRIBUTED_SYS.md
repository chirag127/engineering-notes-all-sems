# Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures  .
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, each with its own advantages and disadvantages    .

## One-phase commit protocol
- A one-phase commit protocol involves a coordinator site that initiates a transaction and communicates with the participant sites that execute the transaction on behalf of the coordinator .
- The coordinator site sends a commit request to all the participant sites and waits for their replies .
- If all the participant sites reply with an OK message, the coordinator site commits the transaction and sends a commit message to all the participant sites .
- If any of the participant sites reply with an abort message, the coordinator site aborts the transaction and sends an abort message to all the participant sites .
- The advantages of this protocol are simplicity and efficiency, as it requires only one round of message exchange between the coordinator and the participants .
- The disadvantages of this protocol are lack of fault tolerance and concurrency control, as it does not handle the cases where the coordinator or the participants fail or the network partitions .

## Two-phase commit protocol
- A two-phase commit protocol is an extension of the one-phase commit protocol that adds a voting phase to improve the fault tolerance and concurrency control    .
- The protocol consists of two phases: the prepare phase and the commit phase    .
- In the prepare phase, the coordinator site sends a prepare request to all the participant sites and waits for their votes    .
- The participant sites execute the transaction and write a log record of their actions, then reply with a yes vote if they are ready to commit or a no vote if they want to abort    .
- In the commit phase, the coordinator site decides whether to commit or abort the transaction based on the votes received from the participant sites    .
- If all the participant sites vote yes, the coordinator site commits the transaction and sends a commit message to all the participant sites    .
- If any of the participant sites vote no, the coordinator site aborts the transaction and sends an abort message to all the participant sites    .
- The participant sites follow the decision of the coordinator site and commit or abort the transaction accordingly    .
- The advantages of this protocol are fault tolerance and concurrency control, as it handles the cases where the coordinator or the participants fail or the network partitions by using timeouts, recovery procedures, and locking mechanisms    .
- The disadvantages of this protocol are blocking and performance overhead, as it requires two rounds of message exchange between the coordinator and the participants and may block the participants in the commit phase until the coordinator recovers or the network reconnects    .

## Three-phase commit protocol
- A three-phase commit protocol is an extension of the two-phase commit