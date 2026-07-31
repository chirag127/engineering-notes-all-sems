### Approximation of errors

- In engineering and science, we often deal with quantities that are subject to measurement errors or uncertainties.
- For example, the length of a rod may be measured as 10 cm, but the actual value may be slightly more or less than that, depending on the accuracy of the measuring device and the human error.
- We can express the measurement error as a range of possible values, such as 10 ± 0.1 cm, which means that the true value of the length is somewhere between 9.9 and 10.1 cm.
- Similarly, the value of a physical constant, such as the gravitational acceleration g, may be given as 9.81 ± 0.02 m/s^2, which means that the true value of g is somewhere between 9.79 and 9.83 m/s^2.
- When we perform calculations with quantities that have measurement errors, we need to estimate how the errors propagate and affect the final result.
- For example, if we want to calculate the area of a rectangle with length 10 ± 0.1 cm and width 5 ± 0.05 cm, we need to find the range of possible values for the area, taking into account the errors in the length and width.
- One way to do this is to use the **maximum error** or **absolute error** of each quantity, which is the maximum possible deviation from the true value.
- For example, the maximum error of the length is 0.1 cm, and the maximum error of the width is 0.05 cm.
- Then, we can use the following formula to find the maximum error of the area:

  - Maximum error of area = (maximum error of length) × (width) + (length) × (maximum error of width)

  - Maximum error of area = (0.1 cm) × (5 cm) + (10 cm) × (0.05 cm)

  - Maximum error of area = 0.75 cm^2

- This means that the true value of the area is somewhere between 49.25 and 50.75 cm^2, or 50 ± 0.75 cm^2.
- Another way to do this is to use the **relative error** or **percentage error** of each quantity, which is the ratio of the maximum error to the measured value, expressed as a percentage.
- For example, the relative error of the length is 0.1/10 = 0.01, or 1%, and the relative error of the width is 0.05/5 = 0.01, or 1%.
- Then, we can use the following formula to find the relative error of the area:

  - Relative error of area = (relative error of length) + (relative error of width)

  - Relative error of area = 0.01 + 0.01

  - Relative error of area = 0.02, or 2%

- This means that the true value of the area is within 2% of the measured value, or 50 × (1 ± 0.02) cm^2, or 49 to 51 cm^2.
- Note that the maximum error and the relative error are different ways of expressing the same uncertainty, and they are related by the following formula:

  - Maximum error = (relative error) × (measured value)

  - 0.75 cm^2 = 0.02 × 50 cm^2

- In general, the relative error is more useful when comparing the accuracy of different measurements, while the maximum error is more useful when finding the range of possible values for a calculation.