### Counting Distinct Elements in a Stream

- A stream is a sequence of data items that arrive in an online fashion, i.e., one by one and cannot be stored or revisited.
- Counting the number of distinct elements in a stream is a fundamental problem in data stream mining, with applications in network monitoring, web analytics, database query optimization, etc.
- The challenge is to design algorithms that use limited memory and processing time, and can handle streams of arbitrary length and distribution.
- There are two main approaches to solve this problem: sketching and sampling.
- Sketching is a technique that uses a compact data structure, called a sketch, to store a summary of the stream that can be used to estimate the number of distinct elements with some error bound.
- Sampling is a technique that randomly selects a subset of the stream elements, called a sample, and uses it to infer the number of distinct elements in the whole stream with some confidence interval.
- Some examples of sketching algorithms are Flajolet-Martin algorithm, HyperLogLog algorithm, Count-Min sketch, etc.
- Some examples of sampling algorithms are reservoir sampling, min-wise independent permutations, etc.