from ultralytics import YOLO

def main():
    model = YOLO("yolov8n-cls.pt")  # classification model

    model.train(
        data="dataset",     # thư mục dataset
        epochs=50,
        imgsz=224,
        batch=32,           # GPU nên tăng batch
        device=0,           # 🔥 GPU số 0
        name="asl_cls"
    )

if __name__ == "__main__":
    main()
