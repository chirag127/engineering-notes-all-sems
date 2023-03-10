 Here is the content in markdown format for the given topic:

### Physical models for the notes of the Unit 1 - Compression Techniques

1.  Source coding theorem - According to source coding theorem, to compress data without losing information, the compression algorithm must exploit redundancy in the data. The compression ratio cannot be less than the entropy of the source. This forms the fundamental limit on lossless data compression.
2.  Statistical modeling - The compression algorithm models the statistical properties of the input data and encodes the data based on the model. For example, if the input data has a biased probability distribution, the more probable symbols are encoded using fewer bits than the less probable symbols. entropy coding is a common technique used.
3.  Predictive coding - The algorithm uses the previous inputs to predict the upcoming input and then encodes the error between the predicted and actual input. If the prediction is good, the error is small and requires fewer bits to encode. Example techniques using predictive coding are differential pulse code modulation for audio and video signals.
4.  Dictionary coding - The input data is compared with a dictionary of sample inputs and indices/pointers to the dictionary inputs that match are encoded instead of the actual input data. The dictionary is built based on the statistical properties of the input data. Example techniques are LZW coding for file compression.

Advantages - Achieves high compression ratios for data with redundancy.
Disadvantages - Lossless compression may not achieve very high compression ratios. Complex algorithms and modelling may be required for good compression.
Applications - Image, audio and video compression, file archiving, communication over bandwidth-limited channels.

Detailed diagrams and examples can be added if required. The content can be modified as needed to suit the learning requirements. Let me know if you would like me to elaborate on any of the points or add/modify any part of the content.