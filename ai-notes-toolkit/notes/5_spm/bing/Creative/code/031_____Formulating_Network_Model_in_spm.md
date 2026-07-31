### Formulating Network Model in SPM

- SPM stands for Statistical Parametric Mapping, a software package for analyzing brain imaging data.
- A network model is a way of representing the interactions among brain regions or nodes using a graph or matrix.
- To formulate a network model in SPM, one needs to follow these steps:

  1. Preprocess the imaging data to remove noise, artifacts, and confounds, and to align the images to a common space.
  2. Extract the time series of each node of interest from the preprocessed data, using a region of interest (ROI) mask or a parcellation scheme.
  3. Compute the functional connectivity or effective connectivity between each pair of nodes, using a measure such as correlation, coherence, or dynamic causal modeling (DCM).
  4. Construct a network matrix or graph from the connectivity values, where each element or edge represents the strength of the connection between two nodes.
  5. Analyze the network properties, such as centrality, modularity, efficiency, or resilience, using graph theory methods or network statistics.
  6. Interpret the network results in relation to the research question, the cognitive or clinical context, and the existing literature.