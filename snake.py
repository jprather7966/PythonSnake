# Ctrl + Shift + P, then select interpreter
#Choose an interpreter that works
import pygame

BLOCK_Size = 20
SNAKE_Color = (0, 255, 0)
APPLE_Color = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((600, 600))
pygame.display.set_caption('SNAKE!')


class Snake():
    def __init__(self, xcor, ycor):
        self.is_alive = True
        self.direction = "RIGHT"
        self.body = [(xcor, ycor),
                     (xcor - BLOCK_Size, ycor),
                     (xcor - BLOCK_Size * 2, ycor)]
    def show(self):
        for body_part in self.body:
            pygame.draw.rect(game_display, SNAKE_Color, pygame.Rect(body_part[0], body_part[1], BLOCK_Size, BLOCK_Size))
    def move(self):
        head_xcor = self.body[0][0]
        head_ycor = self.body[0][1]
        if self.direction == "RIGHT":
            new_xcor = head_xcor + BLOCK_Size
            self.body.insert(0, (new_xcor, head_ycor))
        elif self.direction == "LEFT":
            new_xcor = head_xcor - BLOCK_Size
            self.body.insert(0, (new_xcor, head_ycor))
        elif self.direction == "UP":
            new_ycor = head_ycor - BLOCK_Size
            self.body.insert(0, (head_xcor, new_ycor))
        elif self.direction == "DOWN":
            new_ycor = head_ycor + BLOCK_Size
            self.body.insert(0, (head_xcor, new_ycor))

        self.body.pop()

class Apple():
    def __init__(self):
        self.xcor = 30
        self.ycor = 80
    def show(self):
        pygame.draw.rect(game_display, APPLE_Color, pygame.Rect(self.xcor, self.ycor, BLOCK_Size, BLOCK_Size))

snake = Snake(145, 200)
apple = Apple()

# Main Game Loop
while snake.is_alive:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:   
            snake.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"
            elif event.key == pygame.K_UP:
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                snake.direction = "DOWN"

    game_display.blit(game_display, (0, 0))

    snake.move()

    game_display.fill((0, 0, 0))
    snake.show()
    apple.show()
    pygame.display.flip()
    clock.tick(12)

pygame.quit()