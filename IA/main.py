import cv2
import numpy as np
import json
import os
import sys

fps = 0.0

class Event:
    def __init__(self, frame):
        self.frame = frame
        self.events = []

    def add_event(self, event):
        self.events.append(event)

def destroyAlreadyCreatedFile():
    if os.path.exists("events.json"):
        os.remove("events.json")


def addFrameToEvent(events, frame):

    second_of_frame = int(fps)

    if (not events) or ((events[-1].frame < frame) and frame % second_of_frame == 0):
        events.append(Event(frame))


def insertEvent(events, frame, found_event):

    for event in events:
        frame_event = event.frame
        if frame_event == frame and found_event not in event.events:
            event.add_event(found_event)

def writeToFile(events, filename):

    global fps
    frames = []

    if os.path.exists(filename):
        # Le o arquivo ja existente e copia os events
        with open(filename, "r") as file:
            frames = json.load(file)
    else:
        # Cria o arquivo e adiciona o FPS do video
        _ = open(filename, "x")
        frames.append({"fps": fps})

    # Os novos events sao adicionados
    for item in events:
        frames.append(item.__dict__)        

    # Insere no arquivo
    with open(filename, "w") as file:
        json.dump(frames, file, indent=1)


# tolerance: máximo numero de frames que um evento pode não ocorrer/não ser detectado no vídeo e ainda ser considerado o mesmo evento
def groupFramesByEvent(input_filename, output_filename, tolerance=1):

    tolerance = int(tolerance)

    # Carrega o arquivo JSON original
    with open(input_filename, "r") as file:
        data = json.load(file)

    # Extrai o FPS do JSON original
    fps = data[0]["fps"]

    # Extrai os eventos e os frames associados
    events_data = data[1:]
    event_dict = {}  # Dicionário para armazenar eventos e frames associados

    for event_info in events_data:
        frame = event_info['frame']
        events = event_info['events']

        for event in events:
            if event not in event_dict:
                event_dict[event] = []
            
            # Verifica se o frame atual é consecutivo ao último frame do evento
            if event_dict[event] and (frame - event_dict[event][-1][-1]) <= tolerance:
                event_dict[event][-1] = (event_dict[event][-1][0], frame)  # Atualiza o frame final
            else:
                event_dict[event].append((frame, frame))  # Inicia um novo intervalo de frames

    # Cria a lista de eventos únicos com frames associados
    unique_events = [{"event": event, "frames": frames} for event, frames in event_dict.items()]

    # Adiciona o FPS como o primeiro elemento no arquivo de saída
    unique_events.insert(0, {"fps": fps})

    # Escreve o resultado no novo arquivo JSON
    with open(output_filename, "w") as output_file:
        json.dump(unique_events, output_file, indent=2)


def identifyEvents(video):

    global fps
    class_names = []
    util_class_names = []
    events = []
    actual_frame = 0

    with open("coconames", "r") as f:
        class_names = [cname.strip() for cname in f.readlines()]
    with open("utilnames", "r") as f:
        util_class_names = [cname.strip() for cname in f.readlines()]

    # Redes pré-treinadas YOLO
    net = cv2.dnn.readNet("yolov7-tiny.weights", "yolov7-tiny.cfg")
    model = cv2.dnn.DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255) # da CFG

    # Captura de video da bibioteca do OpenCV
    cap = cv2.VideoCapture(video)
    fps = cap.get(cv2.CAP_PROP_FPS)

    second_of_frame = int(fps)
    
    has_video, frame = cap.read()
    while has_video:

        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        for (classid, score, box) in zip(classes, scores, boxes):

            found_class = class_names[classid]

            # Analisa se é uma classe desejada e possui precisao maior ou igual a 60%
            if found_class in util_class_names and score >= 0.6:

                addFrameToEvent(events, actual_frame)
                insertEvent(events, actual_frame, found_class)

        if(actual_frame != 0 and actual_frame % second_of_frame == 0):
            writeToFile(events, "events.json")
            events = []

        has_video, frame = cap.read()
        actual_frame += 1
    
    return events

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print('Uso: main.py <Nome do video e formato>')
        exit()

    video = sys.argv[1]

    destroyAlreadyCreatedFile()

    events = identifyEvents(video)

    # Escreve o que sobrou
    if(events):
        writeToFile(events, "events.json")
    
    groupFramesByEvent("events.json", "groupedframes.json", tolerance=fps*5)