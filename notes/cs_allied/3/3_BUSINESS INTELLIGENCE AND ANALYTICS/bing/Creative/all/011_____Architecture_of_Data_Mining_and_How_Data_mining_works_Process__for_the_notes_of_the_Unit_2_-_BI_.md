# Architecture of Data Mining and How Data Mining Works (Process)

## Architecture of Data Mining

- Data mining is the process of discovering meaningful new correlations, patterns, and trends by shifting through large amounts of data stored in repositories, using pattern recognition technologies as well as statistical and mathematical techniques.
- Data mining involves several components, and these components constitute a data mining system architecture. The major components of data mining systems are:

  - **Data source**: This is the source of data that will be analyzed by the data mining system. It can be a database, a data warehouse, a data stream, or any other data collection.
  - **Data mining engine**: This is the core component of the data mining system that implements various data mining algorithms and techniques to extract patterns and knowledge from the data. It can be a single module or a collection of modules that communicate with each other.
  - **Data warehouse server**: This is the component that provides an efficient and convenient way to store, access, and manage the data that is required for data mining. It can be a relational database, a multidimensional database, or a specialized data repository.
  - **Pattern evaluation module**: This is the component that evaluates the patterns and knowledge discovered by the data mining engine and determines their relevance and usefulness for the given problem or goal. It can use various criteria, such as interestingness, novelty, validity, or simplicity, to rank and filter the patterns.
  - **Graphical user interface**: This is the component that allows the user to interact with the data mining system and visualize the data, the patterns, and the results. It can provide various features, such as query and reporting tools, data exploration and manipulation tools, data mining task specification and execution tools, and data mining result presentation and interpretation tools.
  - **Knowledge base**: This is the component that stores the domain knowledge and the user preferences that are used to guide the data mining process and improve the quality and efficiency of the data mining results. It can include various types of information, such as metadata, concept hierarchies, background knowledge, or user feedback.

- There are different types of data mining architecture, depending on how the data mining system is coupled with the data source or the data warehouse server. The main types are:

  - **No coupling**: The data mining system retrieves data from a particular data source and does not use the data warehouse server. It operates independently of the data source and the data warehouse server.
  - **Loose coupling**: The data mining system retrieves data from the data warehouse server and stores the data in an intermediate form, such as a file or a table. It operates independently of the data source but depends on the data warehouse server.
  - **Semi-tight coupling**: The data mining system uses some functions or services provided by the data warehouse server, such as indexing, sorting, aggregation, or summarization. It operates independently of the data source but interacts with the data warehouse server.
  - **Tight coupling**: The data mining system is integrated with the data warehouse server and uses the same data structures and query languages. It operates as a part of the data warehouse server.

## How Data Mining Works (Process)

- Data mining is a complex and iterative process that involves several steps and sub-steps. The main steps of data mining are:

  - **Setting objectives**: This is the first and most important step of data mining, where the problem or goal of data mining is defined and the expected outcomes and benefits are identified. This step also involves determining the scope, the resources, and the constraints of the data mining project.
  - **Data gathering and preparation**: This is the step where the relevant data for data mining is collected, cleaned, integrated, transformed, and formatted. This step also involves selecting the appropriate data mining techniques and tools for the data and the problem.
  - **Applying data mining algorithms**: This is the step where the data mining engine applies various data mining algorithms and techniques to the data and extracts patterns and knowledge from it. This step can involve multiple iterations and refinements of the data mining algorithms and parameters.
  - **Evaluating results**: This is the step where the patterns and knowledge discovered by the data mining engine are evaluated by the pattern evaluation module and the user. This step involves assessing the quality, relevance, and usefulness of the data mining results and comparing them with the objectives and expectations of the data mining project.
  - **Deploying and updating**: This is the final step of data mining, where the data mining results are deployed and integrated with the existing systems and processes. This step also involves monitoring