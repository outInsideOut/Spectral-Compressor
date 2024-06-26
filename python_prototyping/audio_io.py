import librosa


def load(file_path, sample_rate=44100):
    audio, sr = librosa.load(file_path, sr=sample_rate, mono=False)
    print("done!")
    return audio, sr


def load_list(file_path_list, sample_rate=44100):
    audio_files = list()
    for path in file_path_list:
        audio_files.append(load(path))
    return dict(zip(file_path_list, audio_files))
