import pygame
from Game import *
from Graphics import *
from Constants import *
import pygame.math as math 

pygame.init()

cameraPosition = math.Vector2(0, 0)
zoom = 1

graphics = Graphics(windowWidth, windowHeight, pixelScale)
game = Game()
gameSpeed = 1

clock = pygame.time.Clock()
timePassed = 0
fps = 0
running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.snakes[0].sprinting = True
            if event.button == 4: zoom = min(zoom * 1.1, maxZoom)
            if event.button == 5: zoom = max(zoom * 1/1.1, minZoom)
        
        if event.type == pygame.MOUSEBUTTONUP:
            game.snakes[0].sprinting = False
        

    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]: cameraPosition.x -= 0.5/zoom
    # if keys[pygame.K_RIGHT]: cameraPosition.x += 0.5/zoom
    # if keys[pygame.K_UP]: cameraPosition.y -= 0.5/zoom
    # if keys[pygame.K_DOWN]: cameraPosition.y += 0.5/zoom
    for t in range(gameSpeed):
        timePassed = pygame.time.get_ticks()
        if timePassed > 1000:
            mousePosition = graphics.GetWorldMouse(pygame.mouse.get_pos())
            fps = clock.get_fps()
            game.Update(mousePosition, fps, timePassed * gameSpeed)
            
            cameraPosition = game.snakes[0].position
        

    if timePassed > 1000:
        graphics.DrawEverything(game, cameraPosition, zoom*2/game.snakes[0].radius)      
    clock.tick(60)
    # print(fps)

pygame.quit()


