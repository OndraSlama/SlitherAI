from Constants import *
import random
import pygame.math as math
class World:
    def __init__(self, game):
        self.game = game
        self.width = worldWidth
        self.height = worldWidth
        self.food = []
        self.regions = []
        self.lastFoodCheck = 0

        xRegions = self.width//regionSize
        yRegions = self.height//regionSize

        for xi in range(xRegions):
            for yi in range(yRegions):
                regionWidth = self.width/xRegions
                regionHeight = self.height/yRegions
                regionRect = [xi*regionWidth - self.width/2, yi*regionHeight  - self.height/2, regionWidth, regionHeight]
                self.regions.append(Region(self, regionRect))

    def Update(self):
        if self.game.time - self.lastFoodCheck > resetFoodInterval*1000:
            self.lastFoodCheck = self.game.time
            for region in self.regions:
                region.CheckFood()

    def DropFood(self, x, y, nutritions):
        self.food.append(Food(None, x, y, nutritions))

class Food:
    def __init__(self, region, x, y, nut):
        self.region = region
        self.nutritions = nut
        self.position = math.Vector2(x, y)
        

class Region:
    def __init__(self, world, regionPosition):
        self.world = world 
        self.regionPosition = regionPosition
        self.food = []
        self.CreateFood(random.randrange(round(foodInRegion*0.8), round(foodInRegion*1.2), 1))

    def CreateFood(self, noOfFood):
        for i in range(noOfFood):
            foodXPos = random.randrange(round(self.regionPosition[0] * 100), round((self.regionPosition[0] + self.regionPosition[2])*100), 1)/100
            foodYPos = random.randrange(round(self.regionPosition[1] * 100), round((self.regionPosition[1] + self.regionPosition[3])*100), 1)/100
            food = Food(self, foodXPos, foodYPos, random.randrange(round(foodNutritions*0.5), round(foodNutritions*1.5), 1))
            self.food.append(food)
            self.world.food.append(food)

    def CheckFood(self):
        if len(self.food) < foodInRegion*0.8:
            self.CreateFood(random.randrange(1, round(foodInRegion*0.4), 1))

