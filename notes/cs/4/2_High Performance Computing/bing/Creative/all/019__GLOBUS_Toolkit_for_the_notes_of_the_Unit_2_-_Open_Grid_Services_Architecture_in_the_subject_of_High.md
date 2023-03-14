### GLOBUS Toolkit for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- GLOBUS Toolkit is an open-source toolkit for grid computing developed and provided by the Globus Alliance.
- Grid computing is a distributed computing paradigm that enables the sharing of heterogeneous resources across multiple administrative domains.
- GLOBUS Toolkit provides a set of libraries and programs that help developers of specific tools or applications with solutions for common problems that are encountered when creating a distributed system services and applications.
- GLOBUS Toolkit adheres to or provides implementations of the following standards:
  - Open Grid Services Architecture (OGSA): a service-oriented architecture for grid computing that defines a set of standard interfaces and behaviors for grid services.
  - Open Grid Services Infrastructure (OGSI): a specification that defines the basic "plumbing" layer for OGSA, but has been superseded by WSRF and WS-Management.
  - Web Services Resource Framework (WSRF): a set of specifications that define how to model and access stateful resources using web services.
  - Job Submission Description Language (JSDL): a standard XML format for describing the requirements and characteristics of computational jobs to be executed on a grid.
  - Distributed Resource Management Application API (DRMAA): a standard API for submitting, monitoring, and controlling jobs on distributed resource management systems.
  - WS-Management: a web services protocol for managing IT resources such as servers, devices, applications, and services.
  - WS-BaseNotification: a web services specification that defines a publish/subscribe mechanism for event notification.
  - SOAP: a protocol for exchanging structured information in a decentralized and distributed environment.
  - Web Services Description Language (WSDL): a standard XML format for describing the functionality and interface of web services.
  - Grid Security Infrastructure (GSI): a component of GLOBUS Toolkit that provides authentication, authorization, and encryption mechanisms for grid services and applications.
- GLOBUS Toolkit consists of several components that can be grouped into four categories:
  - Security: GSI, MyProxy, GridShib, CAS, GAMA, etc.
  - Data Management: GridFTP, RFT, RLS, DRS, etc.
  - Execution Management: GRAM, WS-GRAM, C, Java, and Python CoG, etc.
  - Information Services: MDS, WS-MDS, Index Service, Trigger Service, etc.
- GLOBUS Toolkit is compatible with various third-party software, such as job schedulers, resource brokers, workflow systems, portals, etc.
- GLOBUS Toolkit has been used for various scientific and engineering applications, such as astronomy, bioinformatics, climate modeling, earthquake simulation, etc.
- GLOBUS Toolkit is no longer available as a do-it-yourself distributed computing toolkit, but its spirit lives on in a mature, full-featured and easy to use service for research data management – Globus.org.
- GLOBUS Toolkit has been forked by the Grid Community Forum (GridCF) and renamed as the Grid Community Toolkit (GCT), which continues to maintain and develop the code base.

A possible mnemonic to remember the four categories of GLOBUS Toolkit components is:

**S**ecurity, **D**ata, **E**xecution, **I**nformation -> **SDEI** -> **S**ounds like **SDI** (Strategic Defense Initiative)

A possible learning trick to understand the difference between OGSA and OGSI is:

**OGSA** defines **A**rchitecture, **OGSI** defines **I**nfrastructure -> **A** comes before **I** in the alphabet, **A**rchitecture comes before **I**nfrastructure in the design process.