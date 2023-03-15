# Deployment

Deployment is the process of installing, configuring, and running a software system on a target platform. Deployment can be done manually or automatically, depending on the complexity and scale of the system. Deployment can also involve testing, monitoring, and updating the system as needed.

Some of the topics covered in this unit are:

- Deployment diagrams
- Deployment units
- Deployment configurations
- Deployment strategies
- Deployment tools

## Deployment diagrams

A deployment diagram is a type of UML diagram that shows the physical arrangement and distribution of the components of a software system across different nodes. A node is a physical or virtual device that can execute software, such as a server, a workstation, a mobile device, or a cloud platform. A deployment diagram can also show the communication links and protocols between the nodes, as well as the properties and constraints of the nodes and components.

A deployment diagram consists of the following elements:

- Nodes: represented by cubes with optional stereotypes, such as <<device>>, <<executionEnvironment>>, or <<cloud>>. Nodes can be nested to show hierarchical or composite structures.
- Components: represented by rectangles with optional stereotypes, such as <<artifact>>, <<executable>>, or <<database>>. Components can be nested to show hierarchical or composite structures. Components can also have ports and interfaces to show their provided and required services.
- Links: represented by solid or dashed lines with optional stereotypes, such as <<TCP>>, <<HTTP>>, or <<wireless>>. Links can show the physical or logical connections between nodes or components. Links can also have multiplicity and constraints to show the number and conditions of the connections.
- Dependencies: represented by dashed arrows with optional stereotypes, such as <<deploy>>, <<use>>, or <<call>>. Dependencies can show the relationships and interactions between nodes or components, such as deployment, usage, or invocation.

An example of a deployment diagram for a web application is shown below:

```markdown
+------------------+       +------------------+
| <<device>>       |       | <<device>>       |
| Web Server       |       | Database Server  |
| +--------------+ |       | +--------------+ |
| | <<artifact>> | |       | | <<artifact>> | |
| | WebApp.war   | |       | | DBMS.exe     | |
| +--------------+ |       | +--------------+ |
| +--------------+ |       | +--------------+ |
| | <<artifact>> | |       | | <<artifact>> | |
| | WebApp.jar   | |       | | Database.db  | |
| +--------------+ |       | +--------------+ |
+------------------+       +------------------+
       |  <<HTTP>> |       | <<TCP>> |
       +-----------+-------+---------+
```

## Deployment units

A deployment unit is a package of one or more components that can be deployed as a single entity on a node. A deployment unit can be an executable file, a library, a configuration file, a database, or any other type of software artifact. A deployment unit can have dependencies on other deployment units, such as libraries, frameworks, or services. A deployment unit can also have properties and constraints, such as version, size, or compatibility.

A deployment unit can be represented by a component with the stereotype <<artifact>> in a deployment diagram. An example of a deployment unit for a web application is shown below:

```markdown
+------------------+
| <<artifact>>     |
| WebApp.war       |
| +--------------+ |
| | <<artifact>> | |
| | WebApp.jar   | |
| +--------------+ |
+------------------+
```

## Deployment configurations

A deployment configuration is a specific arrangement and distribution of deployment units across different nodes. A deployment configuration can vary depending on the requirements and constraints of the system, such as performance, scalability, availability, security, or cost. A deployment configuration can also change over time, due to updates, upgrades, or migrations.

A deployment configuration can be represented by a deployment diagram with specific instances of nodes and components. An example of a deployment configuration for a web application is shown below:

```markdown
+------------------+       +------------------+
| <<device>>       |       | <<device>>       |
| WebServer1       |       | DatabaseServer1  |
| +--------------+ |       | +--------------+ |
| | <<artifact>> | |       | | <<artifact>> | |
| | WebApp.war   | |       | | DBMS.exe     | |
| +--------------+ |       | +--------------+ |
| +--------------+ |       | +--------------+ |
| | <<artifact>> | |       | | <<artifact>> | |
| | WebApp.jar   | |       | | Database.db  | |
| +--------------+ |