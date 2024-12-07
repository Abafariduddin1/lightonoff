import pygame
import sys
import time

pygame.init()

font = pygame.font.SysFont("Italic", 60)

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Light Animation")

lighton = pygame.image.load("L.4/lighton.png")
lightons = pygame.transform.scale(lighton, (700, 700))

lightoff = pygame.image.load("L.4/lightoff.png")
lightoffs = pygame.transform.scale(lightoff, (700, 700))

while True:
    screen.blit(lightoffs, (0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            txt_on = font.render("The light is ON!", True, "black")
            screen.blit(lightons, (0,0))
            screen.blit(txt_on, (150, 50))
            pygame.display.update()
    

        if event.type == pygame.MOUSEBUTTONUP:
            screen.blit(lightoffs, (0, 0))
            txt_off = font.render("The light is OFF!", True, "black")
            screen.blit(txt_off, (150, 50))
            pygame.display.update()    
 