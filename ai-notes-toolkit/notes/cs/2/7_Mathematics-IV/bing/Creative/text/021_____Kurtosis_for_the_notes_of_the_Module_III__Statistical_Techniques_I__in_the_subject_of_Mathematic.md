### Kurtosis

- Kurtosis is a measure of the **tailedness** of a distribution, i.e., how often **outliers** occur .
- Kurtosis is measured by **moments** and is given by the following formula :

    $$\beta_2 = \frac{\mu_4}{\mu_2^2}$$

    where $\mu_4$ is the **fourth central moment** and $\mu_2$ is the **second central moment** or the **variance**.

- Alternatively, kurtosis can be defined as the **fourth standardized moment**, i.e., the fourth moment divided by the fourth power of the standard deviation:

    $$\kappa = \frac{E[(X-\mu)^4]}{\sigma^4}$$

    where $E$ is the **expected value**, $\mu$ is the **mean**, and $\sigma$ is the **standard deviation**.

- Kurtosis can also be expressed as the **excess kurtosis**, which is the difference between the kurtosis and 3 :

    $$\gamma_2 = \beta_2 - 3 = \kappa - 3$$

    This is because the kurtosis of a **normal distribution** is 3, so the excess kurtosis measures the deviation from normality.

- The kurtosis of a distribution can be classified as **leptokurtic**, **mesokurtic**, or **platykurtic** :

    - **Leptokurtic** distributions have **positive excess kurtosis** and **heavy tails**, meaning that they have more outliers than a normal distribution.
    - **Mesokurtic** distributions have **zero excess kurtosis** and **medium tails**, meaning that they have the same tailedness as a normal distribution.
    - **Platykurtic** distributions have **negative excess kurtosis** and **light tails**, meaning that they have fewer outliers than a normal distribution.

- Kurtosis is useful for describing the **shape** and **risk** of a distribution. Higher kurtosis indicates a more **peaked** and **skewed** distribution, and also a higher probability of **extreme values** .