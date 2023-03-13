Code inspection is a type of static testing which aims in reviewing the software code and examining for any errors in that. It helps in reducing the ratio of defect multiplication and avoids later-stage error detection by simplifying all the initial error detection processes.

The following diagram illustrates the basic architecture of a code inspection process using ASCII art:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Developer    |----->|   Moderator    |----->|   Reviewers    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Code Review  |<-----|   Code Review  |<-----|   Code Review  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Code Fix     |----->|   Code Fix     |----->|   Code Fix     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The code inspection process involves the following steps:

- The developer writes the code and submits it to the moderator for review.
- The moderator checks the code for compliance with the coding standards and guidelines, and assigns reviewers for further inspection.
- The reviewers examine the code for any logical, syntactical, or functional errors, and report their findings to the moderator.
- The moderator consolidates the feedback from the reviewers and sends it back to the developer.
- The developer fixes the code based on the feedback and resubmits it to the moderator for verification.
- The moderator verifies that the code is free of errors and approves it for deployment.