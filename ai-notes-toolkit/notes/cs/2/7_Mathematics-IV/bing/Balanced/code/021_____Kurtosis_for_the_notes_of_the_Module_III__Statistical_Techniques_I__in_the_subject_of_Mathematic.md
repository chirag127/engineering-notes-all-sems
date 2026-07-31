### Kurtosis

- Kurtosis is a measure of the **tailedness** of a distribution, i.e., how often **outliers** occur.
- Kurtosis is measured by **moments** and is given by the following formula:

```
β2 = μ4 / μ2^2
```

where `μ4` is the **fourth central moment** and `μ2` is the **second central moment** or the **variance**.

- Alternatively, kurtosis can be defined as:

```
β2 = E(x^4) / E(x^2)^2 - 3
```

where `E` is the **expected value** of `x`.

- The kurtosis of a distribution can be classified as **leptokurtic**, **mesokurtic**, or **platykurtic**.
  - **Leptokurtic** distributions have **positive kurtosis**, meaning they have **heavy tails** and a **peaked center**. They are more likely to produce outliers than a normal distribution.
  - **Mesokurtic** distributions have **zero kurtosis**, meaning they have the same tailedness as a normal distribution. They are also called **normal kurtic** distributions.
  - **Platykurtic** distributions have **negative kurtosis**, meaning they have **light tails** and a **flat center**. They are less likely to produce outliers than a normal distribution.

- Kurtosis is often confused with **skewness**, which is a measure of the **asymmetry** of a distribution. However, kurtosis does not imply anything about the shape of the distribution, only its tailedness.
- Kurtosis is useful for describing the **risk** of a distribution, as higher kurtosis implies higher probability of extreme values. It is also used in **hypothesis testing** to compare the kurtosis of a sample distribution with that of a theoretical distribution.