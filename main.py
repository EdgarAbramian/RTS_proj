import pygame
from colors import *
import random


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def get_name(self):
        return self.text

    def render_text(self):
        t_surf = font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()

pygame.init()

font = pygame.font.SysFont(None, 100)
text_input_box = TextInputBox(100, 50, 300, font)
group = pygame.sprite.Group(text_input_box)

WINDOW_SIZE = (500, 400)
FPS = 50

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

X_player, Y_player = 225, 350
X_enemy, Y_enemy = 225, 0
X_enemy2, Y_enemy2 = 300, 0
X_good, Y_good = 400, 0
X_good2, Y_good2  = 100, 0

player = pygame.Rect(X_player, Y_player, 50, 50)
enemy = pygame.Rect(X_enemy, Y_enemy, 50, 50)
enemy2 = pygame.Rect(X_enemy2, Y_enemy2, 50, 50)
good = pygame.Rect(X_good, Y_good, 50, 50)
good2 = pygame.Rect(X_good2, Y_good2, 50, 50)
XP = 3
name = []

not_reg = True
hello_text = False
run = True
menu = True
play = False
game_over = False

while run:
    keys = pygame.key.get_pressed()
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 100)

    pygame.draw.rect(window, LIGHT_BLUE, player)
    pygame.draw.rect(window, RED, enemy)
    pygame.draw.rect(window, RED, enemy2)
    pygame.draw.rect(window, GREEN, good)
    pygame.draw.rect(window, GREEN, good2)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    if menu:
        window.fill(YELLOW)
        if not_reg:
            group.update(event_list)
            group.draw(window)
            window.blit(font.render("Name: ", True, WHITE), (10, 50))
            window.blit(font.render("Press enter to play  Go, go, run!", True, WHITE), (100, 200))
        if keys[pygame.K_RETURN]:
            print(text_input_box.text)
            name.append(text_input_box.text)
            not_reg = False
            play, menu = True, False

    if (play):
        if not XP:
            play = False
            game_over = True
        if ((good.colliderect(player) and Y_good == 350)
        or (good2.colliderect(player) and Y_good2 == 350)):
            XP += 1

        if ((enemy.colliderect(player) and Y_enemy == 350)
        or (enemy2.colliderect(player) and Y_enemy2 == 350)):
            XP -= 1

        if keys[pygame.K_LEFT]:
            X_player -= 8
            player = pygame.Rect(X_player, Y_player, 50, 50)
            window.fill(BLACK)
            pygame.draw.rect(window, RED, enemy)
        elif keys[pygame.K_RIGHT]:
            X_player += 8
            player = pygame.Rect(X_player, Y_player, 50, 50)
            window.fill(BLACK)
            pygame.draw.rect(window, RED, enemy)

        if Y_enemy <= 350:
            Y_enemy += 5
            enemy = pygame.Rect(X_enemy, Y_enemy, 50, 50)
        else:
            Y_enemy = 0
            X_enemy = random.randrange(0, 400, 50)
            enemy = pygame.Rect(X_enemy, Y_enemy, 50, 50)

        if Y_enemy2 <= 350:
            Y_enemy2 += 10
            enemy2 = pygame.Rect(X_enemy2, Y_enemy2, 50, 50)
        else:
            Y_enemy2 = 0
            X_enemy2 = random.randrange(0, 400, 50)
            enemy2 = pygame.Rect(X_enemy2, Y_enemy2, 50, 50)

        if Y_good <= 350:
            Y_good += 5
            good = pygame.Rect(X_good, Y_good, 50, 50)
        else:
            Y_good = 0
            X_good = random.randrange(0, 400, 50)
            good = pygame.Rect(X_good, Y_good, 50, 50)

        if Y_good2 <= 350:
            Y_good2 += 10
            good2 = pygame.Rect(X_good2, Y_good2, 50, 50)
        else:
            Y_good2 = 0
            X_good2 = random.randrange(0, 400, 50)
            good = pygame.Rect(X_good2, Y_good2, 50, 50)


        window.fill(BLACK)
        pygame.draw.rect(window, RED, enemy)
        pygame.draw.rect(window, RED, enemy2)
        pygame.draw.rect(window, LIGHT_BLUE, player)
        pygame.draw.rect(window, GREEN, good)
        pygame.draw.rect(window, GREEN, good2)

        score = font.render('XP = ' + str(XP), True, WHITE)
        window.blit(score, (10, 10))

    if (game_over):
        window.fill(GRAY)
        window.blit(font1.render("GAME OVER!", True, WHITE), (20, 200))
    pygame.display.update()

    clock.tick(FPS)
