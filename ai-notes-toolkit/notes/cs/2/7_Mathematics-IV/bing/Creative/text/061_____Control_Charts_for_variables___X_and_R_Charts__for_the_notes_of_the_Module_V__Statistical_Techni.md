### Control Charts for variables ( X and R Charts)

- Control charts are graphical tools used to monitor the quality of a process by plotting sample data over time and comparing them with predefined control limits.
- Control charts for variables are used when the quality characteristic of interest is a continuous variable, such as weight, length, temperature, etc.
- X-bar and R charts are the most common type of control charts for variables. They are used to monitor the mean and variation of a process based on samples taken at regular intervals .
- X-bar chart plots the sample mean (X-bar) of each subgroup and monitors the changes in the process mean over time. R chart plots the sample range (R) of each subgroup and monitors the changes in the process variation over time .
- X-bar and R charts are usually paired together, as they provide complementary information about the process stability and capability .
- To construct X-bar and R charts, the following steps are required  :
  - Collect samples of fixed size (n) from the process at regular intervals (k).
  - Calculate the sample mean (X-bar) and range (R) for each subgroup.
  - Calculate the grand mean (X-double-bar) and the average range (R-bar) of all subgroups.
  - Calculate the control limits for both charts using the following formulas:

    - X-bar chart: 
      - Upper control limit (UCL) = X-double-bar + A2 * R-bar
      - Lower control limit (LCL) = X-double-bar - A2 * R-bar
      - Center line (CL) = X-double-bar
    - R chart: 
      - Upper control limit (UCL) = D4 * R-bar
      - Lower control limit (LCL) = D3 * R-bar
      - Center line (CL) = R-bar

    - Where A2, D3 and D4 are constants that depend on the sample size (n) and can be found in statistical tables.
  - Plot the sample means and ranges on the X-bar and R charts respectively, along with the control limits and the center line.
  - Analyze the charts for any patterns or points that indicate the process is out of control, such as points beyond the control limits, runs of points on one side of the center line, trends, cycles, etc.
  - Investigate the causes of any out-of-control signals and take corrective actions if necessary.
  - Update the charts with new data and repeat the analysis.