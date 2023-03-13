The following is a possible diagram for the design of activity services (or business services) for the notes of the Unit 4 - Service-Oriented Analysis and Design in the subject of Service Oriented Architecture. The diagram is drawn using ASCII characters and follows the notation of UML activity diagrams. The diagram shows how a business service can be composed of several activity services that perform specific tasks and interact with each other through messages and data flows. The diagram also shows how the business service can be exposed to external consumers through a service contract and a service interface.

```
+---------------------+       +---------------------+
| Business Service    |       | External Consumer   |
|                     |       |                     |
| +-----------------+ |       | +-----------------+ |
| | Service Contract| |       | | Service Contract| |
| +-----------------+ |       | +-----------------+ |
|         |           |       |         |           |
|         v           |       |         v           |
| +-----------------+ |       | +-----------------+ |
| | Service Interface| |<---->| | Service Interface| |
| +-----------------+ |       | +-----------------+ |
|         |           |       |                     |
+---------------------+       +---------------------+
          |
          v
+---------------------+
| Activity Service 1  |
|                     |
| +-----------------+ |
| | Activity 1      | |
| +-----------------+ |
|         |           |
|         v           |
| +-----------------+ |
| | Activity 2      | |
| +-----------------+ |
|         |           |
+---------------------+
          |
          v
+---------------------+
| Activity Service 2  |
|                     |
| +-----------------+ |
| | Activity 3      | |
| +-----------------+ |
|         |           |
|         v           |
| +-----------------+ |
| | Activity 4      | |
| +-----------------+ |
|         |           |
+---------------------+
          |
          v
+---------------------+
| Activity Service 3  |
|                     |
| +-----------------+ |
| | Activity 5      | |
| +-----------------+ |
|         |           |
|         v           |
| +-----------------+ |
| | Activity 6      | |
| +-----------------+ |
|         |           |
+---------------------+
```