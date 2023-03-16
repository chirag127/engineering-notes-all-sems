### Architectural Representation for the notes of the Unit 1 - BUSINESS INTELLIGENCE – INTRODUCTION in the subject of BUSINESS INTELLIGENCE AND ANALYTICS KCS

- Business Intelligence (BI) is a set of processes, architectures, and technologies that convert raw data into meaningful information that drives profitable business actions.
- A business intelligence architecture articulates the technology standards and data management and analytics practices that support an organization's BI efforts, as well as the specific platforms and tools that will be deployed.
- A typical BI architecture consists of the following components :
  - Data sources: These are the original sources of data, such as databases, files, web services, etc.
  - Data integration: This is the process of extracting, transforming, and loading (ETL) data from various sources into a data warehouse or a data lake, which is a centralized repository of integrated data.
  - Data warehouse or data lake: This is the core component of a BI architecture, where data is stored, organized, and modeled for analysis. A data warehouse is a relational database that follows a dimensional model, while a data lake is a non-relational database that stores data in its raw or semi-structured format.
  - Data marts: These are subsets of data from the data warehouse or data lake, tailored for specific business domains or analytical purposes. Data marts can be based on star or snowflake schemas, which are simplified representations of data dimensions and measures.
  - Data analysis and reporting: This is the process of applying various analytical techniques and tools to the data in the data warehouse or data lake, to generate insights, reports, dashboards, and visualizations. Some of the common tools are OLAP (online analytical processing), data mining, machine learning, and business analytics.
  - Data delivery and consumption: This is the process of delivering and presenting the data analysis and reporting results to the end-users, such as business managers, analysts, or customers. This can be done through various channels, such as web portals, mobile applications, email, etc.
- A sample BI architecture diagram is shown below:

![BI architecture diagram](https://cdn.ttgtmedia.com/rms/onlineImages/bi-business_intelligence_architecture_desktop.png)

- Business intelligence architectures can vary depending on the size, complexity, and needs of the organization. Some of the factors that influence the design of a BI architecture are:
  - Data volume and variety: The amount and type of data that needs to be collected, integrated, and analyzed can affect the choice of data sources, data integration tools, and data storage platforms.
  - Data quality and governance: The accuracy, completeness, and consistency of data can affect the reliability and validity of the data analysis and reporting results. Data quality and governance processes ensure that data is cleansed, standardized, and secured according to the business rules and policies.
  - Data latency and frequency: The time lag and frequency of data updates can affect the timeliness and relevance of the data analysis and reporting results. Data latency and frequency depend on the data sources, data integration tools, and data delivery and consumption methods.
  - Data users and usage: The number and type of data users and the purpose and scope of data usage can affect the design and functionality of the data analysis and reporting tools and the data delivery and consumption channels.
  - Data security and privacy: The protection and confidentiality of data can affect the access and control of data by different data users and stakeholders. Data security and privacy measures include encryption, authentication, authorization, and auditing.