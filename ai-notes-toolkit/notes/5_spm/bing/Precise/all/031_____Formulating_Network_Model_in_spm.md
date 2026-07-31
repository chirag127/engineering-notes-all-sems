# Formulating Network Model in SPM

1. **Introduction:** SPM (Statistical Parametric Mapping) is a software package used for the analysis of functional neuroimaging data. One of the ways to analyze this data is by formulating a network model.

2. **Defining the network:** The first step in formulating a network model in SPM is to define the network. This involves selecting the regions of interest (ROIs) that will be included in the network. These ROIs can be selected based on prior knowledge or by using a data-driven approach.

3. **Extracting time series:** Once the ROIs have been selected, the next step is to extract the time series data from each ROI. This can be done using the `spm_regions` function in SPM.

4. **Defining the model:** After the time series data has been extracted, the next step is to define the network model. This involves specifying the connections between the ROIs and the type of model that will be used to represent these connections.

5. **Estimating the model:** Once the model has been defined, the next step is to estimate the model parameters. This can be done using the `spm_dcm_estimate` function in SPM.

6. **Interpreting the results:** After the model has been estimated, the final step is to interpret the results. This involves examining the estimated model parameters to draw conclusions about the functional connectivity between the ROIs in the network.