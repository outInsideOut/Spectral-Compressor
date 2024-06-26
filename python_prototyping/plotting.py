import numpy as np
import matplotlib.pyplot as plt
import librosa


def calc_spectogram(audio, sr=44100):
    mono_audio = librosa.to_mono(audio)
    stft = librosa.stft(mono_audio)
    spectogram = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return spectogram


def plot_spectogram(spectogram, title, sr=44100):
    fig, ax = plt.subplots()

    img = librosa.display.specshow(
        librosa.amplitude_to_db(
            spectogram, ref=np.max
        ), x_axis='time', y_axis='log', ax=ax
    )

    ax.set(title=title)
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.show
