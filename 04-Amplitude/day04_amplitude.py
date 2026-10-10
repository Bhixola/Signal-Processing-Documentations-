import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
freq = 5 # Keep frequency constant
amplitudes = [0.5, 1, 2] # Change amplitude

plt.figure(figsize=(10, 6))
for A in amplitudes:
    x = A * np.sin(2 * np.pi * freq * t)
    plt.plot(t, x, label=f'Amplitude = {A}')

plt.title('Day 04 - Effect of Amplitude (f=5Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Save to Gallery + local
save_path = '/storage/emulated/0/Pictures/day04_amplitude.png'
plt.savefig(save_path, dpi=300)
plt.savefig('day04_amplitude.png')
print(f"Saved to {save_path}")
plt.show()
