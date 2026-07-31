# Service Oriented Architecture and Microservices Architecture

## Introduction

- Service Oriented Architecture (SOA) and Microservices Architecture (MSA) are two common service-based architectures that aim to improve the modularity, scalability, and maintainability of software applications.
- Both architectures rely on breaking down an application into multiple services that communicate through lightweight protocols, such as HTTP or messaging queues.
- However, there are some key differences between SOA and MSA in terms of the scope, granularity, and characteristics of the services.

## SOA Basics

- SOA is an enterprise-wide approach to software development that takes advantage of reusable software components, or services.
- In SOA, each service is comprised of the code and data integrations required to execute a specific business function, such as order processing, inventory management, or customer relationship management.
- Services are loosely coupled, meaning that they can be invoked independently of each other and can be changed or replaced without affecting the rest of the system.
- Services are also interoperable, meaning that they can communicate with each other using standard protocols and formats, regardless of the underlying platforms or technologies.
- SOA enables the reuse of existing services across different applications, reducing the development time and cost, and improving the consistency and quality of the software.
- SOA also facilitates the integration of heterogeneous systems, such as legacy applications, third-party systems, or cloud services, by providing a common interface and a standardized way of exchanging data.

## MSA Basics

- MSA is an architectural pattern that arranges an application as a collection of loosely coupled, fine-grained services, communicating through lightweight protocols.
- In MSA, each service is responsible for a single aspect of the application's functionality, such as authentication, authorization, or notification.
- Services are highly cohesive, meaning that they have a clear and well-defined responsibility and do not depend on other services for their internal logic.
- Services are also independently deployable, meaning that they can be updated or scaled without affecting the rest of the application.
- MSA enables the development of complex and large-scale applications by dividing them into smaller and simpler services that can be developed, tested, and deployed independently by different teams.
- MSA also supports the use of different technologies, languages, and frameworks for each service, allowing the developers to choose the best tools for their specific needs.

## SOA vs MSA

- The main distinction between SOA and MSA comes down to scope. SOA has an enterprise scope, while MSA has an application scope.
- SOA focuses on creating reusable and interoperable services that can be shared across different applications and domains, while MSA focuses on creating fine-grained and independent services that are specific to a single application and domain.
- SOA services tend to be coarse-grained, meaning that they provide a broad range of functionality and data, while MSA services tend to be fine-grained, meaning that they provide a narrow and focused functionality and data.
- SOA services are usually organized by business capabilities, such as customer, order, or product, while MSA services are usually organized by subdomains, such as identity, catalog, or payment.
- SOA services often rely on a centralized governance model, such as an enterprise service bus (ESB) or a service registry, to coordinate and manage the communication and orchestration of the services, while MSA services often rely on a decentralized governance model, such as an API gateway or a service mesh, to enable the discovery and routing of the services.
- SOA services may have different levels of maturity and quality, depending on the age and source of the service, while MSA services are expected to have a consistent and high level of maturity and quality, as they are developed and maintained by the same application team.

## Summary

- SOA and MSA are two service-based architectures that aim to improve the modularity, scalability, and maintainability of software applications.
- SOA is an enterprise-wide approach that focuses on creating reusable and interoperable services that can be shared across different applications and domains.
- MSA is an application-specific approach that focuses on creating fine-grained and independent services that are specific to a single application and domain.
- SOA and MSA differ in terms of the scope, granularity, and characteristics of the services, as well as the governance and quality models of the architecture.