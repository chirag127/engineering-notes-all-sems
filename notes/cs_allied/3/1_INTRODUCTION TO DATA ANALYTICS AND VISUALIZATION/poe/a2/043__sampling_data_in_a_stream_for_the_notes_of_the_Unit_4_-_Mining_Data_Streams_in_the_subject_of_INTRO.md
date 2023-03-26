 Here are the notes on sampling data in a stream for Unit 4 - Mining Data Streams:

### Sampling Data in a Stream

- Stream data arrives continuously and rapidly. It is not feasible to store and process all the data. Sampling is required to analyze stream data.
- Reservoir sampling: Randomly sample k data points from the stream as they arrive. Replace each sampled point with a new incoming point with a decreasing probability as more points are sampled. This produces a random sample of k points from the entire stream.
- Sketching: Construct a compact summary (sketch) of the data using random projections. The sketch can be used to estimate certain properties (e.g. frequent items) of the data. The accuracy of the estimations depends on the size of the sketch.
- Sliding windows: Use a window of recent data points sliding over the stream to analyze local patterns. The window size needs to be carefully chosen based on how fast the stream changes.
- Stratified sampling: Partition the stream into strata (e.g. bursts/non-bursts) and sample each stratum separately to capture the characteristics of different regimes in the stream.

The techniques need to be evaluated based on:

- Bias: How close the estimates are to the actual values.
- Variance: The variability of the estimates. Lower variance leads to more stable results.
- Space and time efficiency: The sample/sketch size and processing time should be small relative to the stream size and speed.

The appropriate technique depends on the analysis task and stream characteristics. Multiple techniques can also be combined to get better results.