import pytest
import cv2

def test_mp4_file_video():
    
    video_path = "example.mp4"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_avi_file_video():
    
    video_path = "example.avi"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_mkv_file_video():
    
    video_path = "example.mkv"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_divx_file_video():
    
    video_path = "example.divx"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_xvid_file_video():
    
    video_path = "example.xvid"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_x264_file_video():
    
    video_path = "example.x264"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_mjpg_file_video():
    
    video_path = "example.mjpg"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_wmv1_file_video():
    
    video_path = "example.wmv1"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_wmv2_file_video():
    
    video_path = "example.wmv2"
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video
