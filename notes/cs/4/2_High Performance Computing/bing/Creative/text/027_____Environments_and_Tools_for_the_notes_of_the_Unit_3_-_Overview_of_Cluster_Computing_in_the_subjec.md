### Environments and Tools for Cluster Computing

- Cluster computing is a form of high performance distributed computing (HPDC) that uses a network of computers (called nodes) to execute parallel and/or distributed applications that require high computational power.
- A cluster computing software stack consists of the following components:
  - Workload managers or schedulers (such as Slurm, PBS, or IBM's LSF) to orchestrate job execution on the nodes.
  - Cluster configuration tools to provision and build clusters, such as:
    - Cluster management tools (such as Managed Instance Groups or Kubernetes) to orchestrate compute nodes and scale them up or down according to the workload demand.
    - DevOps tools (such as Terraform) to automate the creation and configuration of clusters and their resources.
  - End-user applications (such as OpenFOAM, GROMACS, WRF, or Jupyter Notebooks) to execute computations and view and analyze output.
- Cluster computing environments and tools can vary depending on the type and architecture of the cluster, such as:
  - Shared-memory clusters, where all the nodes share a common memory space and communicate via memory access.
  - Distributed-memory clusters, where each node has its own memory space and communicate via message passing.
  - Hybrid clusters, where both shared-memory and distributed-memory nodes are used.
- Some examples of cluster computing environments and tools are :
  - MPI (Message Passing Interface), a standard and widely used library for message passing communication among nodes.
  - OpenMP (Open Multi-Processing), a standard and widely used API for shared-memory parallel programming.
  - PVM (Parallel Virtual Machine), a software system that enables a collection of heterogeneous computers to be used as a single parallel computer.
  - gLite, a set of middleware technologies created by the Enabling Grids for E-sciencE (EGEE) project, which provides services for job submission, data management, security, and information discovery in grid computing environments.
  - Microsoft Windows Cluster Server 2003, a platform that provides pieces for high-performance computing such as the Job Scheduler, MSMPI library and management tools.