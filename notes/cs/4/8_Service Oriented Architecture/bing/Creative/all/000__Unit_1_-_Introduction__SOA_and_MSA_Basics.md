## Unit 1 - Introduction: SOA and MSA Basics

- SOA stands for Service-Oriented Architecture, which is a software design style that consists of multiple self-contained, discrete, and repeatable services that communicate with each other through a service interface .
- MSA stands for Microservice Architecture, which is a variant of SOA that breaks down a single application into multiple loosely coupled, independent services that run in their own processes and can have different operating systems and databases .
- Both SOA and MSA rely on services as the main component, but they differ in terms of service characteristics, such as granularity, reusability, governance, communication, and deployment .
- Some of the main differences between SOA and MSA are:

| SOA | MSA |
| --- | --- |
| Share as much as possible | Share as little as possible |
| Emphasize on business functionality reuse | Emphasize on the concept of bounded context |
| Have common governance and standards | Have relaxed governance and more freedom in choosing technologies |
| Use an enterprise service bus (ESB) for communication | Use a simple, less elaborate messaging system |
| Support multiple message protocols | Prefer lightweight protocols such as REST or gRPC |
| Deploy services to a common platform | Deploy services to separate containers or servers |
| Use multi-threading with more overheads | Use single-threading with less overheads |
| Maximize application service reusability | Minimize service dependencies |
| More likely to use traditional relational databases | More likely to use NoSQL or polyglot persistence |
| Not preferred in a DevOps model | Preferred in a DevOps model |

- A mnemonic to remember the differences between SOA and MSA is: **S**hare, **R**euse, **G**overn, **E**SB, **M**ulti, **C**ommon, **M**ulti, **M**ax, **R**elational, **N**ot (for SOA) and **S**hare, **B**ounded, **F**reedom, **S**imple, **L**ight, **S**eparate, **S**ingle, **M**in, **N**oSQL, **P**referred (for MSA).
- An example of SOA is a banking application that uses services such as account management, transaction processing, fraud detection, and customer support, which are shared and reused by different business processes and applications.
- An example of MSA is a hotel reservation system that uses services such as room availability, booking confirmation, payment processing, and notification, which are independent and self-contained and can be deployed and scaled separately.