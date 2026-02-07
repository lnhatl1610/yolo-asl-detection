import os
import shutil

SRC_ROOT = "dataset/dataset"   # dataset gốc
DST_ROOT = "dataset"           # dataset mới

TRAIN_COUNT = 900
VAL_COUNT = 1000

# Danh sách lớp
classes = (
    [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    + ["del", "nothing", "space"]
)

os.makedirs(DST_ROOT, exist_ok=True)

for split in ["train", "val"]:
    os.makedirs(os.path.join(DST_ROOT, split), exist_ok=True)

for cls in classes:
    src_dir = os.path.join(SRC_ROOT, cls)
    if not os.path.isdir(src_dir):
        print(f"❌ Không tìm thấy lớp: {cls}")
        continue

    images = sorted(os.listdir(src_dir))

    if len(images) < VAL_COUNT:
        print(f"⚠️ Lớp {cls} chỉ có {len(images)} ảnh")
        continue

    # Tạo thư mục đích
    train_dir = os.path.join(DST_ROOT, "train", cls)
    val_dir = os.path.join(DST_ROOT, "val", cls)
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # TRAIN
    for i in range(TRAIN_COUNT):
        src_img = images[i]
        ext = os.path.splitext(src_img)[1]
        dst_name = f"{cls}{i+1}{ext}"

        shutil.copy2(
            os.path.join(src_dir, src_img),
            os.path.join(train_dir, dst_name)
        )

    # VAL
    for i in range(TRAIN_COUNT, VAL_COUNT):
        src_img = images[i]
        ext = os.path.splitext(src_img)[1]
        dst_name = f"{cls}{i+1}{ext}"

        shutil.copy2(
            os.path.join(src_dir, src_img),
            os.path.join(val_dir, dst_name)
        )

    print(f"✅ Hoàn thành lớp {cls}")

print("🎉 Xong toàn bộ dataset!")
