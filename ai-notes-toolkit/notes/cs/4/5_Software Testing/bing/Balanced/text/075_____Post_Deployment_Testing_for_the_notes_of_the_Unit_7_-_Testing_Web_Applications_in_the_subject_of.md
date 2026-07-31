### Post Deployment Testing for the notes of the Unit 7 - Testing Web Applications in the subject of Software Testing

- Post deployment testing is a type of testing in which the software is tested after it is being deployed to production.
- The main objectives of post deployment testing are to verify the functionality, performance, security, usability, and compatibility of the software in the real environment.
- Post deployment testing activities include :
  - Post-deployment verification: Checking the software application against the test plans and test cases to ensure that the expected features and requirements are met.
  - User acceptance testing: Getting feedback from the end-users or stakeholders on the usability, functionality, and satisfaction of the software.
  - Performance testing: Measuring the response time, throughput, scalability, and reliability of the software under different workloads and conditions.
  - Security testing: Assessing the vulnerability, risk, and compliance of the software to prevent unauthorized access, data breaches, or malicious attacks.
  - Compatibility testing: Evaluating the interoperability of the software with different browsers, devices, platforms, or systems.
  - Monitoring: Collecting and analyzing the data on the software usage, performance, errors, or issues to identify and resolve any problems or defects.
- Post deployment testing strategies include :
  - Rolling update deployment: Updating a subset of running application instances instead of simultaneously updating every application instance. This reduces the risk of downtime and allows for testing and rollback if needed.
  - Blue-green deployment: Deploying the new version of the software to a separate environment (blue) while keeping the old version running in the original environment (green). This allows for testing the new version before switching the traffic to it and reverting to the old version if necessary.
  - Canary deployment: Releasing the new version of the software to a small percentage of users or servers before rolling it out to the rest. This allows for testing the impact and feedback of the new version and adjusting it accordingly.
  - Feature flags: Enabling or disabling certain features of the software for different users or groups. This allows for testing the functionality and usability of the features and gradually releasing them to the target audience.