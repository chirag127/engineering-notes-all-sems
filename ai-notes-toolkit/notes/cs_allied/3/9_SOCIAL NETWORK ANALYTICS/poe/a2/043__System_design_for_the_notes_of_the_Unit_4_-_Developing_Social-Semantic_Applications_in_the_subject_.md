 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### System design for the notes of the Unit 4 - Developing Social-Semantic Applications in the subject of SOCIAL NETWORK ANALYTICS

1. Identify the components:
- Data ingestion: APIs to import data from social networks
- Data storage: Databases to store user data, social graph, posts, etc.
- Data processing: Systems to process and compute metrics on the data
- APIs: APIs to query the data and metrics
- Visualization: Dashboards to visualize the data and metrics

2. Scale the components:
- Distributed databases for large data scales
- Queueing systems and distributed processing for scalable data processing
- Load balancers and caching for scalable APIs
- Optimized data models and indexing for fast queries
- sampled data and pre-aggregated metrics for fast visualizations

3. Ensure reliability:
- Replication of databases for high availability
- Fault-tolerant processing using retries and replication
- Graceful degradation of APIs and visualizations

4. Optimize for performance:
- Denormalized data models for fast joins
- Database indexing for fast lookups
- Caching for fast API responses
- Asynchronous and distributed architecture for fast processing
- Sampling and pre-aggregation for fast visualizations

5. Manage complexity:
- Microservices architecture to isolate components
- Automation for deployments and testing
- Monitoring and logging for observability