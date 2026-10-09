import numpy as np
import matplotlib.pyplot as plt

# Time: 0 to 1 second, 1000 samples
t = np.linspace(0, 1, 1000)

# Same sine wave, different frequencies
freqs = [1, 5, 10] # 1Hz, 5Hz, 10Hz
signals = []
for f in freqs:
    x = np.sin(2 * np.pi * f * t)
    signals.append(x)

# Plot
plt.figure(figsize=(10, 6))
for i, f in enumerate(freqs):
    plt.plot(t, signals[i], label=f'{f} Hz')

plt.title('Day 03 - Effect of Frequency on Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('day03_frequency.png', dpi=300)
plt.show()

print("Day 03 done! 1Hz = slow, 10Hz = fast oscillation")
