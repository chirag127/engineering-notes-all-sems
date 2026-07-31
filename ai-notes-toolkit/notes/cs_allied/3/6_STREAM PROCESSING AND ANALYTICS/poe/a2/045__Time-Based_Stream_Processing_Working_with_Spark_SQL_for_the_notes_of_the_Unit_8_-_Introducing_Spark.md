 Here are the notes in markdown format:

### Time-Based Stream Processing
Working with Spark SQL for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS.

1. Time is divided into small batches ( windows)
- Micro-batch processing - processing streams as small batches
- Windows - time intervals
- Sliding windows - overlapping windows of a fixed size that slide along the time axis

2. Aggregating over windows
- Count - count the number of elements in each window
- Sum - sum of values in each window
- Average - average of values in each window
- Max/Min - find max/min value in each window

3. Joins over windows
- Join streaming data with static data (reference data) or data from another stream
- Inner, outer, left, right joins supported
- One or both inputs can be windows

4. Handling late data
- Data can arrive late due to delays
- Late data can affect results if discarded
- Options to handle late data:
-- Discard late data
-- Keep updating results for a limited time after a window closes
-- Have a "grace period" for late data and updates results if data arrives within the grace period

5. Aggregating over sessions
- A session is a series of events from the same entity
- Need to identify sessions boundaries in stream
- Window-based approaches can be inefficient for sessionization
- Other approaches:
-- Gap detection: detect gaps between events and start a new session after a gap
-- Timeout-based: start a new session if no event received for a timeout duration