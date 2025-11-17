import cv2
import time
import os

def test_video_speed():
    """测试视频播放速度控制"""
    # 检查视频文件是否存在
    video_path = r"C:\Users\15781\Videos\Captures\test_video.mp4"
    
    if not os.path.exists(video_path):
        print(f"视频文件不存在: {video_path}")
        print("请确保视频文件存在，或修改 config.py 中的 VIDEO_SOURCE 路径")
        return
    
    print(f"正在打开视频文件: {video_path}")
    
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return
    
    # 获取视频信息
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    
    print(f"视频信息:")
    print(f"  帧率: {fps:.1f} FPS")
    print(f"  总帧数: {total_frames}")
    print(f"  时长: {duration:.1f} 秒")
    
    # 测试不同的速度因子
    speed_factors = [1.0, 2.0, 3.0]  # 正常速度，一半速度，三分之一速度
    
    for speed_factor in speed_factors:
        print(f"\n测试速度因子: {speed_factor}")
        print("按 'q' 退出测试，按任意键继续下一个速度测试")
        
        # 重置视频到开始
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        start_time = time.time()
        frames_processed = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # 显示帧
            cv2.imshow(f"视频测试 - 速度因子: {speed_factor}", frame)
            
            # 计算延迟时间
            base_delay = 30  # 基础延迟（毫秒）
            delay = int(base_delay * speed_factor)
            
            # 等待按键
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('q'):
                break
            elif key != 255:  # 任意键（非q）
                break
                
            frames_processed += 1
        
        end_time = time.time()
        actual_duration = end_time - start_time
        actual_fps = frames_processed / actual_duration if actual_duration > 0 else 0
        
        print(f"  实际播放时长: {actual_duration:.1f} 秒")
        print(f"  实际帧率: {actual_fps:.1f} FPS")
        print(f"  处理帧数: {frames_processed}")
    
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
    print("\n测试完成！")

if __name__ == "__main__":
    test_video_speed()
