import numpy as np

EMBEDDING_DIM = 128

class BehavioralEncoder:
    def __init__(self, seed: int = 42):
        rng = np.random.default_rng(seed)
        self.projection = rng.normal(
            loc=0.0, scale=1.0, size=(5, EMBEDDING_DIM)
        )

    def encode(self, features: dict) -> np.ndarray:
        """
        Convert behavioral feature dict into fixed-length embedding.
        """
        x = np.array([
            features["keystroke_flight_mean"],
            features["keystroke_flight_var"],
            features["keystroke_dwell_mean"],
            features["mouse_speed_mean"],
            features["mouse_speed_var"],
        ], dtype=np.float32)

        # Normalize
        x = (x - x.mean()) / (x.std() + 1e-6)

        # Linear projection
        embedding = np.dot(x, self.projection)

        # L2 normalize for similarity search
        norm = np.linalg.norm(embedding) + 1e-6
        return embedding / norm