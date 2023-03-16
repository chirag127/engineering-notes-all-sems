# Decaying Window

- A decaying window is a technique for processing data streams that assigns different weights to different parts of the stream based on their recency.
- The idea is to give more importance to the recent data and less importance to the older data, as they may be less relevant or outdated.
- A decaying window can be implemented in different ways, such as using exponential decay, time-fading, or landmark windows.
- A decaying window can be useful for finding frequent itemsets, outliers, trends, or patterns in streaming data, as it can adapt to the changing characteristics of the data over time.

## Exponential Decay

- One way to implement a decaying window is to use an exponential decay function, which reduces the weight of each element in the stream by a constant factor as it gets older.
- For example, if the stream consists of elements a1, a2, ..., at, where a1 is the first element to arrive and at is the current element, and c is a small constant, such as 10^-6 or 10^-9, then the weight of each element ai is given by e^(-c(t-i)).
- The advantage of this method is that it does not require a fixed window size or a sliding mechanism, as the weight of each element decays continuously over time.
- The disadvantage is that it may be difficult to choose an appropriate value for c, as it affects the rate of decay and the sensitivity to recent changes.

## Time-Fading

- Another way to implement a decaying window is to use a time-fading function, which reduces the weight of each element in the stream by a certain threshold after a certain time interval.
- For example, if the stream consists of elements a1, a2, ..., at, where a1 is the first element to arrive and at is the current element, and T is a time interval, such as one hour or one day, then the weight of each element ai is given by 1 if it arrived within the last T time units, and 0 otherwise.
- The advantage of this method is that it is easy to implement and understand, as it only requires a simple comparison of timestamps.
- The disadvantage is that it may be too abrupt or coarse, as it ignores the gradual changes in the data and discards the older data completely.

## Landmark

- A third way to implement a decaying window is to use a landmark window, which divides the stream into segments based on certain events or markers, and assigns different weights to different segments based on their distance from the current segment.
- For example, if the stream consists of elements a1, a2, ..., at, where a1 is the first element to arrive and at is the current element, and L is a landmark, such as the start of a day or a week, then the weight of each element ai is given by 1 if it belongs to the current segment, and 0.5^k if it belongs to the k-th previous segment.
- The advantage of this method is that it can capture the periodicity or seasonality of the data, as it aligns the segments with the natural cycles of the data.
- The disadvantage is that it may be sensitive to the choice of the landmark, as it affects the length and number of the segments.