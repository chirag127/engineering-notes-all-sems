A Parametric Productivity Model in spm is a method to evaluate group effects and between-subjects variability on parameters of dynamic causal models (DCMs) for fMRI data. It uses a Bayesian hierarchical model over the parameters, called Parametric Empirical Bayes (PEB), to describe how group level effects constrain parameter estimates on a subject-by-subject basis.

The following diagram illustrates the basic architecture of a Parametric Productivity Model in spm:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   First level   |      |   Second level  |      |   Third level   |
|                 |      |                 |      |                 |
|   DCM for fMRI  |----->|   PEB model     |----->|   PEB model     |
|                 |      |                 |      |                 |
|   Subject 1     |      |   Group 1       |      |   All groups    |
|   Subject 2     |      |   Group 2       |      |                 |
|   Subject 3     |      |   Group 3       |      |                 |
|   ...           |      |   ...           |      |                 |
|   Subject N     |      |   Group M       |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The first level consists of DCMs for fMRI for each subject, which estimate the effective connectivity between brain regions based on the experimental design and the observed BOLD signal. The second level consists of a PEB model for each group of subjects, which estimates the group effects and the between-subjects variability on the DCM parameters. The third level consists of a PEB model for all groups, which estimates the differences between groups on the DCM parameters. The arrows indicate the flow of information from one level to the next. The PEB models can be compared using Bayesian model comparison to test specific hypotheses about the DCM parameters .