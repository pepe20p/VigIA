import pytest
from utils import *
from Event import *
from EventDetector import *
from FileHandler import *

video_path = "video-test1.mp4"

def test_mp4_file_video():
    
    cap = cv2.VideoCapture(video_path)
    
    has_video, _ = cap.read()

    assert has_video

def test_initialization():
    event = Event(1)
    assert event.frame == 1
    assert event.events == []

def test_add_event():
    event = Event(1)
    event.add_event(event)
    assert event.events == [event]

def test_add_frame_to_event():
    event = Event(1)

    set_fps(30)

    event.addFrameToEvent(31)
    assert len(event.events) == 1

    event.addFrameToEvent(60)
    assert len(event.events) == 2

def test_insert_event():
    event = Event(1)
    event.add_event(event)

    found_event = Event(2)
    event.insertEvent(1, found_event)
    assert event.events[0].events == [event, found_event]

    event.insertEvent(2, found_event)
    assert event.events[0].events == [event, found_event]

    event.insertEvent(1, found_event)
    assert event.events[0].events == [event, found_event]
