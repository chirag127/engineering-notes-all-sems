# Control Charts for Variables (p, np and c charts)

Control charts are graphical tools that help monitor the quality of a process by plotting the variation of a quality characteristic over time. Control charts can be classified into two types: variable control charts and attribute control charts. Variable control charts are used for continuous data, such as length, weight, temperature, etc. Attribute control charts are used for discrete data, such as defects, errors, failures, etc.

In this note, we will focus on three types of attribute control charts: p chart, np chart and c chart. These charts are used for different situations and assumptions.

## p chart

A p chart is used to monitor the proportion of defective items in a sample. For example, if we inspect 100 items and find 5 defective ones, the proportion of defective items is 0.05. A p chart plots the proportion of defective items for each sample over time and compares it with the center line (the average proportion of defective items) and the control limits (the upper and lower bounds of the natural variation of the proportion of defective items).

The assumptions of a p chart are:

- The samples are independent and randomly selected from the process.
- The sample size is constant or varies slightly.
- The probability of defect is the same for each item.
- The proportion of defective items follows a binomial distribution.

The formula for the center line and the control limits of a p chart are:

- Center line: p-bar = (total number of defective items) / (total number of items inspected)
- Upper control limit: p-bar + z * sqrt(p-bar * (1 - p-bar) / n)
- Lower control limit: p-bar - z * sqrt(p-bar * (1 - p-bar) / n)

where z is the standard normal deviate corresponding to the desired confidence level (usually 3 for 99.73% confidence), and n is the sample size.

## np chart

An np chart is used to monitor the number of defective items in a sample. For example, if we inspect 100 items and find 5 defective ones, the number of defective items is 5. An np chart plots the number of defective items for each sample over time and compares it with the center line (the average number of defective items) and the control limits (the upper and lower bounds of the natural variation of the number of defective items).

The assumptions of an np chart are:

- The samples are independent and randomly selected from the process.
- The sample size is constant.
- The probability of defect is the same for each item.
- The number of defective items follows a binomial distribution.

The formula for the center line and the control limits of an np chart are:

- Center line: np-bar = n * p-bar
- Upper control limit: np-bar + z * sqrt(np-bar * (1 - p-bar))
- Lower control limit: np-bar - z * sqrt(np-bar * (1 - p-bar))

where z is the standard normal deviate corresponding to the desired confidence level (usually 3 for 99.73% confidence), n is the sample size, and p-bar is the average proportion of defective items.

## c chart

A c chart is used to monitor the number of defects in a sample. For example, if we inspect a car and find 3 scratches, 2 dents and 1 broken light, the number of defects is 6. A c chart plots the number of defects for each sample over time and compares it with the center line (the average number of defects) and the control limits (the upper and lower bounds of the natural variation of the number of defects).

The assumptions of a c chart are:

- The samples are independent and randomly selected from the process.
- The sample size is constant or varies slightly.
- The probability of defect is the same for each item.
- The number of defects follows a Poisson distribution.

The formula for the center line and the control limits of a c chart are:

- Center line: c-bar = (total number of defects) / (total number of samples)
- Upper control limit: c-bar + z * sqrt(c-bar)
- Lower control limit: c-bar - z * sqrt(c-bar)

where z is the standard normal deviate corresponding to the desired confidence level (usually 3 for 99.73% confidence).

## References

: https://sixsigmastudyguide.com/p-attribute-charts/
: https://sixsigmastudyguide.com/attribute-chart-np-chart/
: https://sixsigmastudyguide.com/attribute-chart