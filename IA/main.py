from utils import *
from FileHandler import *
from EventDetector import *


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Uso: main.py <arquivo_video.formato>')
        exit()

    video = sys.argv[1]

    fps = cv2.VideoCapture(video).get(cv2.CAP_PROP_FPS)
    set_fps(fps)
       
    file = FileHandler()
    file.destroy_already_created_file()

    event_detector = EventDetector()

    events = event_detector.identify_events(video)

    # Escreve o que sobrou
    if(events):
        file.write_to_tile(events, "events.json")
    
    file.group_frames_by_event("events.json", "groupedframes.json", tolerance=fps*5)