def generate_explanation(features, label):
    if label == "AI_GENERATED":
        reasons = []
        if features["pitch_std"] < 6:
            reasons.append("unnatural pitch consistency")
        if features["energy_std"] < 0.01:
            reasons.append("uniform energy levels")
        if features["mfcc_std"] < 20:
            reasons.append("highly stable spectral patterns")

        return "AI-like characteristics detected: " + ", ".join(reasons)

    else:
        return "Natural pitch and energy variations indicate human speech"
