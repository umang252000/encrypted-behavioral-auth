REQUIRED_FEATURES = {
    "keystroke_flight_mean",
    "keystroke_flight_var",
    "keystroke_dwell_mean",
    "mouse_speed_mean",
    "mouse_speed_var",
}

def validate_features(features: dict):
    missing = REQUIRED_FEATURES - features.keys()
    if missing:
        raise ValueError(f"Missing features: {missing}")