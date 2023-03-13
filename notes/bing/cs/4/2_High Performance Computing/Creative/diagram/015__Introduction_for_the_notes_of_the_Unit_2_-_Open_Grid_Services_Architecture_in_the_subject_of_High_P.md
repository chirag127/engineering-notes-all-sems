### Introduction

The Open Grid Services Architecture (OGSA) is a service-oriented architecture for a grid computing environment for business and scientific use. It was developed within the Open Grid Forum, which was called the Global Grid Forum (GGF) at the time, around 2002 to 2006.

OGSA defines a set of core capabilities and behaviors that address key concerns in grid systems, such as resource discovery, management, security, and interoperability. OGSA uses most of Web service technologies, notably WSDL and SOAP, but it aims to be largely agnostic in relation to the transport-level handling of data upon the grid.

The following diagram illustrates the basic architecture of a grid system based on OGSA:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Grid Service   |        |  Grid Service   |        |  Grid Service   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service Data   |        |  Service Data   |        |  Service Data   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service Logic  |        |  Service Logic  |        |  Service Logic  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service Handle |        |  Service Handle |        |  Service Handle |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service Type   |        |  Service Type   |        |  Service Type   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service Name   |        |  Service Name   |        |  Service Name   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service ID     |        |  Service ID     |        |  Service ID     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Service        |        |  Service        |        |  Service        |
|  Implementation |        |  Implementation |        |  Implementation |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource       |        |  Resource       |        |  Resource       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource       |        |  Resource       |        |  Resource       |
|  Implementation |        |  Implementation |        |  Implementation |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource       |        |  Resource       |        |  Resource       |
|  Type           |        |  Type           |        |  Type           |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource Name  |        |  Resource Name  |        |  Resource Name  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource ID    |        |  Resource ID    |        |  Resource ID    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Resource       |        |  Resource       |