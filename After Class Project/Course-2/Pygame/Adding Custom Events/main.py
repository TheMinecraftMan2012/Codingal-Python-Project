import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 550, 450
MOVEMENT_SPEED = 7
font = pygame.font.Font(r"After Class Project\Course-2\Adding Custom Events\Poppins-Medium.ttf", 65)
background_image = pygame.transform.scale(pygame.image.load(r"Class Works\Course-2\Pygame\Sprite Collision\bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, changed_x_pos, changed_y_pos):
        self.rect.x = max(min(self.rect.x + changed_x_pos, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + changed_y_pos, SCREEN_HEIGHT - self.rect.height), 0)

sprite_group = pygame.sprite.Group()

enemy_sprite_1 = Sprite(pygame.Color('red'), 30, 60)
enemy_sprite_1.rect.x, enemy_sprite_1.rect.y = 30, 200
sprite_group.add(enemy_sprite_1)

enemy_sprite_2 = Sprite(pygame.Color('red'), 30, 60)
enemy_sprite_2.rect.x, enemy_sprite_2.rect.y = 435, 200
sprite_group.add(enemy_sprite_2)

player_sprite = Sprite(pygame.Color('grey'), 30, 60)
player_sprite.rect.x, player_sprite.rect.y = 235, 400
sprite_group.add(player_sprite)

goal_sprite = Sprite(pygame.Color('blue'), 30, 60)
goal_sprite.rect.x, goal_sprite.rect.y = 235, 30
sprite_group.add(goal_sprite)

running, flag, flag_state = True, False, ""
moving_to_435 = True
moving_to_30 = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_image, (0, 0))
    sprite_group.draw(screen)

    if not flag:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - (keys[pygame.K_LEFT])) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - (keys[pygame.K_UP])) * MOVEMENT_SPEED
        player_sprite.move(x_change, y_change)

        if moving_to_435:
            if enemy_sprite_1.rect.x < 435:
                enemy_sprite_1.rect.x += 8
            else:
                moving_to_435 = False  # Switch direction
        else:
            if enemy_sprite_1.rect.x > 30:
                enemy_sprite_1.rect.x -= 8
            else:
                moving_to_435 = True

        if moving_to_30:
            if enemy_sprite_2.rect.x > 30:
                enemy_sprite_2.rect.x -= 8
            else:
                moving_to_30 = False
        else:
            if enemy_sprite_2.rect.x < 435:
                enemy_sprite_2.rect.x += 8
            else:
                moving_to_30 = True

        if player_sprite.rect.colliderect(goal_sprite.rect):
            sprite_group.remove(enemy_sprite_1, enemy_sprite_2, goal_sprite)
            player_sprite.move(0, 0)
            flag_state = "win"
            flag = True

        if player_sprite.rect.colliderect(enemy_sprite_1.rect) or player_sprite.rect.colliderect(enemy_sprite_2.rect):
            sprite_group.remove(enemy_sprite_1, enemy_sprite_2, goal_sprite)
            player_sprite.move(0, 0)
            flag_state = "lose"
            flag = True
    
    if flag:
        text = font.render("You Win!" if flag_state == "win" else "You Lose!", True, pygame.Color('black'))
        screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, (SCREEN_HEIGHT - text.get_height()) // 2))

    pygame.display.flip()
    pygame.time.Clock().tick(90)

pygame.quit()