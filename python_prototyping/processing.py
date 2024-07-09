import numpy as np
import librosa
import math


def squash_and_trim(audio_list, frames):
    return_list = []
    for audio in audio_list:
        return_list.append(librosa.to_mono(audio)[:frames])
    return return_list


# def return_dB_val(raw, delta):
#     delta_dif = raw - delta
#     return np.where(delta_dif > -80, delta_dif, -80)
def apply_sidechain_compression(side, root, threshold, ratio):
    return root if side < threshold else root / ratio


v_apply_sidechain_compression = np.vectorize(apply_sidechain_compression)


# threshold = dB limit of sidechain input to consider compression
# 1:ratio = intensity of compression
def compress_spect_slice(threshold, ratio,
                         spect_slice_side: np.array,
                         spect_slice_root: np.array):
    assert ratio <= 8 and ratio >= 1 and type(ratio) is int
    # find diff
    sidechained_signal = v_apply_sidechain_compression(
        spect_slice_side, spect_slice_root,
        math.log(ratio), threshold
    )
    return sidechained_signal


def calc_spectogram(audio, sr=44100):
    # mono_audio = librosa.to_mono(audio)
    stft = librosa.stft(audio)
    # spectogram = librosa.amplitude_to_db(np.abs(stft))
    spectogram = np.abs(stft)
    return spectogram, np.angle(stft)


# unecessary for now. but will give control for slicing later if needed/wanted
def griffinlim_spec_to_audio(spec):
    audio = librosa.griffinlim(spec)
    return audio
