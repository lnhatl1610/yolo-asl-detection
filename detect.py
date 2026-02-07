from ultralytics import YOLO

def main():
    model = YOLO("runs/classify/asl_cls/weights/best.pt")

    model(
        source=0,     # webcam
        conf=0.5,
        show=True     # hiện cửa sổ
    )

if __name__ == "__main__":
    main()
