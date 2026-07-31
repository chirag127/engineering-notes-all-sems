### A Parametric Productivity Model in SPM

- SPM stands for Statistical Parametric Mapping, a software package for analyzing functional neuroimaging data.
- A parametric productivity model is a way of estimating the productivity of a system or a process based on some parameters that affect its performance.
- In SPM, a parametric modulation regressor is used to predict variability in the strength of the neural response across different instances of the same condition.
- For example, if the condition is a memory task, the parametric modulation regressor could be the difficulty level of each trial, or the reaction time of the participant.
- To construct a parametric modulation regressor, we first need to construct a regressor that represents the mean or time-invariant neural response to the condition, and then multiply it by the parameter of interest.
- The parametric modulation regressor is then added to the design matrix as an additional column, and its beta coefficient reflects the slope of the relationship between the parameter and the neural response.
- In SPM, parametric modulators are automatically orthogonalized by default, so we don’t have to manually de-mean them ourselves. However, note that when we have more than one parametric modulator specified for a given condition, SPM uses what is called serial orthogonalization to orthogonalize the parameters.
- This means that the first parametric modulator is orthogonalized with respect to the mean regressor, the second parametric modulator is orthogonalized with respect to the mean regressor and the first parametric modulator, and so on.
- This can affect the interpretation of the beta coefficients, as they reflect the unique contribution of each parametric modulator after accounting for the others.
- A parametric productivity model in SPM can be useful for testing hypotheses about how different factors modulate the neural activity associated with a task or a stimulus.
- It can also help to identify brain regions that show differential sensitivity to these factors, and to quantify the magnitude and direction of the modulation.
- A parametric productivity model in SPM can be applied to different types of neuroimaging data, such as fMRI, PET, EEG, or MEG.
- SPM also includes a Parametric Empirical Bayes (PEB) model, which makes it possible to evaluate group effects and between-subjects variability on parameters.
- This page describes the main steps for performing a DCM+PEB analysis, where DCM stands for Dynamic Causal Modeling, a method for estimating effective connectivity between brain regions.