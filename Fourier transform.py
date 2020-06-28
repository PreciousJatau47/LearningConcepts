
# import libraries
import numpy as np
import matplotlib.pyplot as plt



# unit circle

f = 1
t = np.linspace(0,1,100)
exp_ft = np.exp(1j*2*np.pi*t)

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
plt.show()
