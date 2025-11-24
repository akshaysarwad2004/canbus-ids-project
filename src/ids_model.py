from pathlib import Path
import joblib
import pandas as pd

from feature_extractor import extract_features


class CANIDSModel:
    """Wrapper around the trained ML model for easier use."""

    def __init__(self, model_path=None):
        if model_path is None:
            base_dir = Path(__file__).resolve().parents[1]
            model_path = base_dir / "can_ids_model.pkl"

        self.model_path = Path(model_path)
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model file not found at {self.model_path}. "
                "Train the model by running train_ids.py first."
            )

        self.model = joblib.load(self.model_path)

    def predict_frame(self, frame: dict) -> int:
        """Predict whether a single CAN frame is attack (1) or normal (0).

        Frame dict should contain keys: id, dlc, payload.
        """
        df = pd.DataFrame([frame])
        df["attack"] = 0  # dummy label for feature extractor
        feat_df = extract_features(df)
        X = feat_df.drop("attack", axis=1)
        pred = self.model.predict(X)
        return int(pred[0])
