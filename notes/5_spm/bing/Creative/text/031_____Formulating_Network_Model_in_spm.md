### Formulating Network Model in SPM

- SPM stands for Statistical Parametric Mapping, which is a method for analyzing brain imaging data such as fMRI, PET, EEG, etc.
- A network model in SPM is a way of representing the functional connectivity between different brain regions or nodes, based on their temporal correlations or causal interactions.
- To formulate a network model in SPM, one needs to follow these steps:

  - Define the nodes of the network, which can be based on anatomical regions of interest (ROIs), functional ROIs, or independent components.
  - Extract the time series of each node from the imaging data, using a suitable method such as averaging, principal component analysis, or independent component analysis.
  - Choose a measure of connectivity between the nodes, which can be based on correlation, coherence, phase synchronization, Granger causality, dynamic causal modeling, etc.
  - Compute the connectivity matrix or graph, which shows the strength and direction of the connectivity between each pair of nodes.
  - Analyze the network properties, such as modularity, centrality, efficiency, clustering, etc., using graph theory methods or other tools.
  - Interpret the network results in relation to the experimental design, hypotheses, and previous literature.