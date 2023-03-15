### Kurtosis

- Kurtosis is a measure of the **tailedness** of a distribution . Tailedness is how often **outliers** occur.
- Kurtosis is measured by **moments** and is given by the following formula :

```
β2 = μ4 / μ2^2
```

where `μ4` is the **fourth central moment** and `μ2` is the **second central moment** or the **variance** .

- Kurtosis can also be defined as `β2 = (E(x^4) / (E(x^2)^2)) − 3`, where `E` is the **expected value** of `x`.
- The kurtosis of a distribution can be classified as **leptokurtic**, **mesokurtic**, or **platykurtic**  .
  - **Leptokurtic** distributions are variable distributions with **wide tails** and have **positive kurtosis**  . They have more frequent outliers than a normal distribution.
  - **Mesokurtic** distributions are distributions with **medium tails** and have **zero kurtosis**  . They have the same tailedness as a normal distribution.
  - **Platykurtic** distributions are distributions with **thin tails** and have **negative kurtosis**  . They have fewer outliers than a normal distribution.
- Kurtosis is sometimes called **excess kurtosis**, which is the tailedness of a distribution relative to a normal distribution. Excess kurtosis is calculated by subtracting 3 from the kurtosis  .
- Kurtosis is useful for describing the **shape** and **risk** of a distribution . Higher kurtosis indicates more **peakedness** and **heavy tails**, which implies higher probability of extreme values and higher risk . Lower kurtosis indicates more **flatness** and **light tails**, which implies lower probability of extreme values and lower risk .