Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have generated for you:

##### 5. Measurement of power in 3- phase circuit by two-wattmeter method and determination of its power factor for star as well as delta connected load.

- The two-wattmeter method is a technique for measuring the total power in a balanced or unbalanced three-phase circuit using two wattmeters.
- The principle of the method is based on the fact that the power in a three-phase circuit can be expressed as the sum of the powers in two of the three phases.
- The two wattmeters are connected as shown in the diagram below, where W1 and W2 are the readings of the wattmeters, V is the line voltage, I is the line current, and θ is the phase angle between V and I.

![Diagram of two-wattmeter method](https://i.imgur.com/6Zw7Q8w.png)

- The power in each phase can be calculated as:

  - P1 = V1I1 cos θ1 = V I cos (θ + 30°)
  - P2 = V2I2 cos θ2 = V I cos (θ - 30°)
  - P3 = V3I3 cos θ3 = V I cos θ

- The total power can be obtained by adding the powers in two phases:

  - P = P1 + P2 = V I [cos (θ + 30°) + cos (θ - 30°)]
  - P = V I [2 cos θ cos 30°]
  - P = √3 V I cos θ
  - P = W1 + W2

- The power factor can be determined by dividing the total power by the product of the line voltage and current:

  - PF = P / (√3 V I)
  - PF = (W1 + W2) / (√3 V I)

- For a star-connected load, the line voltage is equal to the phase voltage multiplied by √3, and the line current is equal to the phase current. Therefore, the power factor can be written as:

  - PF = (W1 + W2) / (3 Vph Iph)

- For a delta-connected load, the line voltage is equal to the phase voltage, and the line current is equal to the phase current multiplied by √3. Therefore, the power factor can be written as:

  - PF = (W1 + W2) / (Vph 3 Iph)

- The two-wattmeter method can be used to measure the power and power factor of any three-phase load, whether balanced or unbalanced, star or delta connected, resistive, inductive, or capacitive. However, some special cases need to be considered:

  - If the load is purely resistive, the power factor is unity, and the two wattmeters will show equal readings.
  - If the load is purely inductive or capacitive, the power factor is zero, and the two wattmeters will show opposite readings, one positive and one negative. The total power will be zero, indicating that the circuit is only consuming reactive power.
  - If the load is balanced, the phase angle θ will be the same for all phases, and the two wattmeters will show the same readings, regardless of the connection type.
  - If the load is unbalanced, the phase angle θ will vary for each phase, and the two wattmeters will show different readings, depending on the connection type. The total power will still be the sum of the two readings, but the power factor will not be the same for all phases.