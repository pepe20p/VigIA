from utils import *

class Event:

    def __init__(self, frame):
        self.frame = frame
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def add_frame_to_event(self, frame):

        second_of_frame = int(get_fps())

        if (not self.events) or ((self.events[-1].frame < frame) and frame % second_of_frame == 0):
            self.events.append(Event(frame))

    def insert_event(self, frame, found_event):

        for event in self.events:
            frame_event = event.frame
            if frame_event == frame and found_event not in event.events:
                event.add_event(found_event)

    
            