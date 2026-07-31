### Control Charts for Variables (p, np and c charts)

- Control charts are graphical tools that help monitor the quality of a process or product over time.
- Control charts can be classified into two types: variable control charts and attribute control charts.
- Variable control charts are used for continuous data, such as length, weight, temperature, etc. Attribute control charts are used for discrete data, such as defects, errors, failures, etc.
- There are four types of attribute control charts: p chart, np chart, c chart and u chart.
- p chart is used to plot the proportion of defective items in a sample. np chart is used to plot the number of defective items in a sample. c chart is used to plot the number of defects in a sample. u chart is used to plot the number of defects per unit in a sample.
- The assumptions for attribute control charts are:
  - The samples are independent and randomly selected from the population.
  - The items are classified into two categories: defective or non-defective, or defect or non-defect.
  - The probability of defect is constant for each item and each sample (except for u chart).
- The control limits for attribute control charts are calculated using the following formulas:

  - p chart: $\overline{p} \pm z\sqrt{\frac{\overline{p}(1-\overline{p})}{n}}$, where $\overline{p}$ is the average proportion of defective items, $n$ is the sample size, and $z$ is the standard normal deviate corresponding to the desired confidence level (usually 3).
  - np chart: $\overline{np} \pm z\sqrt{\overline{np}(1-\overline{p})}$, where $\overline{np}$ is the average number of defective items, and the other terms are the same as above.
  - c chart: $\overline{c} \pm z\sqrt{\overline{c}}$, where $\overline{c}$ is the average number of defects.
  - u chart: $\overline{u} \pm z\sqrt{\frac{\overline{u}}{n}}$, where $\overline{u}$ is the average number of defects per unit, and $n$ is the average sample size.

- To construct an attribute control chart, the following steps are followed:
  - Collect data in subgroups or samples over time.
  - Calculate the relevant statistic for each sample (p, np, c or u).
  - Plot the statistic on a chart with a center line (the average of the statistic) and control limits (the upper and lower bounds of the statistic).
  - Analyze the chart for any patterns or trends that indicate the process is out of control, such as points beyond the control limits, runs of points on one side of the center line, or cycles or shifts in the data.