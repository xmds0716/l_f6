#视频流读取
import cv2
import time
from config import VIDEO_SOURCE, FPS, FRAME_WIDTH, FRAME_HEIGHT


class VideoCapture:
    def __init__(self, video_source=None):
        # 初始化视频捕获（摄像头/本地视频）
        # 如果没有提供视频源，则使用配置文件中的默认值
        source = video_source if video_source is not None else VIDEO_SOURCE
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise ValueError(f"无法打开视频源：{source}")

        # 设置视频缓冲区为较大值，提高帧率
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 10)  # 较大缓冲区，提高流畅度
        # 设置视频位置为当前帧，强制OpenCV使用正确的时间戳
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        # 设置摄像头参数（如果是摄像头）
        if isinstance(source, int):
            self.cap.set(cv2.CAP_PROP_FPS, FPS)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
            self.cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)  # 自动对焦

        # 获取实际视频帧率（若失败则用默认值）
        self.actual_fps = self.cap.get(cv2.CAP_PROP_FPS) or FPS
        self.frame_width = FRAME_WIDTH
        self.frame_height = FRAME_HEIGHT

        # 标记是否为摄像头
        self.is_camera = isinstance(source, int)

        # 帧率控制变量
        self.last_frame_time = time.time()
        self.frame_interval = 1.0 / self.actual_fps
        # 对于视频文件，使用更灵活的帧率控制
        self.use_frame_timing = not self.is_camera

    def read_frame(self):
        """读取一帧并调整分辨率"""
        # 读取最新帧
        ret, frame = self.cap.read()
        if not ret:
            return False, None  # 视频结束或读取失败

        # 调整帧大小（统一分辨率）
        frame_resized = cv2.resize(frame, (self.frame_width, self.frame_height))

        return True, frame_resized

    def release(self):
        """释放视频资源"""
        self.cap.release()
        cv2.destroyAllWindows()

    def get_fps(self):
        """获取视频帧率（用于测速计算）"""
        return self.actual_fps
