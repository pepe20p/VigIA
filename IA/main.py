import cv2
import numpy as np
import json
import os

class Event:

    def __init__(self, frame):
        self.frame = frame
        self.events = []

    def add_event(self, event):
        self.events.append(event)


def writeToFile(events, filename):

    frames = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            frames = json.load(file)
    else:
        _ = open(filename, "x")

    for item in events:
        frames.append(item.__dict__)        

    with open(filename, "w") as file:
        json.dump(frames, file, indent=1)

def identifyEvents(video):

    # Listas que irão guardar as classes possíveis e outra que guardará apenas classes que desejamos trabalhar
    class_names = []
    util_class_names = []
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
    print('Frames Per Second =',fps)

    minuto_de_frame = int(fps*(0*60 + 2))
    segundo_de_frame = int(fps)
    eventos = []
    i = 0
    
    has_video, frame = cap.read()
    while has_video:

        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        for (classid, score, box) in zip(classes, scores, boxes):
            
            # Analisa se é uma classe desejada e possui precisao maior ou igual a 60%
            if class_names[classid] in util_class_names and score >= 0.6:
                
                # Cria uma instancia na lista se nao ha este frame
                # Percorre a lista de eventos do frame para adicionar o novo

                if not eventos or eventos[-1].frame < i and i % segundo_de_frame == 0:
                    eventos.append(Event(i))

                for evento in eventos:
                    
                    frame_evento = evento.frame
                    if frame_evento == i and class_names[classid] not in evento.events:
                        evento.add_event(class_names[classid])


        # Escreve o que pegou naquele minuto (frames que ocorreram nos 60 segundos)
        if(i % minuto_de_frame == 0 and i != 0):
            writeToFile(eventos, "events.json")
            eventos = []

        has_video, frame = cap.read()
        i += 1
    
    return eventos

if __name__ == '__main__':

    video = "video-test.mp4"

    eventos = identifyEvents(video)

    # Escreve o que sobrou
    if(eventos):
        writeToFile(eventos, "events.json")