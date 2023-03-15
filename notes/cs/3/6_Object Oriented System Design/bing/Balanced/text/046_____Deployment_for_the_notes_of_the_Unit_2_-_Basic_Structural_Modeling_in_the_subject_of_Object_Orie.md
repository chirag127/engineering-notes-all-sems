### Deployment

- Deployment is the process of distributing software components to the nodes of a system, where they can be executed and accessed by other components or users.
- Deployment diagrams are used to model the physical aspects of a system, such as the hardware, the network, the operating system, and the middleware.
- Deployment diagrams show the allocation of software components to nodes, the communication links between nodes, and the properties of nodes and components.
- Deployment diagrams can be used to:
  - Visualize the distribution of software components across a system.
  - Analyze the performance, scalability, reliability, and security of a system.
  - Plan the installation and configuration of a system.
- The main elements of a deployment diagram are:
  - Node: A physical or virtual machine that hosts one or more components. Nodes can be nested to represent complex structures, such as clusters, racks, or clouds. Nodes can have stereotypes to indicate their type, such as <<device>>, <<server>>, or <<database>>.
  - Component: A modular unit of software that provides a well-defined functionality or service. Components can be deployed to nodes, and can communicate with other components through interfaces and ports. Components can have stereotypes to indicate their type, such as <<executable>>, <<library>>, or <<web>>.
  - Artifact: A physical piece of information that is used or produced by a component, such as a file, a document, or a database. Artifacts can be deployed to nodes, and can be associated with components to show their usage or dependency. Artifacts can have stereotypes to indicate their type, such as <<script>>, <<image>>, or <<table>>.
  - Deployment specification: A set of parameters or properties that define how a component or artifact is deployed to a node, such as the location, the configuration, or the version. Deployment specifications can be attached to deployment relationships to show the details of the deployment.
  - Deployment: A relationship that shows the allocation of a component or artifact to a node. Deployment relationships can have stereotypes to indicate their type, such as <<deploy>>, <<install>>, or <<copy>>.
  - Communication path: A relationship that shows the connection between two nodes, and the possible communication between the components or artifacts deployed on them. Communication paths can have stereotypes to indicate their type, such as <<LAN>>, <<WAN>>, or <<HTTP>>.