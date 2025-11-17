import cv2
import argparse
import os
from video_capture import VideoCapture
from vehicle_detector import VehicleDetector
from license_recognizer import LicensePlateRecognizer
from speed_calculator import SpeedCalculator
from vehicle_tracker import VehicleTracker
from utils import draw_detection_lines, draw_vehicle_info
from config import VIDEO_SPEED_FACTOR

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='车辆检测与车牌识别系统')
    parser.add_argument('--video', type=str, default=None,
                        help='视频文件路径（不指定则使用摄像头）')
    args = parser.parse_args()

    # 如果指定了视频文件，检查文件是否存在
    if args.video and not os.path.exists(args.video):
        print(f"错误：找不到视频文件 '{args.video}'")
        return
    # 初始化所有模块
    print("初始化模块...")
    video_capture = VideoCapture(args.video)
    vehicle_detector = VehicleDetector()
    license_recognizer = LicensePlateRecognizer()
    speed_calculator = SpeedCalculator()
    vehicle_tracker = VehicleTracker(max_disappeared=15, max_distance=50)
    fps = video_capture.get_fps()

    # 显示当前使用的视频源
    if args.video:
        print(f"正在使用视频文件：{args.video}")
    else:
        print("正在使用摄像头")
    print(f"视频帧率：{fps:.1f} FPS")

    try:
        print("开始检测（按 'q' 退出）...")
        while True:
            # 1. 读取视频帧
            ret, frame = video_capture.read_frame()
            if not ret:
                print("视频读取完毕或出错！")
                break

            # 2. 绘制测速检测线
            frame_with_lines = draw_detection_lines(frame.copy())

            # 3. 检测车辆
            detected_vehicles, fg_mask = vehicle_detector.detect_vehicles(frame)
            
            # 4. 更新车辆跟踪器
            tracked_vehicles = vehicle_tracker.update(detected_vehicles)
            
            # 5. 遍历每辆车，识别车牌+计算车速
            for vehicle_id, (vehicle, last_seen) in tracked_vehicles.items():
                # 识别车牌（减少识别频率以提高帧率）
                license_plate = None
                if last_seen % 15 == 0:  # 每15帧识别一次车牌，降低频率
                    license_plate = license_recognizer.recognize(frame, vehicle)
                
                # 计算车速
                speed = speed_calculator.calculate_speed(vehicle, fps, vehicle_id)
                
                # 绘制车辆信息
                frame_with_lines = draw_vehicle_info(frame_with_lines, vehicle, license_plate, speed, vehicle_id)

            # 5. 显示结果（原始帧+检测结果）
            cv2.imshow("License Plate + Speed Detection", frame_with_lines)
            cv2.imshow("Foreground Mask", fg_mask)  # 前景掩码（可选显示）

            # 控制视频播放速度
            if args.video:
                # 视频文件模式：通过调整延迟来控制播放速度
                # 使用配置文件中的速度因子来控制播放速度
                base_delay = 30  # 基础延迟（毫秒）
                delay = int(base_delay * VIDEO_SPEED_FACTOR)
                
                # 显示当前速度设置
                if hasattr(main, 'speed_info_shown') == False:
                    print(f"视频播放速度因子：{VIDEO_SPEED_FACTOR} (1.0=正常速度，2.0=一半速度)")
                    main.speed_info_shown = True
                
                # 按 'q' 退出
                if cv2.waitKey(delay) & 0xFF == ord('q'):
                    break
            else:
                # 摄像头模式，使用短延迟
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except Exception as e:
        print(f"程序出错：{str(e)}")
    finally:
        # 释放资源
        video_capture.release()
        print("程序退出，资源已释放！")

if __name__ == "__main__":
    main()
