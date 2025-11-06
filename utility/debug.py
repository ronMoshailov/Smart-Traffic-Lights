import os
from utility import constants

def is_file_exist(file_path):
    """
    מקבלת נתיב לקובץ, בודקת אם הוא קיים ומחזירה את שמו.
    """
    if os.path.isfile(file_path):
        file_name = os.path.basename(file_path)
        print(f"File exists: {file_name}")
        return True, file_name
    else:
        print(f"File does not exist: {file_path}")
        return False, None

is_file_exist(constants.SIMPLE_VIDEO_PATH)