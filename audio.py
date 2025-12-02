import pandas as pd
from scipy.io import wavfile

sample_rate, data = wavfile.read("audio.wav")

df = pd.DataFrame(data)
print(df.head())

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

sample_rate, data = wavfile.read("audio.wav")

# If stereo, convert to mono
if len(data.shape) == 2:
    data = data.mean(axis=1)

# Create time axis
time = np.linspace(0, len(data) / sample_rate, num=len(data))

# Plot waveform
plt.plot(time, data)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
