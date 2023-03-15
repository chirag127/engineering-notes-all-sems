### Kurtosis

- Kurtosis is a measure of the **tailedness** of a distribution, i.e., how often **outliers** occur .
- Kurtosis is measured by **moments** and is given by the following formula :

    `Kurtosis = β2 = μ4 / μ2^2`

    where `μ4` is the **fourth central moment** and `μ2` is the **second central moment** or the **variance**.

- Alternatively, kurtosis can be defined as :

    `Kurtosis = β2 = E(x^4) / E(x^2)^2 - 3`

    where `E` is the **expected value** of `x`.

- The kurtosis of a distribution can be classified as **leptokurtic**, **mesokurtic**, or **platykurtic** .
    - **Leptokurtic** distributions have **positive kurtosis**, meaning they have **heavy tails** and a **peaked center**. They are more likely to produce outliers than a normal distribution.
    - **Mesokurtic** distributions have **zero kurtosis**, meaning they have the same tailedness as a normal distribution. They are also called **normal kurtic** distributions.
    - **Platykurtic** distributions have **negative kurtosis**, meaning they have **light tails** and a **flat center**. They are less likely to produce outliers than a normal distribution.

- Kurtosis is useful for describing the **shape** and **risk** of a distribution. Distributions with high kurtosis are more prone to **extreme values** and **volatility** than distributions with low kurtosis.