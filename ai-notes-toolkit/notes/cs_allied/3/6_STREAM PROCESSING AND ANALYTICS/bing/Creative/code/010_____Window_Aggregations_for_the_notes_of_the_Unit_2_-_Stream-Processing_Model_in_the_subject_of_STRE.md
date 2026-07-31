### Window Aggregations

- Window aggregation is a core operation in data stream processing that computes summary statistics over a sliding or fixed window of events  .
- Window aggregation can be used for various purposes, such as anomaly detection, trend analysis, or monitoring  .
- Window aggregation can be challenging due to complex window types, aggregation functions, concurrent queries, and out-of-order events .
- Window types can be classified into tumbling, sliding, or session windows, depending on how the window boundaries are defined .
  - Tumbling windows have fixed size and non-overlapping intervals, such as every 10 minutes or every hour .
  - Sliding windows have fixed size and overlapping intervals, such as every 10 minutes with a slide of 1 minute or every hour with a slide of 15 minutes .
  - Session windows have variable size and non-overlapping intervals, based on the activity or inactivity of the events, such as a window for each user session .
- Aggregation functions can be classified into algebraic, holistic, or approximate, depending on how they can be computed .
  - Algebraic functions can be computed by combining partial aggregates, such as sum, count, min, max, or average .
  - Holistic functions cannot be computed by combining partial aggregates, such as median, mode, or top-k .
  - Approximate functions can be computed by using probabilistic data structures, such as sketches, histograms, or samples, to trade accuracy for efficiency .
- Concurrent queries can be handled by sharing partial aggregates among windows, to avoid redundant computations and save memory .
- Out-of-order events can be handled by using event-time windows, which are based on the timestamps of the events, rather than the arrival time of the events .
  - Event-time windows require watermarking, which is a mechanism to specify how late the events can be and how long the system should wait for late events before dropping them.
  - Event-time windows can also be updated by using triggers, which are conditions to specify when the window results should be outputted.