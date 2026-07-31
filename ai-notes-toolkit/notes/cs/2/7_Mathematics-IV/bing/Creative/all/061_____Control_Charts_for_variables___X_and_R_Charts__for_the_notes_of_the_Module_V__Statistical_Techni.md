# Control Charts for Variables (X and R Charts)

- Control charts are graphical tools that help monitor the quality of a process by plotting the values of a quality characteristic over time and comparing them with predefined control limits.
- Control charts for variables are used when the quality characteristic is measured on a continuous scale, such as weight, length, temperature, etc.
- X and R charts are a pair of control charts for variables that are used when the subgroup size is two or more, but typically less than 10.
- X chart plots the subgroup averages (X) and monitors the changes in the process mean.
- R chart plots the subgroup ranges (R) and monitors the changes in the process variation.
- X and R charts are usually constructed together, since both the mean and the variation of a process need to be in control for the process to be stable and predictable.
- The steps to construct X and R charts are:

  - Collect data in subgroups of size n at regular intervals from the process.
  - Calculate the subgroup averages (X) and ranges (R) for each subgroup.
  - Calculate the grand average (X-bar-bar) and the average range (R-bar) of all the subgroups.
  - Calculate the control limits for the X chart using the formula:

    - Upper control limit (UCL) = X-bar-bar + A2 * R-bar
    - Lower control limit (LCL) = X-bar-bar - A2 * R-bar
    - Center line (CL) = X-bar-bar

    - Where A2 is a constant that depends on the subgroup size n and can be found in a table.

  - Calculate the control limits for the R chart using the formula:

    - Upper control limit (UCL) = D4 * R-bar
    - Lower control limit (LCL) = D3 * R-bar
    - Center line (CL) = R-bar

    - Where D3 and D4 are constants that depend on the subgroup size n and can be found in a table.

  - Plot the subgroup averages (X) and ranges (R) on the X and R charts respectively, along with the control limits and the center lines.
  - Analyze the charts for any patterns or points that indicate an out-of-control situation, such as:

    - A point outside the control limits
    - A run of seven or more points on one side of the center line
    - A trend of six or more points steadily increasing or decreasing
    - A cycle of points repeating a certain pattern
    - A sudden or unusual change in the level or variation of the points.

  - If any out-of-control signals are detected, investigate the possible causes and take corrective actions to eliminate them.
  - Update the charts with new data and revise the control limits if necessary.