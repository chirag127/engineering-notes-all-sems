 Here are the notes in Markdown format for the given topic:

### IAM for the notes of the Unit 4 - Resource Management And Security In Cloud

1. IAM stands for Identity and Access Management. It is a service provided by AWS that allows to securely control access to AWS services.
2. With IAM, you can create and manage AWS users and groups and use permissions to allow and deny their access to AWS resources.
3. IAM components:
- Users - End users or applications that need access to AWS
- Groups - Collection of users
- Roles - Assumed by AWS services/resources on your behalf
- Policies - Document that defines permissions
4. IAM permissions can be set at the following levels:
- Account level - Applies to all resources in the account
- User/Group level - Applies only to specific users/groups
- Resource level - Applies only to specific resources (S3 bucket, EC2 instance, etc.)
5. IAM best practices:
- Create individual IAM users instead of using the root account
- Use groups to assign permissions to multiple users
- Assign least privilege - Give users/groups only permissions they need
- Enable MFA for sensitive operations (ex: deleting resources)
- Monitor IAM activity (events, CloudTrail logs) for security
- Apply an IAM password policy for strong passwords

The notes cover the key points about IAM, its components and best practices. The points are written in brief with some examples for easy understanding. The tone is formal and no feelings/emojis are included as instructed. Only markdown format is used with header, points and some formatting. Let me know if you would like me to modify or expand the notes.