Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

##### 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The principle of the method is based on the fact that the power in a three-phase circuit can be expressed as the sum of the powers in two of the three phases.
- The two wattmeters are connected as shown in the following diagrams for star and delta connected loads respectively.

![star](https://i.imgur.com/8JZ6a0R.png)

![delta](https://i.imgur.com/0Z0k0Za.png)

- The readings of the two wattmeters are given by:

  - W1 = V1I1 cos(θ1 - φ1) = VphIph cos(θ - φ)
  - W2 = V2I2 cos(θ2 - φ2) = VphIph cos(θ + φ)

  where Vph and Iph are the phase voltage and current, θ is the phase angle between the line voltage and current, φ is the phase angle between the two line voltages, and θ1, θ2, φ1, φ2 are the angles shown in the diagrams.

- The total power in the circuit is given by:

  - P = W1 + W2 = VphIph cos(θ - φ) + VphIph cos(θ + φ)
  - P = 2VphIph cos(θ) cos(φ)

- The power factor of the circuit is given by:

  - PF = P / (3VphIph) = cos(θ) cos(φ) / √3

- For a balanced load, φ = 0 or 180°, and the power factor is given by:

  - PF = cos(θ) / √3

- For an unbalanced load, φ can have any value, and the power factor can be calculated by:

  - PF = (W1 + W2) / (√3 VLL IL) = (W1 + W2) / (√3 Vph Iph √3) = (W1 + W2) / (3VphIph)

  where VLL and IL are the line voltage and current.

- Alternatively, the power factor can be calculated by using the following formula:

  - PF = √[(W1 + W2)² - (W1 - W2)² cos(2φ)] / (W1 + W2)

  where φ is the phase angle between the two line voltages, which can be determined by:

  - tan(φ) = (W1 - W2) / (√3 W1W2)

- The two-wattmeter method can be used for both star and delta connected loads, but the connections of the wattmeters and the calculations of the power factor are different for each case.