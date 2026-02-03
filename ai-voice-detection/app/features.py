import numpy as np
import librosa

def extract_features(audio, sr):
    # Pitch (fundamental frequency)
    pitch = librosa.yin(audio, fmin=50, fmax=300)
    pitch = pitch[~np.isnan(pitch)]

    # Energy
    energy = audio ** 2

    # MFCC
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

    features = {
        "pitch_std": float(np.std(pitch)) if len(pitch) > 0 else 0.0,
        "energy_std": float(np.std(energy)),
        "mfcc_std": float(np.std(mfcc))
    }

    return features
