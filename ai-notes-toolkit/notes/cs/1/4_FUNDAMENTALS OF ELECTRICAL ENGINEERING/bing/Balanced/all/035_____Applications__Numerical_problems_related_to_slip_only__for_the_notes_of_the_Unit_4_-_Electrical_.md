# Applications (Numerical problems related to slip only)

Slip is the difference between the synchronous speed and the actual speed of an induction motor. It is expressed as a percentage or a fraction of the synchronous speed. Slip is an important parameter that affects the torque, power, efficiency, and speed regulation of an induction motor. Slip can be calculated using the following formula:

$$
s = \frac{n_s - n_r}{n_s}
$$

where $s$ is the slip, $n_s$ is the synchronous speed, and $n_r$ is the rotor speed.

Some numerical problems related to slip are:

- A three-phase induction motor has a synchronous speed of 1200 rpm and a full-load speed of 1140 rpm. Find the slip and the frequency of the rotor current at full load.

  - Solution: The slip is given by:

    $$
    s = \frac{n_s - n_r}{n_s} = \frac{1200 - 1140}{1200} = 0.05
    $$

    The frequency of the rotor current is given by:

    $$
    f_r = s f_s = 0.05 \times 60 = 3 \text{ Hz}
    $$

    where $f_s$ is the frequency of the stator current, which is 60 Hz in this case.

- A four-pole induction motor is connected to a 50 Hz supply. The rotor resistance per phase is 0.2 ohm and the rotor reactance per phase at standstill is 2 ohm. Find the slip and the torque at standstill.

  - Solution: The synchronous speed is given by:

    $$
    n_s = \frac{120 f_s}{p} = \frac{120 \times 50}{4} = 1500 \text{ rpm}
    $$

    where $p$ is the number of poles.

    The slip at standstill is 1, since the rotor speed is zero.

    The torque at standstill is given by:

    $$
    T = \frac{3 s V_r^2 R_r}{(R_r + s X_r)^2 + (s X_r)^2}
    $$

    where $V_r$ is the rotor induced voltage per phase, $R_r$ is the rotor resistance per phase, and $X_r$ is the rotor reactance per phase.

    Since the rotor induced voltage is proportional to the slip, we can write:

    $$
    V_r = s V_s
    $$

    where $V_s$ is the stator applied voltage per phase.

    Substituting the values, we get:

    $$
    T = \frac{3 \times 1 \times (1 V_s)^2 \times 0.2}{(0.2 + 1 \times 2)^2 + (1 \times 2)^2} = \frac{0.6 V_s^2}{8.8} = 0.068 V_s^2 \text{ Nm}
    $$

    Note that the torque is independent of the frequency and the number of poles.