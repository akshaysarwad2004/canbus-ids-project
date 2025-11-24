import pandas as pd
import random
import time
from pathlib import Path


def generate_frame(frame_id, attack=False):
    """Generate a single synthetic CAN frame."""
    return {
        "timestamp": time.time(),
        "id": frame_id,
        "dlc": 8,
        "payload": "".join(f"{random.randint(0, 255):02X}" for _ in range(8)),
        "attack": 1 if attack else 0,
    }


def generate_normal(n=5000):
    """Generate normal CAN traffic with a fixed set of IDs."""
    data = []
    normal_ids = [0x100, 0x200, 0x300, 0x400]

    for _ in range(n):
        fid = random.choice(normal_ids)
        data.append(generate_frame(fid))

    return pd.DataFrame(data)


def generate_attack(n=1000):
    """Generate malicious CAN traffic (spoofing / DoS / fuzzy)."""
    data = []
    attack_ids = [0x123, 0x666, 0x777]

    for _ in range(n):
        fid = random.choice(attack_ids)
        data.append(generate_frame(fid, attack=True))

    return pd.DataFrame(data)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parents[1]
    dataset_dir = base_dir / "dataset"
    dataset_dir.mkdir(exist_ok=True)

    normal_df = generate_normal()
    attack_df = generate_attack()

    normal_path = dataset_dir / "normal.csv"
    attack_path = dataset_dir / "attack.csv"

    normal_df.to_csv(normal_path, index=False)
    attack_df.to_csv(attack_path, index=False)

    print(f"Normal data saved to {normal_path}")
    print(f"Attack data saved to {attack_path}")
    print("Dataset generation complete ✓")
