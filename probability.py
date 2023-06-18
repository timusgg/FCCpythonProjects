import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = [ball for ball, number in balls.items() for _ in range(number)]


    def draw(self, number):
        removedBalls = []  
        if number < len(self.contents):
            for _ in range(number):
                ball = random.choice(self.contents)
                removedBalls.append(ball)
                self.contents.remove(ball)
        else:    
            removedBalls = self.contents.copy()
            self.contents.clear()
        
        return removedBalls



def experiment(hat:Hat, expected_balls, num_balls_drawn, num_experiments):
    successfulDraws = 0
    for _ in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        removedBalls = hatCopy.draw(num_balls_drawn)
        successBalls = [ball for ball in expected_balls if ball in removedBalls and removedBalls.count(ball) >= expected_balls[ball]]
        if len(expected_balls) == len(successBalls):
            successfulDraws += 1
        
    return successfulDraws/num_experiments

        


    

hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":2},
                  num_balls_drawn=7,
                  num_experiments=10000)


print(probability)
