""" Learning fourier transforms
Concepts gotten from "But what is the Fourier Transform? A visual introduction"
https://www.youtube.com/watch?v=spUNpyF58BY

Author: Precious Jatau
"""

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
f1 = 3
f2 = 5
A = 2
nPts = 2000
tDuration = 5
t = np.linspace(0,tDuration,nPts)
xt1 = A*np.sin(2*np.pi*f1*t)
xt2 = A*np.sin(2*np.pi*f2*t)
xt = xt1 + xt2

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
axs[1].set_title("Wounded x(t)")
plt.tight_layout()

# Almost fourier transform
# for different winding frequencies, calculate the mean of the real and imaginary parts of wound signal
xtTransform = []
fSamples = np.linspace(0,8,nPtsWind)
for fWind in fSamples:
    xtWound = xt * np.exp(1j * 2 * np.pi * fWind * t)
    xtTransform.append((np.mean(xtWound.real), np.mean(xtWound.imag)))

comReal = [x[0] for x in xtTransform]   # center of mass real
comImag = [x[1] for x in xtTransform]   # center of mass real

plt.figure()
plt.plot(fSamples, comReal, color = 'blue', linewidth = 2, label = 'real')
plt.plot(fSamples, comImag, color = 'red', linewidth = 2, label = 'imaginary')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Center of mass")
plt.title("Center of mass at different fWind")
plt.legend()
plt.show()