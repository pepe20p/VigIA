from utils import *
from FileHandler import *
from Event import *

current_frame = 0
events = Event(current_frame)

class EventDetector():

    def identify_events(self, video):

        global current_frame

        cap = cv2.VideoCapture(video)

        has_video, frame = cap.read()

        while has_video:

            self.analyze_frame(frame)

            self.is_time_to_write(current_frame)

            has_video, frame = cap.read()
            current_frame += 1
        
        return events.events
    
    def analyze_frame(self, frame):

        global events

        classes, scores, _ = model.detect(frame, 0.1, 0.2)

        for (classid, score, _) in zip(classes, scores, _):

            found_class = class_names[classid]
            
            # Analisa se é uma classe desejada e possui precisao maior ou igual a 60%
            if found_class in util_class_names and score >= get_precision():

                events.add_frame_to_event(current_frame)
                events.insert_event(current_frame, found_class)

    
    def is_time_to_write(self, current_frame):

        global events

        second_of_frame = int(get_fps())

        if(current_frame != 0 and current_frame % second_of_frame == 0):
            FileHandler().write_to_file(events.events, "events.json")
            events = Event(current_frame)