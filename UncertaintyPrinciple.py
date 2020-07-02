""" The uncertainty principle
from "The more general uncertainty principle, beyond quantum"
https://www.youtube.com/watch?v=MBnnXbOM5S4&t=100s
by 3Blue1Brown

SUMMARY

Short (in time) signals correlate with a wide range of frequencies
Long signals correlate with a small range of frequencies

On Fourier transforms:
the position of the center of mass (com) vector encodes the strength of that frequency in the original signal,
the angle between the x-axis and the com vector encodes the phase.
FT's can also be thought as a measure of how well a signal correlates with a particular winding frequency

Uncertainty principle radar example:

Radars measure the range of targets as the round trip time of a transmitted pulse
All reflected (return) pulses are integrated.
Long pulses could lead to overlapping returns in time (position), making it difficult to resolve individual returns

Radars measure the velocity of targets as the change in frequency between the transmitted and returned signal.
To have more certain frequency estimates, longer sampling in time (pulses) is neccessary.

x(time) <=FT=> X(F)

Thus, more certainty in measuring the position (range) of targets would cause incertainty in measuring their velocity
(frequency) and vice versa.

Uncertainty principle:

If a particle is considered as a wave x(position) concentrated over a certain spatial location,
then the FT X(spatial frequency), tells how much spatial frequencies correspond to x(postion).

x(position) <=FT=> X(spatial F)
momentum = p * spatial frequency

Thus, there is a trade off in measuring position and momentum.


Code author: Precious Jatau
"""

#TODO
# create xt as a sum of many short pulses
# find fourier transform of above
# vary pulse width and see trade offs in frequencies

