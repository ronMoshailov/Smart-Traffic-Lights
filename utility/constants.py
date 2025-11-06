import os

## ========== Directory Paths ========== ##
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Day
DAY_360P_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'day_360p.mp4')       #  360p, day    ,
DAY_720P_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'day_720p.mp4')       #  720p, day    ,

# Night
NIGHT_720P_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'night_720p.mp4')               #  720p, night  ,
NIGHT_1080P_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'night_junction_1080p.mp4')    # 1080p, night  ,
NIGHT_01_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'night_junction.mp4')             # 1080p, night  ,

# Day - Snow
DAY_SNOW_720P_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'day_snow_720p.mp4')     #  720p, night  ,

# Day - Low Quality
DAY_LOW_QUALITY_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'day_low_quality.mp4')     #  720p, night  ,

# Test
COLORADO_TEST_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'colorado_test.mp4')
TEST_NIGHT_VIDEO_PATH = os.path.join(PROJECT_DIR, 'videos', 'Test', 'night_video.mp4')
