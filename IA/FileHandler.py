from utils import *

class FileHandler():

    def destroy_already_created_file(self):
        if os.path.exists("events.json"):
            os.remove("events.json")

    def write_to_file(self, events, filename):
        
        frames = []

        if os.path.exists(filename):
            # Le o arquivo ja existente e copia os events
            with open(filename, "r") as file:
                frames = json.load(file)
        else:
            # Cria o arquivo e adiciona o FPS do video
            _ = open(filename, "x")
            frames.append({"fps": get_fps()})

        # Os novos events sao adicionados
        for item in events:
            frames.append(item.__dict__)        

        # Insere no arquivo
        with open(filename, "w") as file:
            json.dump(frames, file, indent=1)

    def group_frames_by_event(self, input_filename, output_filename, tolerance=1):

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