# Differential and Common-Mode Operation of Op-Amp

- An op-amp is a differential amplifier that can amplify the difference between two input signals.
- The input signals can be classified into two modes: common-mode and differential-mode.
- Common-mode signals are the signals that are the same for both inputs, while differential-mode signals are the signals that are different for both inputs.
- For example, if the input signals are V1 and V2, then the common-mode signal is (V1 + V2) / 2 and the differential-mode signal is (V1 - V2) / 2.
- The op-amp ideally amplifies only the differential-mode signal and rejects the common-mode signal. This is because the op-amp has a high common-mode rejection ratio (CMRR), which is the ratio of the differential-mode gain to the common-mode gain.
- The common-mode gain is the gain of the op-amp when both inputs are connected to the same signal, while the differential-mode gain is the gain of the op-amp when the inputs are connected to different signals.
- The common-mode gain is usually very small compared to the differential-mode gain, so the CMRR is very large, typically in the order of 10^5 or more.
- The common-mode signal can cause interference or noise in the op-amp output, especially if the input signals are not well balanced or matched. Therefore, it is desirable to minimize the common-mode signal and maximize the differential-mode signal for better performance and accuracy of the op-amp.
- The common-mode and differential-mode signals can be represented by the following equations:

  - Vcm = (V1 + V2) / 2
  - Vd = (V1 - V2) / 2
  - Vout = Ad * Vd + Ac * Vcm
  - where Ad is the differential-mode gain, Ac is the common-mode gain, Vcm is the common-mode signal, Vd is the differential-mode signal, and Vout is the output signal of the op-amp.
- The common-mode and differential-mode signals can also be represented by the following diagram:

  ![Diagram of common-mode and differential-mode signals](https://resources.system-analysis.cadence.com/blog/msa2021-understanding-common-mode-vs-differential-mode-signals/fig1.png)

  - Figure 1: Diagram of common-mode and differential-mode signals