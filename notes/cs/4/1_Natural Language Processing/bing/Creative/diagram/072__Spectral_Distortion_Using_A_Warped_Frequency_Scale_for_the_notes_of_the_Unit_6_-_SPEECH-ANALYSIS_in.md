The following diagram illustrates the basic architecture of a spectral warping network that modifies a signal in such a way that the frequency spectrum is stretched or compressed from the original. The network consists of a cascade of first-order all-pass filters, each with a complex coefficient a that determines the amount and direction of frequency warping. The frequency distortion function D(w) shows how the input frequency w is mapped to the output frequency w' for different values of a. A positive a causes a compression of the low frequencies and a stretching of the high frequencies, while a negative a causes the opposite effect. The diagram is drawn using ASCII characters.

```
    +-----+     +-----+     +-----+     +-----+
    |  a  |     |  a  |     |  a  |     |  a  |
x(t)----->|  +  |----->|  +  |----->|  +  |----->|  +  |----->y(t)
    |  |  |     |  |  |     |  |  |     |  |  |
    +--|--+     +--|--+     +--|--+     +--|--+
       |           |           |           |
       |           |           |           |
       |           |           |           |
       +-----------+-----------+-----------+
                   Delay
                   z^-1

D(w) = w' / w

  ^ w'
  |
  |     a = 0.9
  |    /
  |   /
  |  /
  | /
  |/     a = 0.5
  +-----------------> w
  |\
  | \    a = -0.5
  |  \
  |   \
  |    \  a = -0.9
  |
```