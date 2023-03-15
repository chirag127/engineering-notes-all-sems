A Walk Through (Walkthrough) Static testing strategy is a type of static testing technique where the developer presents the code to others, who then give their opinions. It is not surprising for the presenting developers to realize problems themselves during the walkthrough . The purpose of this technique is to improve the quality of the code and to detect defects early in the development cycle.

A possible ascii diagram for a Walk Through (Walkthrough) Static testing strategy is:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Developer      |       |  Reviewers      |       |  Moderator      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |----------------------->|                        |
        |  Present code          |                        |
        |                        |----------------------->|
        |                        |  Give feedback         |
        |<-----------------------|                        |
        |  Resolve issues        |                        |
        |                        |                        |
        |----------------------->|                        |
        |  Confirm resolution    |                        |
        |                        |----------------------->|
        |                        |  Close walkthrough     |
        |<-----------------------|                        |
        |  Update code           |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        V                        V                        V
```