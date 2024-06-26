import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

wav_file = "thunder.wav"

sample_rate, samples = wavfile.read(wav_file)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()
