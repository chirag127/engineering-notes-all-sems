 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Tree structured Vector Quantizers for the notes of the Unit 5 - Advantages of Vector Quantization over Scalar Quantization in the subject of Data Compression

- Vector Quantization (VQ) involves mapping k-dimensional input vectors onto a finite set of output vectors called codevectors. Scalar Quantization (SQ) maps each scalar input to the nearest reproduction scalar level.
- VQ has the following advantages over SQ:
-- Higher compression ratios: VQ can achieve higher compression ratios than SQ as it utilizes correlation between components of the input vector. SQ does not exploit this correlation.
-- Ability to reconstruct the input: The decoded output of VQ is one of the codevectors which is used to reconstruct the input. In SQ, the decoded output is a reproduction scalar level which does not retain the input structure.
-- Robustness to channel errors: VQ is more robust to channel errors as corruption of a single component of the codevector can be corrected using the correlation between components. This is not possible in SQ.
- Tree-structured VQ (TSVQ) is a variant of VQ that uses a tree-structured codebook. The tree is traversed top-down to find the best matching codevector. TSVQ gives faster encoding and decoding and provides a hierarchical representation of the input.
- The key advantages of TSVQ over regular VQ are:
-- Faster search due to tree structure
-- Easy scalability by increasing depth of the tree
-- Progressive transmission by truncating the tree
-- Embedded quantization with varying bit rates