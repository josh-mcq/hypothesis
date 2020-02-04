import json
import argparse
import guess
import sys



def read_the_json(page):
    with open(page, 'r') as stream:
        data = json.load(stream)
    return data

class Answer:
    '''
    this class represents a guess
    '''
    def __init__(self, name, hypothesis, confidence, notes, dtime, result, explanation, points, lessons):
        self.name = name
        self.hypothesis = hypothesis
        self.confidence = confidence
        self.notes = notes
        self.dtime = dtime
        self.result = result
        self.explanation = explanation
        self.points = points
        self.lessons = lessons

    @classmethod
    def read_the_json(self, page):
        with open(page, 'r') as stream:
            data = json.load(stream)
        return data

    @classmethod
    def write_to_json(self, page, data):
        with open(page, 'w') as file:
            json.dump(data, file)



if __name__ == '__main__':
    # noinspection PyTypeChecker
    #breakpoint()
    if len(sys.argv) < 2:
        name = input("Name of entry : ")
    else:
        name = sys.argv[-1]
    if not "-d" in sys.argv:
        guesses = Answer.read_the_json('guesses.json')
        my_guess = guesses[name]
        print(my_guess['hypothesis'])
        result = input("result(correct, incorrect, mu): ")
        explanation = input("explanation: ")
        lessons = input("lessons: ")
        #guesses = read_the_('guesses.json')
        my_guess = guesses[name]
        a = Answer(name=name, hypothesis=my_guess['hypothesis'], confidence=my_guess['confidence'], notes=my_guess['notes'], dtime=my_guess['dtime'], result=result, explanation=explanation, points=0, lessons=lessons)
        guesses.pop(name)
        a.write_to_json('guesses.json', guesses)
        data = read_the_json('answers.json')
        data[name] = {'hypothesis': a.hypothesis, 'confidence': a.confidence, 'notes': a.notes, 'dtime': a.dtime, 'result': a.result, 'explanation': a.explanation, 'points': a.points, 'lessons': a.lessons}
    else:
        a = Answer
        data = a.read_the_json('answers.json')
        data.pop(sys.argv[-1])
    a.write_to_json('answers.json', data)