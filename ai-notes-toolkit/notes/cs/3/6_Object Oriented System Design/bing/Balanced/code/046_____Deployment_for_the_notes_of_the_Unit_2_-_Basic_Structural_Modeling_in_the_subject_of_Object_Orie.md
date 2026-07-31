### Deployment

- Deployment is the process of distributing the system components to the nodes in the physical architecture of the system.
- Deployment diagrams are used to model the static deployment view of a system. They show the configuration of the hardware elements (nodes) and the software components, processes and objects that are assigned to them.
- Deployment diagrams are related to component diagrams because they are used to deploy the components from component diagrams.
- Deployment diagrams can also show the communication paths between the nodes, which can be modeled as associations with stereotypes such as <<LAN>>, <<WAN>>, <<TCP/IP>>, etc.
- The main elements of a deployment diagram are:
  - Node: A physical element that can contain one or more components, processes or objects. It can be a device, a server, a workstation, etc. Nodes are depicted as cubes with optional compartments for components, processes or objects.
  - Component: A modular part of a system that encapsulates its behavior and data, and exposes interfaces for communication. It can be a binary file, a library, a database, etc. Components are depicted as rectangles with two small rectangles on the left side.
  - Process: A running instance of a component or a program. It can be a thread, a daemon, a service, etc. Processes are depicted as rectangles with the stereotype <<process>>.
  - Object: A runtime instance of a class or a component. It can be an entity, a boundary, a control, etc. Objects are depicted as rectangles with the stereotype <<object>> and an optional class or component name.
  - Artifact: A physical piece of information that is used or produced by the system. It can be a file, a document, a report, etc. Artifacts are depicted as rectangles with the stereotype <<artifact>> and an optional file name.
  - Manifestation: A dependency relationship that shows how an artifact is deployed on a node, component, process or object. It is depicted as a dashed line with the stereotype <<manifest>> and an optional name.
  - Deployment specification: A specification of the properties and parameters of a node, component, process or object that affect its deployment. It can be a configuration file, a script, a command line, etc. Deployment specifications are depicted as rectangles with the stereotype <<deploy>> and an optional name. They are attached to the elements they specify by a dashed line.

- An example of a deployment diagram for a web application is shown below:

```markdown
+-----------------+      +-----------------+      +-----------------+
| Web Server      |      | Application     |      | Database Server |
| <<node>>        |      | Server          |      | <<node>>        |
|                 |      | <<node>>        |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | index.html  | |      | | WebApp.jar  | |      | | WebDB.db   | |
| | <<artifact>>| |      | | <<artifact>>| |      | | <<artifact>>| |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      |                 |
| | WebServer   | |      | | WebApp      | |      |                 |
| | <<process>> | |      | | <<process>> | |      |                 |
| +-------------+ |      | +-------------+ |      |                 |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      |                 |
| | WebServer   | |      | | WebApp      | |      |                 |
| | <<component>>| |      | | <<component>>| |      |                 |
| +-------------+ |      | +-------------+ |      |                 |
+-----------------+      +-----------------+      +-----------------+
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
       |                        |                        |
       |<<LAN>>                 |<<LAN>>                 |<<LAN>>
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |

```
