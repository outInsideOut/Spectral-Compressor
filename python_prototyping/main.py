import audio_io as aio
import numpy as np
import plotting
import processing


thunder_wav = "thunder.wav"
kicks_wav = "kicks.wav"

audio_dict = aio.load_list([thunder_wav, kicks_wav])

thunder_raw = audio_dict["thunder.wav"]
kicks_raw = audio_dict["kicks.wav"]

thunder_spectogram = plotting.calc_spectogram(thunder_raw[0])
# plotting.plot_spectogram(thunder_spectogram, "Thunder")
kicks_spectogram = plotting.calc_spectogram(kicks_raw[0])
# plotting.plot_spectogram(kicks_spectogram, "Kicks")
