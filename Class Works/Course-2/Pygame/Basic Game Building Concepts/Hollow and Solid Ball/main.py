import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption("Hollow and Solid Ball")

GREEN = (0, 255, 0)

pygame.draw.circle(screen, GREEN, (500 // 1.5, 500 // 2), 50)
pygame.draw.circle(screen, GREEN, (500 // 3, 500 // 2), 50, 3)

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()