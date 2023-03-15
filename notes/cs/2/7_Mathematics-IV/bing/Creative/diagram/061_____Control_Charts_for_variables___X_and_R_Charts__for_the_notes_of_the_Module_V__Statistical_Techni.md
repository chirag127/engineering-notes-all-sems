### Control Charts for Variables (X and R Charts)

- Control charts are graphical tools used to monitor the quality of a process by plotting sample data over time and comparing them with predefined control limits.
- Variables are measurable characteristics of a process, such as length, weight, temperature, etc.
- X and R charts are a pair of control charts that are used with variables data when the subgroup size is two or more.
- X chart plots the subgroup averages (X) and monitors the changes in the process mean.
- R chart plots the subgroup ranges (R) and monitors the changes in the process variation.
- The control limits for both charts are calculated using the following formulas :

    - X chart: 
        - Center line (CL) = grand average of subgroup averages = X-bar-bar
        - Upper control limit (UCL) = X-bar-bar + A2 * R-bar
        - Lower control limit (LCL) = X-bar-bar - A2 * R-bar
    - R chart: 
        - Center line (CL) = average of subgroup ranges = R-bar
        - Upper control limit (UCL) = D4 * R-bar
        - Lower control limit (LCL) = D3 * R-bar

    - Where A2, D3 and D4 are constants that depend on the subgroup size and can be found in statistical tables .
- The X and R charts are constructed by plotting the subgroup averages and ranges against the subgroup number or time, and drawing the center line and the control limits on each chart .
- The X and R charts are used together to analyze the stability and capability of a process .
- A process is stable if the points on both charts are within the control limits and show no patterns or trends .
- A process is capable if the natural variation of the process is within the specification limits set by the customer or the design .
- The process capability can be assessed by calculating the process capability index (Cp), which is the ratio of the specification width to the process width :

    - Cp = (USL - LSL) / 6 * sigma
    - Where USL and LSL are the upper and lower specification limits, and sigma is the estimated process standard deviation .
    - A Cp value greater than 1 indicates that the process is capable, while a Cp value less than 1 indicates that the process is not capable .
- The X and R charts are widely used in quality control and improvement, as they help to detect and eliminate the sources of variation that affect the process performance .