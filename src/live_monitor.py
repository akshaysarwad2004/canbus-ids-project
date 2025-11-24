import can
from ids_model import CANIDSModel


def main():
    model = CANIDSModel()
    # Change channel/bustype based on your platform
    bus = can.interface.Bus(channel="can0", bustype="socketcan")

    print("🔍 Live CAN IDS Monitoring Started... (Ctrl+C to stop)")

    while True:
        msg = bus.recv()  # blocking call
        if msg is None:
            continue

        frame = {
            "id": msg.arbitration_id,
            "dlc": msg.dlc,
            "payload": msg.data.hex().upper(),
        }

        pred = model.predict_frame(frame)

        if pred == 1:
            print(f"⚠️  INTRUSION DETECTED! → ID=0x{frame['id']:03X}, payload={frame['payload']}")
        else:
            print(f"OK: ID=0x{frame['id']:03X}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping CAN IDS monitor.")
