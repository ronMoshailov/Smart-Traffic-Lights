import os


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
