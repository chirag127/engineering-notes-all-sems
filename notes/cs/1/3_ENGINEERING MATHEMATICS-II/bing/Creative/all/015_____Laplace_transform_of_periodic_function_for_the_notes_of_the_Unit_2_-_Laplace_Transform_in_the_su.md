# Laplace transform of periodic function

A periodic function is a function that repeats itself after a fixed interval of time, called the period. For example, a sine wave, a square wave, and a sawtooth wave are all periodic functions.

The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.

Let f(t) be a periodic function with period T, such that f(t) = f(t+nT) for any integer n and for all t > 0. Then, the Laplace transform of f(t) is given by:

L{f(t)} = L{f(t) - f(t-T) + f(t-T)}  
= L{f(t) - f(t-T)} + e^(-sT)L{f(t)}  
= L{f(t) - f(t-T)} + e^(-sT)L{f(t+nT)}  
= L{f(t) - f(t-T)} + e^(-sT)L{f(t)}  
= L{f(t) - f(t-T)} / (1 - e^(-sT))

The term f(t) - f(t-T) is the difference between one cycle of the periodic function and the previous cycle. Therefore, the Laplace transform of f(t) can be obtained by finding the Laplace transform of one cycle of the function and dividing it by 1 - e^(-sT).

## Example

Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

![periodic function](https://www.intmath.com/laplace-transformation/img/periodic-function-1.gif)

The function f(t) can be written as:

f(t) = u(t) - u(t-1) + u(t-2) - u(t-3)

where u(t) is the unit step function. The Laplace transform of f(t) is:

L{f(t)} = L{u(t) - u(t-1) + u(t-2) - u(t-3)}  
= L{u(t)} - L{u(t-1)} + L{u(t-2)} - L{u(t-3)}  
= 1/s - e^(-s)/s + e^(-2s)/s - e^(-3s)/s  
= (1 - e^(-s) + e^(-2s) - e^(-3s)) / s

Using the time-shifting property, we can write:

L{f(t)} = L{f(t) - f(t-2)} / (1 - e^(-2s))  
= (1 - e^(-s) + e^(-2s) - e^(-3s)) / (s(1 - e^(-2s)))