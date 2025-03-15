import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((58, 58, 58))
pygame.display.set_caption("My first game screen")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()