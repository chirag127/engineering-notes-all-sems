 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Window Aggregations for the notes of the Unit 2 - Stream-Processing Model

1. Tumbling window: A tumbling window is a fixed-sized, non-overlapping window. Tuples are assigned to windows based on the timestamp of the tuple. For example, with a tumbling window of 5 minutes, tuples with timestamps at 10:07, 10:12, and 10:15 would all be in the window from 10:05 to 10:10.
2. Sliding window: A sliding window is a fixed-sized, overlapping window. Tuples are assigned to multiple windows based on the timestamp of the tuple and the size/slide interval of the window. For example, with a window size of 5 minutes and a slide interval of 1 minute, tuples with timestamps at 10:07, 10:08, and 10:09 would all be in the windows from 10:05 to 10:10, 10:06 to 10:11, and 10:07 to 10:12.
3. Session window: A session window groups tuples based on sessions. Sessions are defined by a gap duration - if tuples arrive with a gap less than the defined gap duration, they are considered part of the same session. For example, with a gap duration of 30 minutes, tuples with timestamps at 10:05, 10:07, and 10:20 would be in the same session, but the tuple at 11:05 would start a new session.

The aggregations can be applied on the tuples within a window to calculate metrics like counts, sums, averages, maximums, and minimums on the values of the tuples within the window.