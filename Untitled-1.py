from pygame import *
from random import randint
from time import time

back = (255, 204, 229)
mw = display.set_mode((500, 500))
mw.fill(back)

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y < 700:
            self.rect.y += self.speed


#ball= ("ball.png.png", 100, 200, 10, 10)
platform= Player("platforn.png", 200, 330, 100, 30, 7)


game = True
finish = False
clock = time.Clock()
FSP = 60
while True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.fill()
    platform.fill()
                
    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x <0:
        speed_x *= -1

    if move_right:
        platform.rect.x += 3
    if move_left:   
        platform.rect.x -= 3

    if ball.rect.y > 350:
        time_text = Label(150, 150, 50, 50, back)
        time_text.set_text("YOU LOSE", 60, (250,0,0))
        time_text.draw(10, 10)
        game_over = True

    ball.rect.x += speed_x
    ball.rect.y += speed_y
    ball.draw()
    platform.draw()

if finish != True:
    ball.draw()
    platform.draw()
        
    pygame.display.update()
    clock.tick(40)
pygame.display.update()