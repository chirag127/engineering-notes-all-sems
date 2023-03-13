The following is a detailed ASCII diagram for Need for Models for the notes of the Unit 4 - Service-Oriented Analysis and Design in the subject of Service Oriented Architecture.

### Need for Models

Service-oriented modeling is a process that aims to create models that provide a comprehensive view of the analysis, design, and architecture of all software entities in an organization, which can be understood by individuals with diverse levels of business and technical understanding.

Service-oriented modeling requires additional activities and artifacts that are not found in traditional object-oriented analysis and design (OOAD), such as service identification, specification, realization, composition, and governance.

The following diagram illustrates the basic architecture of a service-oriented system, which consists of three layers: the business layer, the service layer, and the technology layer.

+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business Layer |     |  Service Layer  |     | Technology Layer|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business Goals |     |  Service Goals  |     |  Technology Goals|
|  Business Rules |     |  Service Rules  |     |  Technology Rules|
|  Business Logic |     |  Service Logic  |     |  Technology Logic|
|  Business Data  |     |  Service Data   |     |  Technology Data |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business       |     |  Service        |     |  Technology     |
|  Processes      |     |  Contracts      |     |  Components     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business       |     |  Service        |     |  Technology     |
|  Services       |     |  Interfaces     |     |  Interfaces     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Business       |     |  Service        |     |  Technology     |
|  Models         |     |  Models         |     |  Models         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+

The business layer defines the business goals, rules, logic, data, processes, and services that are relevant to the organization. The business models capture the business requirements and expectations for the system.

The service layer defines the service goals, rules, logic, data, contracts, and interfaces that are exposed to the consumers and providers of the system. The service models capture the service specifications and behaviors for the system.

The technology layer defines the technology goals, rules, logic, data, components, and interfaces that are used to implement and support the system. The technology models capture the technology configurations and capabilities for the system.

The models in each layer are aligned and consistent with each other, and they are governed by the principles and policies of service-orientation. The models in each layer are also refined and validated through various techniques, such as use cases, scenarios, prototypes, and testing.

Service-oriented modeling helps to ensure that the system is designed and built according to the business needs and expectations, and that it is flexible and adaptable to changing requirements and environments. Service-oriented modeling also helps to communicate and collaborate with different stakeholders, such as business analysts, service designers, service developers, service consumers, and service providers.