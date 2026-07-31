### Post Deployment Testing for the notes of the Unit 7 - Testing Web Applications in the subject of Software Testing

- Post deployment testing is a type of testing in which the software is tested after it is being deployed to production.
- The purpose of post deployment testing is to ensure that the software functions as intended in the real environment and meets the user expectations and requirements.
- Post deployment testing involves the following activities  :
  - Post-deployment verification: The QA or Test lead conducts the verification of the software application as per the need and its requirement and these are generally the test plans and the test cases of the software application which are compared from the previous or existing test plan and test cases.
  - Retesting the features: The features that were tested before deployment are retested in the production environment to check their functionality and performance.
  - Gathering user feedback: The feedback from the end-users or customers is collected and analyzed to identify any issues or defects in the software or to suggest any improvements or enhancements.
  - Monitoring the software: The software is monitored for its availability, reliability, security, scalability, and performance using various tools and metrics. Any anomalies or errors are reported and resolved as soon as possible.
  - Updating the software: The software is updated with any patches, fixes, or new features based on the feedback and monitoring results. The updates are tested and verified before deploying them to the production environment.
- Post deployment testing can be done using various strategies, such as:
  - Rolling update deployment: In this strategy, a subset of running application instances are updated instead of simultaneously updating every application instance. This allows for testing the updates in a controlled manner and minimizing the impact on the users.
  - Blue-green deployment: In this strategy, two identical environments are created, one for production (blue) and one for testing (green). The updates are deployed and tested in the green environment, and then the traffic is switched from the blue to the green environment. This allows for fast and reliable testing and deployment with minimal downtime.
  - Canary deployment: In this strategy, the updates are deployed and tested on a small percentage of users or servers before rolling them out to the entire production environment. This allows for testing the updates in a real environment and detecting any issues or bugs early.
- Post deployment testing is an essential part of the software development life cycle and the DevOps and agile methodologies. It helps to ensure the quality, reliability, and user satisfaction of the software  .