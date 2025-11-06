import os
import torch

def rename_files_in_folder(folder_path):

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for i, filename in enumerate(files, start=1):
        # חילוץ סיומת הקובץ (למשל jpg, png וכו')
        ext = os.path.splitext(filename)[1]

        # יצירת שם חדש בפורמט 001, 002, 003...
        new_name = f"{i:03d}{ext}"

        # בניית נתיבים מלאים
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        # שינוי השם
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_name}')

    print("✅ סיום! כל הקבצים שונו בהצלחה.")

# דוגמה לשימוש:
# rename_files_in_folder(r"C:\Users\YourName\Desktop\images")

def set_cuda():
    if torch.cuda.is_available():
        device = "cuda"
        print(f"✅ GPU detected: {torch.cuda.get_device_name(0)}")
    else:
        device = "cpu"
        print("⚠️ CUDA not available, running on CPU.")
    return device