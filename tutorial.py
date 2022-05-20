import os
import pygame
from pygame import Rect
from pygame.math import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'

class GameState():
    def __init__(self):
        self.worldSize = Vector2(16,10)
        self.tankPos = Vector2(0,0)


    def update(self,moveTankCommand):
        self.tankPos += moveTankCommand

        if self.tankPos.x < 0:
            self.tankPos.x = 0
        elif self.tankPos.x >= self.worldSize.x:
            self.tankPos.x = self.worldSize.x - 1

        if self.tankPos.y < 0:
            self.tankPos.y = 0
        elif self.tankPos.y >= self.worldSize.y:
            self.tankPos.y = self.worldSize.y - 1

class UserInterface():
    def __init__(self):
        pygame.init()
        
        self.gameState = GameState()
        
        self.cellSize = Vector2(64,64)
        self.unitsTexture = pygame.image.load("units.png")
        
        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x),int(windowSize.y)))
        
        
        pygame.display.set_caption("Rylan's Rangers")
        pygame.display.set_icon(pygame.image.load("icon.png"))
        self.moveTankCommand = Vector2(0,0)
        
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        
        self.moveTankCommand = Vector2(0,0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveTankCommand.x = 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveTankCommand.x = -1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveTankCommand.y = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveTankCommand.y = -1
                    
    def update(self):
        self.gameState.update(self.moveTankCommand)

    def render(self):
        self.window.fill((0,0,0))
        
        # Tank base
        spritePoint = self.gameState.tankPos.elementwise()*self.cellSize
        texturePoint = Vector2(1,0).elementwise()*self.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
        self.window.blit(self.unitsTexture,spritePoint,textureRect)

        pygame.display.update()       

    def run(self):    
        while self.running:
            self.processInput()
            self.update()
            self.render()        
            self.clock.tick(60)
            
UserInterface = UserInterface()
UserInterface.run()

pygame.quit()
