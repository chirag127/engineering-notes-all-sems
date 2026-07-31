### Predicting the goodness of fit for the notes of the Unit 5 - Evaluation of Social Network Analysis

- Goodness of fit is a statistical concept that measures how well a model fits the observed data.
- In social network analysis, goodness of fit can be used to evaluate how well a network model captures the structural properties of a real network, such as density, reciprocity, clustering, degree distribution, etc.
- One way to assess the goodness of fit of a network model is to use the exponential random graph model (ERGM), which is a family of models that can represent various network features using parameters and functions.
- To estimate the parameters of an ERGM, one can use maximum likelihood estimation (MLE), which finds the values that maximize the probability of observing the data given the model.
- To test the goodness of fit of an ERGM, one can use the following steps :
  - Generate a set of simulated networks from the fitted ERGM using Markov chain Monte Carlo (MCMC) methods.
  - Calculate the network statistics of interest (such as density, reciprocity, clustering, etc.) for each simulated network and the observed network.
  - Compare the distributions of the network statistics across the simulated networks and the observed network using graphical or numerical methods, such as histograms, boxplots, or quantile-quantile plots.
  - If the distributions are similar, then the ERGM has a good fit to the data. If the distributions are different, then the ERGM has a poor fit and may need to be modified or rejected.
- Another way to assess the goodness of fit of a network model is to use the chi-square test, which is a common method for testing the difference between observed and expected frequencies in categorical data.
  - To use the chi-square test for network data, one needs to divide the network into cells based on some criteria, such as node attributes, edge types, or network partitions.
  - Then, one needs to calculate the observed and expected frequencies of each cell, where the expected frequencies are based on the network model or a null hypothesis.
  - Next, one needs to compute the chi-square statistic, which is the sum of the squared differences between the observed and expected frequencies, divided by the expected frequencies.
  - Finally, one needs to compare the chi-square statistic with a critical value from the chi-square distribution, which depends on the degrees of freedom and the significance level of the test.
  - If the chi-square statistic is larger than the critical value, then the network model does not fit the data well. If the chi-square statistic is smaller than the critical value, then the network model fits the data well.
- Goodness of fit is an important aspect of social network analysis, as it can help to validate, compare, and improve network models, as well as to understand the underlying mechanisms and processes that shape network structures and dynamics.