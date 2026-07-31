### Dynamic Time Warping for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Dynamic Time Warping (DTW) is an algorithm for measuring the similarity between two temporal sequences, such as speech signals, that may vary in speed or length  .
- DTW is based on the idea of finding the optimal alignment between two sequences by minimizing the distance between them .
- DTW can handle non-linear distortions and local variations in the sequences, such as different pronunciations, accents, or speaking rates  .
- DTW works by constructing a matrix that represents the pairwise distances between the elements of the two sequences, and then finding the shortest path through the matrix that satisfies some constraints .
- The constraints are: 
  - The path must start at the top-left corner and end at the bottom-right corner of the matrix .
  - The path must be monotonically increasing, meaning that it can only move right, down, or diagonally .
  - The path must be continuous, meaning that it cannot skip any cells in the matrix .
- The length of the path is the DTW distance between the two sequences, and the path itself is the optimal alignment .
- DTW can be used for various applications, such as speech recognition, speaker identification, gesture recognition, data mining, financial markets, etc   .
- DTW has some limitations, such as high computational complexity, sensitivity to noise, and lack of global constraints  .
- DTW can be improved by using different distance measures, pruning techniques, warping constraints, or dimensionality reduction methods  .