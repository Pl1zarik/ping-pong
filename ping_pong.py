from pygame import *
import pygame

W =  900
H = 500

window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (144, 165, 247)
window.fill(back)

clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 50)

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 100:
            self.rect.y += self.speed
    
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H - 100:
            self.rect.y += self.speed

racet_l = Player('racket.png', 10, H//2, 25, 100, 10)
racet_r = Player('racket.png', W - 35, H//2, 25, 100, 10)
ball = GameSprite('ball.png', W//2, H//2, 50, 50, 0)

speed_x = 5
speed_y = 5

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        racet_l.update_l()
        racet_r.update_r()

        racet_l.reset()
        racet_r.reset()
        ball.reset()

        if ball.rect.y > H - 50 or ball.rect.y < 0 :
            speed_y *= -1

        if sprite.collide_rect(racet_l, ball) and speed_x < 0:
            speed_y *= -1
            speed_x *= -1

        if sprite.collide_rect(racet_r, ball) and speed_x > 0:
            speed_y *= -1
            speed_x *= -1

        u_lose_l = font.render('Игрок 1 проиграл!!!', 1, (139, 0, 0))
        u_lose_r = font.render('Игрок 2 проиграл!!!', 1, (139, 0, 0))
        
        if ball.rect.x > W:
            window.blit(u_lose_r, (270, 200))
            finish = True
        
        if ball.rect.x < 0:
            window.blit(u_lose_l, (270, 200))
            finish = True
    else:
        restart_game = font.render('Press space restart game!', True, (0, 0, 0))
        window.blit(restart_game, (270, 250))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            ball.rect.y = H//2
            ball.rect.x = W//2
            finish = False
    display.update()
    clock.tick(FPS)    
