### Dynamic Time Warping for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

Dynamic Time Warping (DTW) is a technique used to measure the similarity between two time series sequences that may vary in speed. It is widely used in applications such as speech recognition, handwriting recognition, and bioinformatics.

#### How does Dynamic Time Warping work?

The DTW algorithm works by finding the optimal alignment between two time series sequences. It achieves this by warping the time axis of one sequence to match the other sequence. The algorithm aligns the two sequences by finding the path that minimizes the distance between them, while allowing for the possibility of time warping.

#### Advantages of Dynamic Time Warping

- DTW can handle time series sequences with different scales and lengths.
- DTW can handle time series sequences with variations in speed.
- DTW can handle time series sequences with missing data points.

#### Disadvantages of Dynamic Time Warping

- DTW can be computationally expensive for long time series sequences.
- DTW can be sensitive to noise and outliers in the data.

#### Mnemonics and Learning Tricks

- One way to remember the concept of DTW is to think of it as a technique that allows for "stretching" and "compressing" of time series sequences, similar to how we can stretch and compress a rubber band.
- Another way to remember DTW is to think of it as a technique that finds the "optimal path" between two time series sequences, similar to how we can find the optimal path between two locations on a map.

#### Applications of Dynamic Time Warping

- Speech recognition: DTW is used to compare spoken words to a reference database of words.
- Handwriting recognition: DTW is used to compare handwritten letters to a reference database of letters.
- Bioinformatics: DTW is used to compare DNA sequences to identify similarities and differences.

#### Example of Dynamic Time Warping

Suppose we have two time series sequences, A and B. The length of sequence A is 5 and the length of sequence B is 7. The distance between each point in the two sequences is shown in the table below.

|   | B1 | B2 | B3 | B4 | B5 | B6 | B7 |
|---|---|---|---|---|---|---|---|
| A1 | 2 | 3 | 3 | 3 | 4 | 6 | 9 |
| A2 | 4 | 5 | 5 | 5 | 6 | 8 | 11 |
| A3 | 7 | 8 | 8 | 8 | 9 | 11 | 14 |
| A4 | 9 | 10 | 10 | 10 | 10 | 12 | 15 |
| A5 | 11 | 12 | 12 | 12 | 12 | 12 | 13 |

The DTW algorithm finds the optimal path between the two sequences, which is shown in the diagram below.

```
A1 - A2 - A3 - A4 - A5
  |   |   |   |   |   |
B1 - B2 - B2 - B3 - B4 - B5 - B6 - B7
```

The total distance between the two sequences along the optimal path is 6.