### Kurtosis

- Kurtosis is a measure of the **tailedness** of a distribution, i.e., how often **outliers** occur .
- Kurtosis is measured by **moments** and is given by the following formula :

    `Kurtosis = β2 = μ4 / μ2^2`

    where `μ4` is the **fourth central moment** and `μ2` is the **second central moment** or the **variance**.

- Alternatively, kurtosis can be defined as the **fourth standardized moment**, i.e., the fourth central moment divided by the standard deviation to the fourth power:

    `Kurtosis = κ = E[(X - μ)^4] / σ^4`

    where `E` is the **expected value** of `X`, `μ` is the **mean** of `X`, and `σ` is the **standard deviation** of `X`.

- The kurtosis of a distribution can be classified as **leptokurtic**, **mesokurtic**, or **platykurtic** :

    - **Leptokurtic** distributions have **high kurtosis** (greater than 3) and **heavy tails**, meaning that they have more outliers than a normal distribution.
    - **Mesokurtic** distributions have **medium kurtosis** (equal to 3) and **moderate tails**, meaning that they have the same amount of outliers as a normal distribution.
    - **Platykurtic** distributions have **low kurtosis** (less than 3) and **thin tails**, meaning that they have fewer outliers than a normal distribution.

- Kurtosis is useful for describing the **shape** and **risk** of a distribution. Higher kurtosis indicates a more **peaked** and **asymmetric** distribution, while lower kurtosis indicates a more **flat** and **symmetric** distribution. Higher kurtosis also implies higher **probability** of extreme values and higher **sensitivity** to outliers, while lower kurtosis implies lower probability of extreme values and lower sensitivity to outliers.