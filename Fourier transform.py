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


# Create sinusoid
f = 3
A = 2
t = np.linspace(0,1,100)
xt = A*np.sin(2*np.pi*f*t)

# set winding parameters
fWind = 3

# Wind around unit circle at the rate of 1 cycle per second
xtWound = xt*np.exp(1j*2*np.pi*fWind*t)

# plot
fig, axs = plt.subplots(3)
axs[0].plot(t, xt)

axs[1].plot(xtWound.real, xtWound.imag)
plt.show()
