# Fuzzy to Crisp Conversion

- Fuzzy to crisp conversion, also known as **defuzzification**, is the process of transforming a fuzzy set into a single crisp value that represents the best decision or action based on the fuzzy set .
- Fuzzy to crisp conversion is necessary because some applications require a precise output that can be understood and executed by a controller or a human .
- Fuzzy to crisp conversion can be done by various methods, such as:
  - **Center of gravity (COG)**: This method calculates the weighted average of the numeric values that correspond to the membership degrees of the fuzzy set. It is the most common and widely used method of defuzzification .
  - **Center of sums (COS)**: This method calculates the ratio of the sum of the products of the numeric values and the membership degrees to the sum of the membership degrees. It is similar to COG, but it gives more weight to the higher membership degrees .
  - **Center of maxima (COM)**: This method calculates the average of the numeric values that have the maximum membership degree in the fuzzy set. It is also known as the mean of maxima or the height method .
  - **Bisector of area (BOA)**: This method finds the numeric value that divides the area under the membership function of the fuzzy set into two equal parts. It is also known as the median method .
  - **Smallest of maxima (SOM)**: This method finds the smallest numeric value that has the maximum membership degree in the fuzzy set. It is also known as the minimum of maxima or the leftmost maximum method .
  - **Largest of maxima (LOM)**: This method finds the largest numeric value that has the maximum membership degree in the fuzzy set. It is also known as the maximum of maxima or the rightmost maximum method .
- The choice of the defuzzification method depends on the characteristics and requirements of the application, such as the shape of the membership function, the number of fuzzy sets, the desired accuracy, the computational complexity, and the interpretability .