import cv2
import numpy as np

def calculate_damage(frame):
    """
    Calculates bridge damage percentage based on edge/crack intensity
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)

    crack_pixels = np.sum(edges > 0)
    total_pixels = edges.size

    damage_percentage = (crack_pixels / total_pixels) * 100
    return round(damage_percentage, 2)

