### Control Charts for Variables (p, np and c charts)

Control charts are graphical tools that help monitor the quality of a process or product over time. They plot the values of a quality characteristic against a time scale and compare them with predetermined control limits. Control charts can be classified into two types: variables control charts and attributes control charts.

Variables control charts are used when the quality characteristic is measured on a continuous scale, such as weight, length, temperature, etc. Attributes control charts are used when the quality characteristic is counted or classified into categories, such as defective or non-defective, pass or fail, etc.

There are four types of attributes control charts: p, np, c and u charts. Each of them has different assumptions and applications.

- p chart: This chart plots the proportion of defective items in a sample. It is used when the sample size is variable and the items can be classified into two categories: defective or non-defective. The assumptions of the p chart are:

  - The items are sampled randomly from the population.
  - The items are independent of each other.
  - The probability of defect is constant for each item.
  - The sample size is large enough (at least 20) to approximate the binomial distribution by the normal distribution.

- np chart: This chart plots the number of defective items in a sample. It is used when the sample size is constant and the items can be classified into two categories: defective or non-defective. The assumptions of the np chart are:

  - The items are sampled randomly from the population.
  - The items are independent of each other.
  - The probability of defect is constant for each item.

- c chart: This chart plots the number of defects in a sample. It is used when the sample size is variable and the items can have more than one defect. The assumptions of the c chart are:

  - The items are sampled randomly from the population.
  - The items are independent of each other.
  - The probability of defect is constant for each item.
  - The defects are independent of each other.

- u chart: This chart plots the average number of defects per unit in a sample. It is used when the sample size is variable and the items can have more than one defect. The assumptions of the u chart are:

  - The items are sampled randomly from the population.
  - The items are independent of each other.
  - The probability of defect is constant for each item.
  - The defects are independent of each other.

The formulas for calculating the control limits and the center line for each type of chart are given in the table below:

| Chart | Center line | Upper control limit | Lower control limit |
| ----- | ----------- | ------------------- | ------------------- |
| p     | $\bar{p}$   | $\bar{p} + 3\sqrt{\frac{\bar{p}(1-\bar{p})}{\bar{n}}}$ | $\bar{p} - 3\sqrt{\frac{\bar{p}(1-\bar{p})}{\bar{n}}}$ |
| np    | $\bar{n}\bar{p}$ | $\bar{n}\bar{p} + 3\sqrt{\bar{n}\bar{p}(1-\bar{p})}$ | $\bar{n}\bar{p} - 3\sqrt{\bar{n}\bar{p}(1-\bar{p})}$ |
| c     | $\bar{c}$   | $\bar{c} + 3\sqrt{\bar{c}}$ | $\bar{c} - 3\sqrt{\bar{c}}$ |
| u     | $\bar{u}$   | $\bar{u} + 3\sqrt{\frac{\bar{u}}{\bar{n}}}$ | $\bar{u} - 3\sqrt{\frac{\bar{u}}{\bar{n}}}$ |

Where $\bar{p}$ is the average proportion of defective items, $\bar{n}$ is the average sample size, $\bar{c}$ is the average number of defects, and $\bar{u}$ is the average number of defects per unit.

To construct and interpret a control chart, the following steps are followed:

1. Collect and plot the data on the chart.
2. Calculate the center line and the control limits using the formulas above.
3. Draw the center line and the control limits on the chart.
4. Analyze the chart for any patterns or trends that indicate the process is out of control, such as points beyond the control limits, runs of points above or below the center line