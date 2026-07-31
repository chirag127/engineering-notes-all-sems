 Here are the notes on Authentication/Authorization for Smart Devices for the Unit 1 - INTRODUCTION: SECURING THE INTERNET OF THINGS:

### Authentication/Authorization for Smart Devices

- Authentication is the process of verifying the identity of a user or device. It ensures that only legitimate entities can access the system.
- Authorization determines what level of access an authenticated entity should have. It specifies what resources an entity can access and what operations it can perform on those resources.
- For smart devices with limited computational power and memory, lightweight authentication and authorization schemes are required. Some options include:

--Pre-shared keys: Devices are provisioned with secret keys that are used to authenticate the device. Scalability and key management are challenges.
-- certificates: X.509 certificates can be used but certificate revocation is challenging with constrained devices.
--Biometrics: Biometric authentication like fingerprint, iris scan, etc. can be used but may not be practical for all types of devices. They also suffer from scalability issues.
--One-time passwords: Passwords that are only valid for one login session can be used but time synchronization challenges exist.

- For authorization, attribute-based access control systems can be used where permissions are assigned based on attributes of the device like location, owner, type, etc. Instead of checking permissions for each resource, a policy decision point can evaluate attributes and determine appropriate access. However, more complex policies may be difficult to evaluate on constrained devices.
- Balancing security and performance is crucial for authentication and authorization on smart devices due to their resource constraints. Lightweight and scalable schemes must be designed while still providing adequate security.