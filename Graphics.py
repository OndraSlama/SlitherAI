import pygame
import pygame.gfxdraw
import pygame.math as math

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

width = 1200
height = 800

class Graphics:
    def __init__(self, w, h, s):
        self.pixelWidth = w 
        self.pixelHeight = h
        self.scale = s
        self.window = pygame.display.set_mode((self.pixelWidth, self.pixelHeight))

        self.camX = 0
        self.camY = 0
        self.zoom = 1

        pygame.display.set_caption('Slither')


    def DrawEverything(self, game, cam, zoom):
        self.camX = cam.x
        self.camY = cam.y
        self.zoom = zoom        

        # Draw background
        self.window.fill(BLACK)


        # # Draw regions
        # for region in game.world.regions:
        #     rect = [self.GetX(region.regionPosition[0]), self.GetY(region.regionPosition[1]), self.Scale(region.regionPosition[2]), self.Scale(region.regionPosition[3])]
        #     pygame.draw.rect(self.window, BLUE, rect , max(self.Scale(.1), 1))
        
        # Draw boundaries
        rect = [self.GetX(-game.world.width/2), self.GetY(-game.world.height/2), self.Scale(game.world.width), self.Scale(game.world.height)]
        pygame.draw.rect(self.window, RED, rect , max(self.Scale(1), 4))

        # Draw food
        for food in game.world.food:
            posX = self.GetX(food.position.x)
            posY = self.GetY(food.position.y)
            rad = self.Scale(food.nutritions/15)
            if abs(posX - self.pixelWidth/2) < self.pixelWidth/2 and  abs(posY - self.pixelHeight/2) < self.pixelHeight/2:
                pygame.gfxdraw.aacircle(self.window, posX, posY, rad, GREEN)
                pygame.gfxdraw.filled_circle(self.window, posX, posY, rad, GREEN)

        # Draw snakes
        for snake in game.snakes:
            rad = self.Scale(snake.radius)
            posX = self.GetX(snake.position.x)
            posY = self.GetY(snake.position.y)  
            pygame.gfxdraw.aacircle(self.window, posX, posY, rad, RED)
            pygame.gfxdraw.filled_circle(self.window, posX, posY, rad, RED)
            
            for part in snake.body:
                posX = self.GetX(part.x)
                posY = self.GetY(part.y)
                if abs(posX - self.pixelWidth/2) < self.pixelWidth/2 and  abs(posY - self.pixelHeight/2) < self.pixelHeight/2:
                    pygame.gfxdraw.aacircle(self.window, posX, posY, rad, RED)
                    pygame.gfxdraw.filled_circle(self.window, posX, posY, rad, RED)

        pygame.display.update()

    def GetX(self, x):
        return round((x * self.scale - self.camX * self.scale)*self.zoom + self.pixelWidth/2)

    def GetY(self, y):
        return round((y * self.scale - self.camY * self.scale)*self.zoom + self.pixelHeight/2)

    def Scale(self, dist):
        return round(dist*self.scale*self.zoom)

    def GetWorldMouse(self, mousePos):
        x = (mousePos[0] - self.pixelWidth/2)/(self.zoom * self.scale) + self.camX
        y = (mousePos[1] - self.pixelHeight/2)/(self.zoom * self.scale) + self.camY
        return math.Vector2(x,y)