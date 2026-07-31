### Control Charts for Variables (X and R Charts)

- Control charts are graphical tools used to monitor the quality of a process by plotting sample data over time and comparing them with predefined control limits.
- Variables are measurable characteristics of a process, such as length, weight, temperature, etc.
- X and R charts are a pair of control charts that are used with variables data that have a subgroup size of two or more.
- X chart plots the sample means (X-bar) of the subgroups and monitors the changes in the process mean.
- R chart plots the sample ranges (R) of the subgroups and monitors the changes in the process variation.
- The control limits for the X chart are calculated as:

  - Upper control limit (UCL) = X-bar-bar + A2 * R-bar
  - Lower control limit (LCL) = X-bar-bar - A2 * R-bar
  - Center line (CL) = X-bar-bar

  where X-bar-bar is the grand mean of the sample means, R-bar is the average of the sample ranges, and A2 is a constant that depends on the subgroup size.

- The control limits for the R chart are calculated as:

  - Upper control limit (UCL) = D4 * R-bar
  - Lower control limit (LCL) = D3 * R-bar
  - Center line (CL) = R-bar

  where D3 and D4 are constants that depend on the subgroup size.

- The control limits for both charts are based on the assumption that the process is in control and follows a normal distribution.
- The sample size for the X and R charts should be large enough to detect meaningful shifts in the process, but not too large to be impractical or costly.
- A common rule of thumb is to use a sample size of 4 or 5, unless the process variation is very small or very large.
- The X and R charts are used together to check the stability and predictability of a process.
- A process is said to be in control if all the points on both charts are within the control limits and show no patterns or trends.
- A process is said to be out of control if any of the following rules are violated:

  - One or more points are beyond the control limits
  - Two out of three consecutive points are beyond the 2-sigma limits
  - Four out of five consecutive points are beyond the 1-sigma limits
  - Eight or more consecutive points are on the same side of the center line
  - Six or more consecutive points are increasing or decreasing
  - Fourteen or more consecutive points alternate up and down

- If a process is out of control, the cause of the variation should be identified and eliminated before continuing with the charting.
- The X and R charts are useful for:

  - Monitoring the performance of a process over time
  - Detecting the presence of special causes of variation
  - Evaluating the effect of process improvement actions
  - Estimating the process capability and potential  .