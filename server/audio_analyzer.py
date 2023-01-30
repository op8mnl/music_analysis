from scipy.io import wavfile
import numpy as np
from numpy.fft import fft , ifft
from pathlib import Path
import os 
import matplotlib.pyplot as plt

path = Path(__file__).parent.resolve()

samplerate, data = wavfile.read(str(path)+"\\assets\\Kendrick Lamar - DNA Lyrics.wav")

print(f"number of channels = {data.shape[1]}")

length = data.shape[0] / samplerate

print(f"length = {length}s")

time = np.linspace(0., length, data.shape[0])
X = fft(data)
N = len(X)
n = np.arange(N)
T = N/samplerate
freq = n/T 

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(t, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()