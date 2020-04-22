import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))

# Import Images
background_img = pygame.image.load('Tic-tac-toe.png')
X_sml = pygame.image.load('X_sml.JPG').convert()
O = pygame.image.load('O_sml.JPG')

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # screen.blit(X_sml, (50,50))
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] in range(0,191) and event.pos[1] in range(0,194):
                    screen.blit(X_sml, (50,50))
                    pygame.display.flip()

    screen.blit(background_img, (0,0))
    pygame.display.update()
    
    # screen.blit(O, (255,50))
    

# kpad1 = from (0,417) to (191,600)
# kpad2 = from (225,417) to (378,600)
# kpad3 = from (410,417) to (600,600)
# kpad4 = from (0,227) to (191,385)
# kpad5 = from (225,227) to (378,385)
# kpad6 = from (410,227) to (600,385)
# kpad7 = from (0,0) to (191,194)
# kpad8 = from (225,0) to (378,194)
# kpad9 = from (410,0) to (600,194)



# Change to check something




pygame.quit()