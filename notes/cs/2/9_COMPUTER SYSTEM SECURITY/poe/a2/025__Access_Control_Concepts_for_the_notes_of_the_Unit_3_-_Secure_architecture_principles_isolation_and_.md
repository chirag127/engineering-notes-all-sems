 Here are the notes on Access Control Concepts for Unit 3 - Secure architecture principles isolation and least privilege in COMPUTER SYSTEM SECURITY:

### Access Control Concepts

- Discretionary Access Control (DAC): Access is based on identity of the user and the permissions associated with the user's access token (e.g. DAC in Linux). Permissions can be granted or revoked by the owner of an object.
- Mandatory Access Control (MAC): Access is based on the security level/clearance of the user and the sensitivity label of the object/resource. Enforces a strict access policy based on security labels (e.g. MAC in SELinux).
- Role-Based Access Control (RBAC): Access is based on the role of the user in an organization. Users are assigned roles and roles are assigned permissions. Users acquire permissions through their roles (e.g. RBAC in AWS IAM).
- Attribute-Based Access Control (ABAC): Access is based on user attributes, resource attributes and the environment. Policies are defined based on these attributes to control access (e.g. XACML is an ABAC standard).

Notes:
- Be formal and objective.
- Write in points.
- Avoid emojis, external links and feelings.
- Use markdown format.