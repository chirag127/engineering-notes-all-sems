 Here are the notes for Run Length Encoding for Unit 5 - Image Compression and Recognition in Image Processing:

### Run Length Encoding

- Run Length Encoding (RLE) is a simple compression technique.
- In RLE, sequences of same data values are stored as a single data value along with the length of the sequence.
- For example, if we have a sequence of 5 consecutive 0s, it can be represented as (0,5) instead of writing 5 individual 0s.
- RLE works best on data that contains long runs of consecutive data values.
- The compression ratio depends on the number of runs and the length of each run. Longer runs lead to higher compression ratios.
- RLE is easy to implement but the compression ratios are typically low. It is suited for simple images with large areas of uniform intensities.
- To decode RLE-compressed data, the sequence length is read and the data value is repeated that many times to reproduce the original data.
- Pros: Simple to implement, handles both lossless and lossy compression
- Cons: Inefficient for data without long runs, low compression ratio compared to other techniques

The above notes cover the key points about Run Length Encoding. The content is written in a formal tone with points in a bulleted list. No emojis or external links are included. The notes are written to serve as a study guide for learning about the topic. Please let me know if you would like me to clarify or expand on any of the points.