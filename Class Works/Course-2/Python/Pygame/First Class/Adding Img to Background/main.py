import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding Image to background")

bg_image = pygame.transform.scale(pygame.image.load(r"I:\Codingal Python\2\Codingal-Python-Project\Class Works\Course-2\Pygame\First Class\Adding Img to Background\background.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
peng_image = pygame.transform.scale(pygame.image.load(r"I:\Codingal Python\2\Codingal-Python-Project\Class Works\Course-2\Pygame\First Class\Adding Img to Background\penguin.png").convert_alpha(), (200, 200))
peng_rect = peng_image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color("black"))
text_rect = text.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
    
        display_surface.blit(bg_image, (0, 0))
        display_surface.blit(peng_image, peng_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()