import numpy as np
import matplotlib.pyplot as plt

# Same time like yesterday
fs = 1000
t = np.linspace(0, 1, fs)
freq = 5

# Yesterday's signal
sine_signal = np.sin(2 * np.pi * freq * t)

# Today's signal - COSINE
cosine_signal = np.cos(2 * np.pi * freq * t)

# Plot both together
plt.figure(figsize=(10, 5))
plt.plot(t, sine_signal, label='Sine - starts at 0')
plt.plot(t, cosine_signal, label='Cosine - starts at 1', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Day 02: Sine vs Cosine - Same Frequency, Different Phase')
plt.legend()
plt.grid(True)
plt.savefig('day02_cosine.png')
plt.show()
