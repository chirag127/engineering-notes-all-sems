### A Parametric Productivity Model in SPM

- A parametric productivity model is a way of analyzing how the brain responds to different aspects of a stimulus or a task, such as intensity, difficulty, reward, etc.
- A parametric productivity model uses parametric modulators, which are variables that modulate the amplitude of the neural response to a condition according to some parameter of interest.
- A parametric productivity model can be implemented in SPM using the following steps:
  - Specify a general linear model (GLM) for each subject, with one or more parametric modulators for each condition of interest.
  - Estimate the GLM and obtain the parameter estimates for each voxel and each modulator.
  - Perform a group-level analysis using a parametric empirical Bayes (PEB) model, which allows testing for group effects and between-subject variability on the modulators.
  - Compare the full PEB model to nested PEB models to test specific hypotheses about the modulators, or search over nested PEB models to find the optimal model.
  - Review the results and interpret the posterior probabilities and significance of the modulators.