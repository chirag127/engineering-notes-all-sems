### Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for transmitting and storing scanned documents, such as faxes.
- Facsimile encoding exploits the fact that most scanned documents have large areas of white or black pixels, and uses run-length encoding to represent the number of consecutive pixels of the same color  .
- Run-length encoding assigns a variable-length code to each run of pixels, depending on its length and color. For example, a run of 10 white pixels could be encoded as 00001010, and a run of 5 black pixels could be encoded as 11111001.
- Facsimile encoding can achieve high compression ratios for documents that have a lot of white space or simple patterns, such as text or line drawings .
- Facsimile encoding can also use adaptive models to adjust the code lengths based on the statistics of the data, such as the frequency of runs of different lengths and colors .
- Facsimile encoding can be combined with other modulation methods, such as amplitude and phase modulation, to transmit the compressed data over a communication channel.
- Facsimile encoding is standardized by the International Telecommunication Union (ITU) in various recommendations, such as T.4, T.6, and T.82 .