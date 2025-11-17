#车辆跟踪
import cv2
import numpy as np
from collections import deque

class VehicleTracker:
    def __init__(self, max_disappeared=10, max_distance=50):
        """
        初始化车辆跟踪器
        :param max_disappeared: 车辆消失的最大帧数，超过则移除
        :param max_distance: 两个检测框之间的最大距离，超过则认为是不同车辆
        """
        self.next_object_id = 0
        self.objects = {}  # 存储当前跟踪的车辆 {id: (contour, last_seen)}
        self.disappeared = {}  # 存储车辆消失的帧数 {id: frame_count}
        self.max_disappeared = max_disappeared
        self.max_distance = max_distance

    def register(self, contour):
        """注册新的车辆"""
        self.objects[self.next_object_id] = (contour, 0)  # (contour, last_seen_frame)
        self.disappeared[self.next_object_id] = 0
        self.next_object_id += 1

    def deregister(self, object_id):
        """移除车辆"""
        del self.objects[object_id]
        del self.disappeared[object_id]

    def update(self, detected_contours):
        """
        更新跟踪器
        :param detected_contours: 当前帧检测到的车辆轮廓列表
        :return: 跟踪到的车辆 {id: contour}
        """
        # 如果当前帧没有检测到任何车辆，标记所有现有车辆为消失
        if len(detected_contours) == 0:
            for object_id in list(self.disappeared.keys()):
                self.disappeared[object_id] += 1

                # 如果车辆消失超过最大帧数，移除它
                if self.disappeared[object_id] > self.max_disappeared:
                    self.deregister(object_id)

            return self.objects

        # 如果当前没有任何跟踪的车辆，注册所有检测到的车辆
        if len(self.objects) == 0:
            for contour in detected_contours:
                self.register(contour)
        else:
            # 获取现有车辆的中心点
            object_centroids = {}
            object_ids = list(self.objects.keys())
            for i, (object_id, (contour, _)) in enumerate(self.objects.items()):
                x, y, w, h = cv2.boundingRect(contour)
                cx = x + w // 2
                cy = y + h // 2
                object_centroids[object_id] = (cx, cy)

            # 获取新检测到的车辆的中心点
            input_centroids = []
            for contour in detected_contours:
                x, y, w, h = cv2.boundingRect(contour)
                cx = x + w // 2
                cy = y + h // 2
                input_centroids.append((cx, cy))

            # 计算距离矩阵
            D = np.zeros((len(self.objects), len(detected_contours)))
            for i, object_id in enumerate(object_ids):
                for j, (cx, cy) in enumerate(input_centroids):
                    ox, oy = object_centroids[object_id]
                    D[i, j] = np.sqrt((cx - ox) ** 2 + (cy - oy) ** 2)

            # 使用匈牙利算法找到最小匹配
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            # 跟踪已使用的行和列索引
            used_row_idxs = set()
            used_col_idxs = set()

            # 遍历(行,列)索引元组的组合
            for (row, col) in zip(rows, cols):
                # 如果已经检查过这个行或列，忽略它
                if row in used_row_idxs or col in used_col_idxs:
                    continue

                # 如果距离大于最大距离，不匹配
                if D[row, col] > self.max_distance:
                    continue

                # 获取对象ID和轮廓
                object_id = object_ids[row]
                self.objects[object_id] = (detected_contours[col], 0)  # 更新轮廓和重置last_seen
                self.disappeared[object_id] = 0  # 重置消失计数器

                # 标记为已使用
                used_row_idxs.add(row)
                used_col_idxs.add(col)

            # 计算未使用的行和列索引
            unused_row_idxs = set(range(0, D.shape[0])).difference(used_row_idxs)
            unused_col_idxs = set(range(0, D.shape[1])).difference(used_col_idxs)

            # 如果对象数量大于等于检测到的轮廓数量，检查是否有对象消失
            if D.shape[0] >= D.shape[1]:
                for row in unused_row_idxs:
                    object_id = object_ids[row]
                    self.disappeared[object_id] += 1

                    # 如果对象消失超过最大帧数，移除它
                    if self.disappeared[object_id] > self.max_disappeared:
                        self.deregister(object_id)
            else:
                # 否则注册新的检测到的对象
                for col in unused_col_idxs:
                    self.register(detected_contours[col])

        # 更新所有对象的last_seen计数
        for object_id in list(self.objects.keys()):
            contour, last_seen = self.objects[object_id]
            self.objects[object_id] = (contour, last_seen + 1)

        return self.objects
