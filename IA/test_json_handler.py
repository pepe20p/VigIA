import pytest
from utils import *
from Event import *
from EventDetector import *
from FileHandler import *

def test_write_to_file():
    handler = FileHandler()
    events = [Event(30, [ "Event A" ]), Event(60, [ "Event B" ])]
    output = "output_test.json"

    handler.writeToFile(events, output)

    with open(output, "r") as file:
            result = json.load(file)

    assert result[0]["fps"] == 0.0
    assert result[1]["frame"] == 30
    assert result[1]["events"] == ["Event A"]
    assert result[2]["frame"] == 60
    assert result[2]["events"] == ["Event B"]

def test_event_grouping():
    input = "input_test.json" 
    output = "output_test.json"
    handler = FileHandler()

    handler.groupFramesByEvent(input, output, tolerance=5)

    with open(output, "r") as file:
            result = json.load(file)
    
    assert result == [
            {
                "fps": 29.97002997002997
            },
            {
                "event": "car",
                "frames": [(24, 30), (58, 59), (87, 88), (116, 146), (174, 175), (203, 204), (232, 233), (261, 262)]
            },
            {
                "event": "person",
                "frames": [(116, 291), (319, 320), (348, 349), (377, 378), (406, 407), (435, 436), (464, 465), (493, 494), (522, 522)]
            },
            {
                "event": "bicycle",
                "frames": [(174, 204), (232, 262), (290, 291)]
            }
        ]
