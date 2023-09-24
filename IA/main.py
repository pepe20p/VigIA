import cv2
import numpy as np
import json

class Event:

    def __init__(self, frame):
        self.frame = frame
        self.events = []

    def add_event(self, event):
        self.events.append(event)


def writeToFile(events, filename):

    with open(filename, "a") as file:
        for item in events:
            json.dump(item.__dict__, file, indent=2)


def identifyEvents(video):

    eventos = []
    i = 0

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


    # Enquanto há frames do vídeo para processar
    has_video, frame = cap.read()
    while has_video:

        # Detecção dos eventos
        classes, scores, boxes = model.detect(frame, 0.1, 0.2)

        # Percorrer as detecções
        for (classid, score, box) in zip(classes, scores, boxes):
            
            # Analisa se é uma classe desejada e possui precisao maior ou igual a 60%
            if class_names[classid] in util_class_names and score >= 0.6:
                
                # Cria uma instancia na lista se nao ha este frame
                if not eventos or eventos[-1].frame < i and i % int(fps) == 0:
                    eventos.append(Event(i))

                # Percorre a lista de eventos para adicionar (caso ainda nao exista)
                # a classe nova no frame certo
                for evento in eventos:
                    
                    frame_evento = evento.frame
                    
                    if frame_evento == i and class_names[classid] not in evento.events:
                        evento.add_event(class_names[classid])

        # Escreve o que pegou naquele minuto (frames que ocorreram nos 60 segundos)
        if(i % int(fps*(1*60 + 0)) == 0 and i != 0):
            
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