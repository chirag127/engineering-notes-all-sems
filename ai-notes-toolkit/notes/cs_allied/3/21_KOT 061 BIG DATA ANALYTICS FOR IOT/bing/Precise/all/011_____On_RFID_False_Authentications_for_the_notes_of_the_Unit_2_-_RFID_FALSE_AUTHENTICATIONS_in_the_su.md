# On RFID False Authentications

- RFID technology has been used in real applications such as supply chain management, in which RFID tags are attached to products so that they can be conveniently identified by tag readers .
- Many reader/tag authentication protocols are proposed to effectively authenticate tags and readers .
- However, false authentications that a legitimate tag could be wrongly rejected by a reader may arise from these protocols when they are applied to C1G2 (class 1 generation 2) passive RFID tags .
- YA-TRAP is an example of how false authentications may arise from these protocols .
- A protocol pattern has been identified, of which the implementation on C1G2 passive tags leads to false authentications .
- A naiveSemaphore-based solution has been proposed which revises the pattern by adding semaphore operations so as to avoid false authentications .
