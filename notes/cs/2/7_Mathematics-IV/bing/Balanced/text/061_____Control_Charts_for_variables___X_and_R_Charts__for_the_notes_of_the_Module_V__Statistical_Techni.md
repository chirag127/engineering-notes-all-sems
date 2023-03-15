### Control Charts for Variables (X and R Charts)

- Control charts are graphical tools used to monitor the quality of a process by plotting sample data over time and comparing them with predefined control limits.
- Variables are measurable characteristics of a process, such as length, weight, temperature, etc.
- X and R charts are a pair of control charts that are used with variables data when the subgroup size is two or more.
- X chart plots the subgroup averages (X) and monitors the central tendency of the process.
- R chart plots the subgroup ranges (R) and monitors the variation of the process.
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
- The X and R charts should be constructed and analyzed together, as they complement each other and provide a complete picture of the process behavior.
- The X and R charts are used to determine if a process is stable and predictable, meaning that it is in a state of statistical control and only affected by common causes of variation .
- A process is considered out of control if any of the following rules are violated on the X or R chart :

  - One point falls outside the control limits
  - Two out of three consecutive points fall beyond the 2-sigma warning limits
  - Four out of five consecutive points fall beyond the 1-sigma warning limits
  - Eight consecutive points fall on one side of the center line
  - Six points in a row steadily increase or decrease
  - Fourteen points in a row alternate up and down
  - Fifteen points in a row fall within the 1-sigma warning limits
  - Eight points in a row fall outside the 1-sigma warning limits

- If a process is out of control, the assignable causes of variation should be identified and eliminated, and the control limits should be recalculated using the new data .
- If a process is in control, the control limits can be used to estimate the process capability, which is the ability of the process to meet the customer specifications .
- The process capability can be measured by the following ratios :

  - Cp = (USL - LSL) / (6 * sigma)
  - Cpk = min [(USL - X-bar-bar) / (3 * sigma), (X-bar-bar - LSL) / (3 * sigma)]

  - Where USL and LSL are the upper and lower specification limits, and sigma is the estimated process standard deviation, which can be calculated as sigma = R-bar / d2, where d2 is another constant that depends on the subgroup size .
- A process is capable if Cp and Cpk are both greater than or equal to 1, meaning that the process variation is within the specification limits .
- A process is not capable if Cp or Cpk are less than 1, meaning that the process variation exceeds the specification limits .
- A process is centered if Cp and Cpk are equal, meaning that the process mean is at the midpoint of the specification limits .
- A process is not centered if Cp and Cpk are not equal, meaning that the process mean is shifted towards one of the specification limits .