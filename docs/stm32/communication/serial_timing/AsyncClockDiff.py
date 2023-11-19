import matplotlib.pyplot as plt
import numpy as np

# Time axis and constant high signal
time = np.linspace(1, 11, 500)
high_signal = np.ones_like(time)

# Sender and receiver sampling points
sender_sampling_points = np.linspace(1, 11, 10)
sender_sampled_high_signal = np.ones_like(sender_sampling_points)

receiver_sampling_9 = np.linspace(1, 11, 9)
receiver_sampled_high_signal_9 = np.ones_like(receiver_sampling_9)

receiver_sampling_11 = np.linspace(1, 11, 11)
receiver_sampled_high_signal_11 = np.ones_like(receiver_sampling_11)

# Plotting
plt.figure(figsize=(15, 4))

# Function to label points
def label_points(x, y, ax, offset=(0, 0)):
    for i, (px, py) in enumerate(zip(x, y)):
        ax.text(px + offset[0], py + offset[1], str(i+1), color='black', fontsize=8)

# Sender high signal
ax1 = plt.subplot(3, 1, 1)
plt.axis('off')
plt.plot(time, high_signal, 'C0-', label='High Signal')
plt.plot(sender_sampling_points, sender_sampled_high_signal, 'ro', label='Sampling Points (10 samples)')
label_points(sender_sampling_points, sender_sampled_high_signal, ax1, offset=(0, 0.04))
plt.title('Sender High Signal with 10 Sampling Points')
plt.ylim(0.8, 1.2)

# Receiver high signal with 9 samples
ax2 = plt.subplot(3, 1, 2)
plt.axis('off')
plt.plot(time, high_signal, 'C1-', label='High Signal')
plt.plot(receiver_sampling_9, receiver_sampled_high_signal_9, 'go', label='Sampling Points (9 samples)')
label_points(receiver_sampling_9, receiver_sampled_high_signal_9, ax2, offset=(0, 0.04))
plt.title('Receiver High Signal with 9 Sampling Points (10% Error)')
plt.ylim(0.8, 1.2)

# Receiver high signal with 11 samples
ax3 = plt.subplot(3, 1, 3)
plt.axis('off')
plt.plot(time, high_signal, 'C2-', label='High Signal')
plt.plot(receiver_sampling_11, receiver_sampled_high_signal_11, 'bo', label='Sampling Points (11 samples)')
label_points(receiver_sampling_11, receiver_sampled_high_signal_11, ax3, offset=(0, 0.04))
plt.title('Receiver High Signal with 11 Sampling Points (10% Error)')
plt.ylim(0.8, 1.2)

plt.tight_layout()

plt.savefig('AsyncClockDiff.png',dpi=300)
plt.show()