Hello, I am Sydney, your AI assistant. I can help you with your topic of three phase balanced circuits. Here are some notes that you can use for your study material:

### Three phase balanced circuits

- A three phase balanced circuit is a type of alternating current (AC) power system that consists of three voltage sources and three loads connected in either star (Y) or delta (Δ) configuration.
- In a balanced system, each of the three instantaneous voltages have equal amplitudes but are separated from the other voltages by a phase angle of 120°. The three voltages (or phases) are typically labeled a, b and c .
- The advantages of using a three phase balanced circuit over a single phase circuit are:
  - Higher power transfer capability
  - Higher efficiency
  - Smoother torque output for motors
  - Less conductor material required
- The analysis of a three phase balanced circuit can be simplified by using the following steps :
  - Choose a reference phase, usually phase a, and draw the corresponding single phase equivalent circuit
  - Apply Kirchhoff's laws or other methods to solve for the voltage and current in the reference phase
  - Use the phase relationships to find the voltage and current in the other phases
  - Use the power formula to find the total power delivered or consumed by the circuit
- The power formula for a three phase balanced circuit is :
  - P = √3 V L I L cos θ
  - Where P is the total power, V L is the line voltage, I L is the line current, and θ is the power factor angle
  - The power factor angle is the angle between the voltage and current phasors of the reference phase
  - The power factor is the cosine of the power factor angle and indicates how efficiently the circuit uses the power
  - The power factor can be improved by adding capacitors or inductors to the circuit to cancel out the reactive power
- The following diagram shows an example of a three phase balanced circuit with a star-connected load:

```markdown
    a
    |
    V
    R
    |
    o-----o
   / \   / \
  /   \ /   \
 /     X     \
V      |      V
R      |      R
|      |      |
o------o------o
|      |      |
|      V      |
|      R      |
|      |      |
o------o------o
|      |      |
b      c      n
```
- The diagram shows the phase voltages V a , V b , and V c , the line voltages V ab , V bc , and V ca , the phase currents I a , I b , and I c , the line currents I ab , I bc , and I ca , and the neutral current I n .
- The following relationships hold for a star-connected load :
  - V L = √3 V p
  - I L = I p
  - I n = 0
  - Where V L is the line voltage, V p is the phase voltage, I L is the line current, I p is the phase current, and I n is the neutral current
- The following diagram shows an example of a three phase balanced circuit with a delta-connected load:

```markdown
    a
    |
    V
    R
    |
    o-----o
   / \   / \
  /   \ /   \
 /     X     \
V      |      V
R      |      R
|      |      |
o------o------o
|      |      |
|      V      |
|      R      |
|      |      |
o------o------o
|      |      |
b      c      n
```
- The diagram shows the phase voltages V ab , V bc , and V ca , the line voltages V a , V b , and V c , the phase currents I ab , I bc , and I ca , the line currents I a , I b , and I c , and the neutral current I n .
- The following relationships hold for a delta-connected load :
  - V L = V p
  - I L = √3 I p
  - I n = 0
  - Where V L is the line voltage