### YA TRAP

- YA TRAP is a reader/tag authentication protocol for RFID systems .
- It aims to effectively authenticate tags and readers using hash functions and shared secrets .
- However, it may suffer from false authentications, which means that a legitimate tag could be wrongly rejected by a reader .
- False authentications may arise from the following reasons:
  - The tag may not be able to respond to the reader's challenge in time due to the limited power supply of passive RFID tags.
  - The tag may not be able to store the updated secret value after a successful authentication due to the unreliable memory of passive RFID tags.
  - The tag may not be able to synchronize with the reader's secret value due to the lossy communication channel of RFID systems.
- False authentications may lead to security and privacy risks, such as denial of service, impersonation, and tracking.
- To prevent false authentications, some countermeasures are proposed, such as:
  - Using a timer to measure the response time of the tag and adjust the threshold accordingly.
  - Using a backup memory to store the previous secret value and compare it with the current one.
  - Using a sequence number or a timestamp to ensure the freshness and consistency of the secret value.