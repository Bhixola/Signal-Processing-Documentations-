import numpy as np
import matplotlib.pyplot as plt

# My first signal - sine wave
t = np.linspace(0, 1, 500) # time from 0 to 1 sec
frequency = 5 # 5 Hz
signal = np.sin(2 * np.pi * frequency * t)

plt.plot(t, signal)
plt.title("My First Signal - 5Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
