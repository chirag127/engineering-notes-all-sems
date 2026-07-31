# Measures of Central Tendency

Measures of central tendency are summary statistics that attempt to describe a whole set of data with a single value that represents the middle or centre of its distribution. They are also known as measures of centre or averages. There are three main measures of central tendency: the mean, the median, and the mode    .

- **Mean (Average)**: Represents the sum of all values in a dataset divided by the total number of the values. It is calculated by the formula:

  `mean = (sum of all values) / (number of values)`

  For example, the mean of the dataset {2, 4, 6, 8, 10} is:

  `mean = (2 + 4 + 6 + 8 + 10) / 5 = 6`

  The mean is sensitive to outliers, which are extreme values that are much higher or lower than the rest of the data. Outliers can skew the mean and make it less representative of the central tendency of the data.

- **Median**: The middle value in a dataset that is arranged in ascending order (from the smallest value to the largest value). If the dataset has an odd number of values, the median is the value that splits the dataset in half. If the dataset has an even number of values, the median is the average of the two middle values. It is calculated by the following steps:

  1. Sort the dataset in ascending order.
  2. Find the position of the middle value using the formula:

     `position = (number of values + 1) / 2`

  3. If the position is a whole number, the median is the value at that position. If the position is a fraction, the median is the average of the values at the positions above and below the fraction.

  For example, the median of the dataset {2, 4, 6, 8, 10} is:

  1. The dataset is already sorted in ascending order.
  2. The position of the middle value is:

     `position = (5 + 1) / 2 = 3`

  3. The position is a whole number, so the median is the value at the third position, which is 6.

  The median of the dataset {1, 3, 5, 7, 9, 11} is:

  1. The dataset is already sorted in ascending order.
  2. The position of the middle value is:

     `position = (6 + 1) / 2 = 3.5`

  3. The position is a fraction, so the median is the average of the values at the third and fourth positions, which are 5 and 7. The average of 5 and 7 is 6.

  The median is less sensitive to outliers than the mean, and it can better represent the central tendency of a skewed dataset.

- **Mode**: Defines the most frequently occurring value in a dataset. It is calculated by counting the frequency of each value in the dataset and finding the value with the highest frequency. For example, the mode of the dataset {2, 4, 4, 6, 8, 10} is 4, because it occurs twice and no other value occurs more than once. A dataset can have more than one mode if two or more values have the same highest frequency. For example, the dataset {2, 4, 4, 6, 6, 8, 10} has two modes: 4 and 6. A dataset can also have no mode if all values have the same frequency. For example, the dataset {2, 4, 6, 8, 10} has no mode, because each value occurs once. The mode is not affected by outliers, and it can represent the central tendency of a categorical or nominal dataset.