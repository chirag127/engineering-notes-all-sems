Formal Technical Reviews (Peer Reviews) are a type of static testing technique that involves a structured and documented examination of software artifacts by a team of technical experts. The purpose of this technique is to identify and eliminate defects, improve quality, and ensure compliance with standards and specifications. The main steps of a Formal Technical Review are:

- Planning: The moderator selects the review team, schedules the meeting, and distributes the documents to be reviewed.
- Preparation: The reviewers study the documents and identify potential defects, issues, and questions.
- Review Meeting: The moderator leads the discussion, the author clarifies the doubts, the scribe records the defects, and the reviewers provide feedback and suggestions.
- Rework: The author fixes the defects and updates the documents based on the review comments.
- Follow-up: The moderator checks the rework, verifies the defect resolution, and closes the review.

The following diagram illustrates the basic architecture of a Formal Technical Review using ASCII characters:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Planning    +----->+   Preparation  +----->+ Review Meeting |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
                                                        |
                                                        |
                                                        v
                                                +----------------+
                                                |                |
                                                |     Rework    |
                                                |                |
                                                +----------------+
                                                        |
                                                        |
                                                        v
                                                +----------------+
                                                |                |
                                                |   Follow-up   |
                                                |                |
                                                +----------------+
```