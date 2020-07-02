""" Learning fourier transforms
from "But what is the Fourier Transform? A visual introduction"
https://www.youtube.com/watch?v=spUNpyF58BY
by 3Blue1Brown

Author: Precious Jatau
"""

# TO DO
# create filter to remove high frequency noise
# take IFT
# apply filter to time domain
# visual filtered signal, fourier transform

# import libraries
import numpy as np
import matplotlib.pyplot as plt


# Create a unit circle using euler's formular
fWind = 1
t = np.linspace(0,1,100)
exp_ft = np.exp(1j*2*np.pi*fWind*t)

fig, axs = plt.subplots(2,2)
axs[0,0].plot(t, exp_ft.real)
axs[0,0].set_title("Real part")
axs[0,0].set_xlim([0, 1])

axs[0,1].plot(t, exp_ft.imag)
axs[0,1].set_title("Imaginary part")
axs[0,1].set_xlim([0, 1])

axs[1,0].plot(exp_ft.real, exp_ft.imag)
axs[1,0].set_title("Unit circle")
axs[1,0].set_xlim([-1, 1])
axs[1,0].set_ylim([-1, 1])
axs[1,0].set_xlabel("Real")
axs[1,0].set_ylabel("Imag")

plt.tight_layout()


# Create a signal containing two frequencies: 3 and 5 cycles per second
# Note: shorter tDuration lead to more uncertain frequency estimates and vice versa
f = [3, 5]
A = [2, 2]
nPts = 2000
tDuration = 4
t = np.linspace(0,tDuration,nPts)

xt = 0
for i in range(len(f)):
    xt = xt + A[i]*np.sin(2*np.pi*f[i]*t)

# set winding parameters
fWind = 3
nPtsWind = 1000

# Wind signal around unit circle at the rate of fWind cycle per second
xtWound = xt*np.exp(1j*2*np.pi*fWind*t)

# plot signal, wounded signal
fig, axs = plt.subplots(2)
axs[0].plot(t, xt)
axs[0].set_title("x(t)")

axs[1].plot(xtWound.real, xtWound.imag)
axs[1].set_title("Wounded x(t), fWind = {} Hz".format(fWind))
plt.tight_layout()

# Almost fourier transform
# for different winding frequencies, calculate the mean of the real and imaginary parts of wound signal
xtTransform = []
fSamples = np.linspace(0,8,nPtsWind)
for fWind in fSamples:
    xtWound = xt * np.exp(1j * 2 * np.pi * fWind * t)
    xtTransform.append(xtWound)

comReal = [np.mean(x.real) for x in xtTransform]   # center of mass real
comImag = [np.mean(x.imag) for x in xtTransform]   # center of mass imaginary

plt.figure()
plt.plot(fSamples, comReal, color = 'blue', linewidth = 2, label = 'real')
plt.plot(fSamples, comImag, color = 'red', linewidth = 2, label = 'imaginary')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Center of mass")
plt.title("Center of mass at different fWind")
plt.legend()
plt.show()

# Inverse fourier transform


