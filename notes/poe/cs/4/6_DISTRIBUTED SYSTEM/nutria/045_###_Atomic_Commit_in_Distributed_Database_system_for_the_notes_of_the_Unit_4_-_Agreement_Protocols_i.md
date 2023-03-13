
### Atomic Commit in Distributed Database System for the Notes of the Unit 4 - Agreement Protocols in the Subject of DISTRIBUTED SYSTEM

Atomic Commit is an agreement protocol used in distributed database systems. It is used to ensure that all transactions in a distributed system are either completely committed or completely aborted. In order to achieve this, the protocol uses two-phase commit and three-phase commit. 

#### Two-Phase Commit

Two-phase commit is a process in which all the participants in a distributed system agree to a single outcome. The process is divided into two phases: 

1. **Prepare**: In this phase, all the participants in the system agree to a single outcome. 

2. **Commit**: In this phase, all the participants in the system commit to the outcome agreed upon in the first phase. 

The two-phase commit protocol ensures that all the participants in the system agree to the same outcome, and that the outcome is committed to the database.

#### Three-Phase Commit

Three-phase commit is an extension of two-phase commit. It is used in distributed systems where there are multiple participants and multiple databases. The process is divided into three phases:

1. **Prepare**: In this phase, all the participants in the system agree to a single outcome. 

2. **Agree**: In this phase, all the participants in the system agree to the outcome agreed upon in the first phase. 

3. **Commit**: In this phase, all the participants in the system commit to the outcome agreed upon in the first two phases. 

The three-phase commit protocol ensures that all the participants in the system agree to the same outcome, and that the outcome is committed to all the databases in the system.

Atomic Commit is an important agreement protocol used in distributed database systems. It ensures that all transactions in a distributed system are either completely committed or completely aborted. The protocol uses two-phase commit and three-phase commit to achieve this.