#!python
import json
import argparse
import sys
from datetime import datetime

class Hypothesis:
    '''
    this class represents a guess
    '''
    def __init__(self, name, hypothesis, confidence, notes, dtime):
        self.name = name
        self.hypothesis = hypothesis
        self.confidence = confidence
        self.notes = notes
        self.dtime = dtime

    def write_to_yml(self, page, data):
        with open(page, 'w') as file:
            yaml.dump(data, file)

    def read_the_yml(self):
        with open('guesses.yml', 'r') as stream:
            data = yaml.load(stream, Loader=yaml.Loader)
        return data

    @classmethod
    def write_to_json(self, page, data):
        with open(page, 'w') as file:
            json.dump(data, file)

    @classmethod
    def read_the_json(self):
        with open('guesses.json', 'r') as stream:
            data = json.load(stream)
        return data




usage = '''
validate [-h|--help]
         [--debug]
'''

if __name__ == '__main__':
    # noinspection PyTypeChecker
    #breakpoint()
    parser = argparse.ArgumentParser(
        prog="validate",
        usage=usage,
        description="Run syntax validation on all Janus specs in the .janus directory.")
    parser.add_argument(
        "--name",
        type=str,
        required=False,
        help="Give it a name.")
    parser.add_argument(
        "--hypothesis",
        type=str,
        required=False,
        help="Make your guess.")
    parser.add_argument(
        "--confidence",
        type=str,
        required=False,
        help="How confident are you?.")
    parser.add_argument(
        "--notes",
        type=str,
        required=False,
        help="What's the deets?")
    #args = parser.parse_args()
    if len(sys.argv) < 2:
        name = input("Name of entry : ")
    else:
        name = sys.argv[-1]
    if not "-d" in sys.argv:
        hypothesis = input("Enter your hypothesis : ")
        confidence = input("What's your confidence level? : ")
        notes = input("any notes, links, etc? : ")
        #date = input("(Optional) date: ")
        #dt_object = datetime.datetime.now()
        #if not date:
        #    date = "_".join([str(i) for i in [dt_object.year, dt_object.month, dt_object.day]])
        #time = ":".join([str(i) for i in [dt_object.hour, dt_object.minute]])
        thedatetime = datetime.now().isoformat(timespec='minutes')
        h = Hypothesis(name=name, hypothesis=hypothesis, confidence=confidence, notes=notes, dtime=thedatetime)
        data = h.read_the_json()
        data[h.name] = {'hypothesis': h.hypothesis, 'confidence': h.confidence, 'notes': h.notes, 'dtime': h.dtime}
    else:
        h = Hypothesis
        data = h.read_the_json()
        data.pop(sys.argv[-1])
    h.write_to_json('guesses.json', data)
