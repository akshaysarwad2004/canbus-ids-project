import pandas as pd


def _payload_entropy(payload: str) -> float:
    """Simple entropy-like metric based on unique characters in the hex string."""
    if not payload:
        return 0.0
    chars = set(payload)
    return len(chars) / len(payload)


def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add basic features for IDS model.

    Expected input columns:
        - id
        - dlc
        - payload
        - attack (label)
    """
    df = df.copy()
    df["id_int"] = df["id"].astype(int)

    # Entropy-like feature
    df["entropy"] = df["payload"].astype(str).apply(_payload_entropy)

    # Simple spoofing indicator based on known malicious IDs
    suspicious_ids = {0x123, 0x666, 0x777}
    df["is_spoof"] = df["id_int"].apply(lambda x: 1 if x in suspicious_ids else 0)

    # You can extend this with time-based features, rolling statistics, etc.
    feature_cols = ["id_int", "dlc", "entropy", "is_spoof"]
    if "attack" in df.columns:
        feature_cols.append("attack")

    return df[feature_cols]
