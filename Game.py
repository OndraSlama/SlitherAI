from World import *
from Snake import *
class Game:
    def __init__(self):
        self.world = World(self)
        self.snakes = []        
        self.fps = 1
        self.time = 0
        self.mousePosition = None

        for i in range(1):
            self.snakes.append(Snake(self, 10*i, 20*i))

    def Update(self, mousePos, fps, time):
        self.mousePosition = mousePos
        self.fps = max(fps, 1)
        self.time = time       
        self.world.Update()
        for snake in self.snakes:
            snake.Update()

    def CheckForCollisions(self):
        for snake in self.snakes:
            for otherSnake in self.snakes:
                if snake != otherSnake:
                    for part in otherSnake.body:
                        if snake.position.distance_squared_to(part) < (snake.radius + otherSnake.radius)**2:
                            snake.Die()
                            self.snakes.remove(snake)