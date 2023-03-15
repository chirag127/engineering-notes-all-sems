# Control Charts for Variables (p, np and c charts)

Control charts are graphical tools that help monitor the quality of a process by plotting the variation of a measured characteristic over time. They are used to detect and prevent the occurrence of special causes of variation that may affect the process performance.

There are different types of control charts depending on the type of data being measured. For attribute data, which are discrete and categorical, there are four common types of control charts: p, np, c and u charts.

## p chart

A p chart is used to plot the proportion of defective items in a sample. A defective item is one that does not meet the quality specifications. For example, a p chart can be used to monitor the proportion of defective light bulbs produced by a factory.

The assumptions of a p chart are:

- The samples are independent and randomly selected from the process.
- The sample size is constant or varies within a small range.
- The probability of defect is the same for each item.

The formula for the center line and the control limits of a p chart are:

- Center line: p-bar = (total number of defectives in all samples) / (total number of items in all samples)
- Upper control limit: p-bar + z * sqrt(p-bar * (1 - p-bar) / n)
- Lower control limit: p-bar - z * sqrt(p-bar * (1 - p-bar) / n)

where z is the standard normal deviate corresponding to the desired confidence level (usually 3 for 99.73% confidence), and n is the sample size.

If the sample size varies, the control limits can be adjusted by multiplying the standard deviation term by sqrt(n-bar / n), where n-bar is the average sample size.

## np chart

An np chart is used to plot the number of defective items in a sample. It is similar to a p chart, but it reflects integer numbers rather than proportions. For example, an np chart can be used to monitor the number of defective pens in a batch of 100 pens.

The assumptions of an np chart are the same as those of a p chart.

The formula for the center line and the control limits of an np chart are:

- Center line: np-bar = n * p-bar
- Upper control limit: np-bar + z * sqrt(np-bar * (1 - p-bar))
- Lower control limit: np-bar - z * sqrt(np-bar * (1 - p-bar))

where z, n and p-bar are the same as in the p chart.

## c chart

A c chart is used to plot the number of defects in a sample. A defect is a specific flaw or nonconformity in an item. For example, a c chart can be used to monitor the number of scratches on a car surface.

The assumptions of a c chart are:

- The samples are independent and randomly selected from the process.
- The sample size or area of opportunity is constant.
- The probability of defect is the same for each item or unit of area.

The formula for the center line and the control limits of a c chart are:

- Center line: c-bar = (total number of defects in all samples) / (total number of samples)
- Upper control limit: c-bar + z * sqrt(c-bar)
- Lower control limit: c-bar - z * sqrt(c-bar)

where z is the same as in the p chart.

If the lower control limit is negative, it is set to zero.