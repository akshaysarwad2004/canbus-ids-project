import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

from feature_extractor import extract_features


def main():
    base_dir = Path(__file__).resolve().parents[1]
    dataset_dir = base_dir / "dataset"

    normal_path = dataset_dir / "normal.csv"
    attack_path = dataset_dir / "attack.csv"

    if not normal_path.exists() or not attack_path.exists():
        raise FileNotFoundError(
            "Dataset files not found. Run can_simulator.py first to generate them."
        )

    normal = pd.read_csv(normal_path)
    attack = pd.read_csv(attack_path)

    df = pd.concat([normal, attack], ignore_index=True)
    df_feat = extract_features(df)

    X = df_feat.drop("attack", axis=1)
    y = df_feat["attack"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    pred = model.predict(X)
    acc = accuracy_score(y, pred)
    print(f"Training Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y, pred, digits=4))

    model_path = base_dir / "can_ids_model.pkl"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
