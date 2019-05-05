from Constants import *
import random
import pygame.math as math

class Snake:
    def __init__(self, game, x, y):
        self.game = game
        self.aiControlled = False
        self.position = math.Vector2(x,y)
        self.velocity = math.Vector2(1, 0)
        self.sprinting = False
        self.speed = snakeSpeed
        self.length = snakeInitialLength
        self.traveled = 0
        self.food = snakeInitialLength
        self.newPartCost = 30
        self.body = []
        self.radius = 1
        self.lastEaten = 0
        self.lastFoodDropped = 0

        self.body.append(math.Vector2(x,y))

    def Update(self):
        if self.aiControlled:
            pass
        else:
            differenceAngle = self.velocity.angle_to(self.game.mousePosition - self.position)
            rotateAngle = self.ClampAngle(differenceAngle)            

        if self.sprinting and self.length > 100:
            self.speed = snakeSpeed * 2.5
        else:
            self.speed = snakeSpeed
            self.sprinting = False

        self.velocity = self.velocity.rotate(rotateAngle)
        self.velocity = self.velocity.normalize()*self.speed
        
        print(self.length)
        self.Move()

        if self.game.time - self.lastEaten > 100: #eat every 100 miliseconds
            self.Eat()
            self.lastEaten = self.game.time

        self.UpdateLength()


    def Move(self):       
        self.position += self.velocity/self.game.fps
        self.traveled += self.speed/self.game.fps
        self.Join()

        if self.sprinting:
            self.food -= sprintCost/self.game.fps
            self.length -= sprintCost/self.game.fps
            if self.game.time - self.lastFoodDropped > 250:
                self.game.world.DropFood(self.body[-1].x, self.body[-1].y, sprintCost/4)
                self.lastFoodDropped = self.game.time
        else:
                self.lastFoodDropped = self.game.time

        
    def Join(self):
        distanceBetweenParts = self.radius*.8
        for i in range(len(self.body)):
            velocity = None

            if i == 0:
                previous = self.position                
            else:
                previous = self.body[i-1]             

            offset = previous - self.body[i]
            offset.scale_to_length(distanceBetweenParts)
            self.body[i] = previous - offset


    def Eat(self):
        for food in self.game.world.food:
            if food.position.distance_squared_to(self.position) < (self.radius * 1.2)**2:
                self.food += food.nutritions
                self.length += food.nutritions
                self.game.world.food.remove(food)
                if food.region is not None:
                    food.region.food.remove(food)
        

    def UpdateLength(self):
        if self.food >= self.newPartCost:
            self.body.append(math.Vector2(self.body[-1].x, self.body[-1].y))
            self.food -= self.newPartCost
            self.newPartCost *= greedFactor
            self.radius *= sizeGrowFactor

        if self.food < 0:
            self.body.pop()
            self.newPartCost *= 1/greedFactor
            self.radius *= 1/sizeGrowFactor
            self.food += self.newPartCost*0.95

    # def Die(self):
    #     for part in self.body:
    #         for i in range()
    #         xPos
           


    def ClampAngle(self, angle):
        if angle  > 180: angle -= 360
        if angle  < -180: angle += 360
        return max(min(turningAngle/self.game.fps/self.radius, angle), -turningAngle/self.game.fps/self.radius)
            


# class Part:
#     def __init__(self):
#         self.position


