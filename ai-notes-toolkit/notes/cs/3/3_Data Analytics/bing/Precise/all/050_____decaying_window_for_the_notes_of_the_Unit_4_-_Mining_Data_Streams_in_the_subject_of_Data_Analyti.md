### Decaying Window - Mining Data Streams

- In the context of mining data streams, a decaying window is a technique used to give more importance to recent data while still taking into account older data.
- This is in contrast to a sliding window, which only considers the most recent data within a fixed time frame.
- One common implementation of a decaying window is the exponentially decaying window.
- If a stream consists of elements a1, a2, ..., at, where a1 is the first element to arrive and at is the current element, we can define the exponentially decaying window for this stream to be the sum Σi = 1,2,…,t ai * e^(-c * (t-i)), where c is a small constant such as 10^(-6) or 10^(-9) .
- This formula gives more weight to recent elements while still taking into account older elements, with the weight of older elements decreasing exponentially over time.
- Decaying windows can be useful in various applications, such as counting items or computing the characteristic function of each possible item in a stream .