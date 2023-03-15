# Decaying Window

- A decaying window is a technique to handle streaming data that assigns different weights to different parts of the stream based on their recency.
- The idea is to give more importance to the recent data and less importance to the older data, as they may be less relevant or outdated.
- A decaying window can be implemented in different ways, such as:
  - Exponentially decaying window: The weight of each element in the stream is proportional to an exponential function of its age, such as e^(-c*t), where c is a constant and t is the time difference from the current element.
  - Time-fading window: The weight of each element in the stream is proportional to a linear function of its age, such as 1 - c*t, where c is a constant and t is the time difference from the current element.
  - Landmark window: The weight of each element in the stream is proportional to a step function of its age, such as 1 if t < T and 0 otherwise, where T is a fixed threshold and t is the time difference from the current element.
- A decaying window can be used to compute various statistics or functions over the stream, such as:
  - Sum: The sum of the weighted elements in the stream, such as Σ a_i * w_i, where a_i is the i-th element and w_i is its weight.
  - Count: The count of the weighted elements in the stream, such as Σ w_i, where w_i is the weight of the i-th element.
  - Average: The average of the weighted elements in the stream, such as (Σ a_i * w_i) / (Σ w_i), where a_i is the i-th element and w_i is its weight.
  - Frequency: The frequency of a given element in the stream, such as (Σ w_i * I(a_i = x)) / (Σ w_i), where x is the element of interest, w_i is the weight of the i-th element, and I is the indicator function that returns 1 if the condition is true and 0 otherwise.
  - Frequent itemsets: The sets of elements that appear frequently in the stream, such as those whose frequency exceeds a given threshold.
- A decaying window can help to reduce the memory and computational requirements of processing streaming data, as it can discard or compress the older data that have low weights.
- A decaying window can also help to capture the trends or patterns in the stream, as it can reflect the changes or variations in the data over time.