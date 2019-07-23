# Ctrl + Shift + P, then select interpreter
#Choose an interpreter that works
import pygame
import random 

#Game Settings
GAME_SIZE = 600 
BLOCK_SIZE = GAME_SIZE / 40
SNAKE_COLOR = (0, 255, 0)
APPLE_Color = (255, 0, 0)
BACKGROUND_COLOR = (0,0,0)

pygame.init()
SCORE_FONT = pygame.font.SysFont('Arial', int(GAME_SIZE * 0.065) , True)
clock = pygame.time.Clock()
game_display = pygame.display.set_mode((GAME_SIZE, GAME_SIZE))
pygame.display.set_caption('SNAKE!')
class Game_Object():
    def __init__(self,xcor,ycor, color):
        self.xcor = xcor
        self.ycor = ycor
        self.color = color
    def show_as_circle(self):
        pygame.draw.circle(game_display, self.color, (int (self.xcor + BLOCK_SIZE/2) , int(self.ycor + BLOCK_SIZE/2)), int (BLOCK_SIZE / 2))
    def show_as_square(self):
        pygame.draw.rect(game_display, self.color, pygame.Rect(self.xcor, self.ycor, BLOCK_SIZE, BLOCK_SIZE))


class Snake():
    def __init__(self, xcor, ycor):
        self.is_alive = True
        self.score = 0
        self.direction = "RIGHT"
        self.body = [Game_Object(xcor, ycor,SNAKE_COLOR),
                     Game_Object(xcor - BLOCK_SIZE, ycor,SNAKE_COLOR),
                     Game_Object(xcor - BLOCK_SIZE * 2, ycor,SNAKE_COLOR)]
        self.previous_last_tail = self.body[len(self.body) - 1]

    def grow(self):
        self.body.append(self.previous_last_tail)

    def show(self):
        for body_part in self.body:
            body_part.show_as_square()

    def set_direction_right(self):
        if self.direction != "LEFT":
            self.direction = "RIGHT"

    def set_direction_left(self):
        if self.direction != "RIGHT":
            self.direction = "LEFT"

    def set_direction_up(self):
        if self.direction != "DOWN":
            self.direction = "UP"

    def set_direction_down(self):
        if self.direction != "UP":
            self.direction = "DOWN"

    def move(self):
        head_xcor = self.body[0].xcor
        head_ycor = self.body[0].ycor
        if self.direction == "RIGHT":
            head_xcor = head_xcor + BLOCK_SIZE
        elif self.direction == "LEFT":
            head_xcor = head_xcor - BLOCK_SIZE
        elif self.direction == "UP":
            head_ycor = head_ycor - BLOCK_SIZE
        elif self.direction == "DOWN":
            head_ycor = head_ycor + BLOCK_SIZE
        
        new_snake_head = Game_Object(head_xcor,head_ycor,SNAKE_COLOR)
        self.body.insert(0,new_snake_head)
        self.previous_last_tail = self.body.pop()

    def has_collided_with_wall(self):
        head = self.body[0]
        if head.xcor < 0 or head.ycor < 0 or head.xcor + BLOCK_SIZE > GAME_SIZE or head.ycor + BLOCK_SIZE > GAME_SIZE:
            return True
        return False
    def has_collided_with_self(self):
        head = self.body[0]
        for i in range(1, len(self.body)):
            if head.xcor == self.body[i].xcor and head.ycor == self.body[i].ycor:
                return True
        return False
            
    def has_eaten_apple(self, apple_object):
        head = self.body[0]
        if head.xcor == apple_object.body.xcor and head.ycor == apple_object.body.ycor:
             return True 
        return False    

class Apple():
    def __init__(self, snake_body):
        self.body = self.get_rnd_game_object()
        

        while self.apple_is_on_snake(snake_body):
            self.body = self.get_rnd_game_object()
        
    def get_rnd_game_object(self):
        xcor = random.randrange(0, GAME_SIZE / BLOCK_SIZE) * BLOCK_SIZE
        ycor = random.randrange(0, GAME_SIZE / BLOCK_SIZE) * BLOCK_SIZE
        return Game_Object(xcor, ycor, APPLE_Color)
    def apple_is_on_snake(self,snake_body):
        for snake_part in snake.body:
            if snake_part.xcor == self.body.xcor and snake_part.ycor == self.body.ycor:
                return True
        return False
    def show(self):
        self.body.show_as_circle()


def handle_events():
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:   
            snake.is_alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.set_direction_left()
            elif event.key == pygame.K_RIGHT:
                snake.set_direction_right()
            elif event.key == pygame.K_UP:
                snake.set_direction_up()
            elif event.key == pygame.K_DOWN:
                snake.set_direction_down()
            elif event.key == pygame.K_p:
                pause_game()
def pause_game():
    game_is_Paused = True
    while game_is_Paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                snake.is_alive == False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_is_Paused = False
                elif event.key == pygame.K_ESCAPE:
                    snake.is_alive = False
                    game_is_Paused = False
            pygame.display.update()
            clock.tick(5)
snake = Snake(BLOCK_SIZE * 5, BLOCK_SIZE * 5)
apple = Apple(snake.body)

# Main Game Loop
while snake.is_alive:

    handle_events()
    game_display.blit(game_display, (0, 0))

    snake.move()
    if snake.has_collided_with_wall() or snake.has_collided_with_self():
        snake.is_alive = False
    if snake.has_eaten_apple(apple):
        snake.score += 1
        snake.grow()
        apple = Apple(snake.body)

    game_display.fill(BACKGROUND_COLOR)
    snake.show()
    apple.show()

    score_text = SCORE_FONT.render(str(snake.score),False, (255,255,255))
    game_display.blit(score_text,(0,0))

    pygame.display.flip()
    clock.tick(12)

pygame.quit()