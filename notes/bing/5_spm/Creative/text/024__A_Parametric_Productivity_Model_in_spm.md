### A Parametric Productivity Model in SPM

- A parametric productivity model is a mathematical model that relates the output of a software project to the input factors, such as size, complexity, quality, resources, etc.
- A parametric productivity model can be used to estimate the cost, effort, schedule, and quality of a software project, as well as to compare different alternatives and optimize the project plan.
- One of the most widely used parametric productivity models in software engineering is COCOMO (Constructive Cost Model), which was developed by Barry Boehm in 1981 and revised in 2000.
- COCOMO consists of three levels of models: basic, intermediate, and detailed, each with increasing accuracy and complexity.
- The basic COCOMO model estimates the effort and duration of a software project based on the size of the software (measured in lines of code or function points) and a set of coefficients that reflect the project type (organic, semi-detached, or embedded).
- The intermediate COCOMO model refines the basic model by introducing 15 cost drivers that account for various attributes of the software product, the hardware platform, the personnel, and the project environment.
- The detailed COCOMO model further extends the intermediate model by incorporating the effects of software reuse, software architecture, and software components on the effort and duration estimates.
- In SPM, parametric modulation is a technique that allows to model the variability in the neural response to a stimulus or condition based on a continuous or categorical variable that varies across trials .
- Parametric modulation can be used to test hypotheses about the neural correlates of cognitive processes, such as attention, memory, emotion, reward, etc.
- To perform parametric modulation in SPM, one needs to specify a parametric modulator regressor for each condition of interest, which is a vector that contains the values of the variable that modulates the neural response for each trial.
- SPM automatically orthogonalizes the parametric modulator regressors by default, which means that it removes any linear dependence between them and the main condition regressors.
- SPM also uses serial orthogonalization to orthogonalize multiple parametric modulators for the same condition, which means that it removes the linear dependence of each parametric modulator on the previous ones in the order they are specified.
- SPM estimates the beta coefficients for the parametric modulator regressors, which reflect the slope of the relationship between the neural response and the modulating variable.
- SPM also allows to perform a Parametric Empirical Bayes (PEB) analysis, which is a method to evaluate group effects and between-subjects variability on the parameters of a dynamic causal model (DCM).
- DCM is a framework that models the effective connectivity between brain regions based on the observed fMRI data and a biophysical model of neuronal activity and hemodynamics.
- PEB is a hierarchical Bayesian model that estimates the posterior distributions of the parameters of interest (such as the connection strengths, the modulatory effects, the intrinsic parameters, etc.) at the group level, as well as the covariance structure of the parameters across subjects.
- PEB can be used to test hypotheses about the differences or similarities of the parameters between groups or conditions, as well as to identify the most likely model structure or the optimal number of parameters for a given dataset.