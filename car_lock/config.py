import cv2
# 视频配置
VIDEO_SOURCE = r"C:\Users\15781\Videos\Captures\test_video.mp4" # 0=本地摄像头，可替换为视频路径（如"test_video.mp4"）
FPS = 30 # 默认帧率（若视频读取失败时使用）
FRAME_WIDTH = 960  # 输出帧宽度（减小分辨率以提高帧率）
FRAME_HEIGHT = 540  # 输出帧高度（减小分辨率以提高帧率）

# 车辆检测配置
MIN_VEHICLE_AREA = 800  # 最小车辆轮廓面积（过滤噪点）
DILATE_ITERATIONS = 1  # 膨胀操作次数（减少以提高帧率）
ERODE_ITERATIONS = 1   # 腐蚀操作次数（去除小噪点）

# 测速配置
PIXEL_PER_METER = 50  # 像素/米（需根据实际场景校准，关键参数！）
DETECTION_LINE1_Y = 200  # 第一检测线Y坐标
DETECTION_LINE2_Y = 500  # 第二检测线Y坐标
LINE_COLOR = (0, 255, 0)  # 检测线颜色（绿色）
LINE_THICKNESS = 2  # 检测线粗细

# 车牌识别配置
OCR_LANG = ['ch_sim', 'en']  # 识别语言（中文+英文）
OCR_CONFIDENCE = 0.5  # 车牌识别置信度阈值（过滤低可信度结果）

# 可视化配置
TEXT_FONT = cv2.FONT_HERSHEY_SIMPLEX
TEXT_SIZE = 0.7
TEXT_COLOR = (255, 0, 0)  # 文字颜色（蓝色）
TEXT_THICKNESS = 2

# 视频播放速度控制
VIDEO_SPEED_FACTOR = 1.0  # 视频播放速度因子：1.0=正常速度，2.0=一半速度，0.5=两倍速度
