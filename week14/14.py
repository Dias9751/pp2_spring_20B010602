#TASK 2
import random, sys
import pygame, time
import psycopg2
from config import config
l = input('login: ')
p = input('password: ')

sql_user = "select * from users;"
sql_score = "select * from game_snake"
conn = None
try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sql_user)
    inf = cur.fetchall()
    cur.execute(sql_score)
    inf2 = cur.fetchall()
    conn.commit()
    cur.close()
except Exception as e:
    print(str(e))
finally:
    if conn is not None:
        conn.close()

cnt = 0
for row in inf:
    if row[1] == l and row[2] == p:
         cnt += 1
    print(row[1], row[2])

for row in inf2:
    s_level = row[2]
    s_speed = row[3]
    s_score = row[4]
    print(row[0], row[1], row[2], row[3], row[4])


if cnt > 0:
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    class Snake:
        def __init__(self, x, y, speed):
            self.size = 1
            self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
            self.radius = 10
            self.dx = 5  # Right.
            self.dy = 0
            self.is_add = False
            self.speed = speed

        def draw(self):
            for element in self.elements:
                pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

        def add_to_snake(self):
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False
            if self.size % 3 == 0:
                self.speed += 10

        def move(self):
            if self.is_add:
                self.add_to_snake()

            for i in range(self.size - 1, 0, -1):
                self.elements[i][0] = self.elements[i - 1][0]
                self.elements[i][1] = self.elements[i - 1][1]

            self.elements[0][0] += self.dx
            self.elements[0][1] += self.dy
            return (self.elements[0][0], self.elements[0][1])

        def eat(self, foodx, foody):
            x = self.elements[0][0]
            y = self.elements[0][1]
            if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
                return True
            return False


    class Food:
        def __init__(self):
            self.x = random.randint(400, 400)
            self.y = random.randint(400, 400)

        def gen(self):
            self.x = random.randint(25, 765)
            self.y = random.randint(25, 625)

        def draw(self):
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))
            return (self.x, self.y)

    class Food_Big:
        def __init__(self):
            self.x = random.randint(300, 300)
            self.y = random.randint(300, 300)
        def gen(self):
            self.x = random.randint(25, 765)
            self.y = random.randint(25, 625)

        def draw(self):
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 20, 20))
            return (self.x, self.y)

    class Sure:
        def draw(self):
            pygame.draw.rect(screen, (216, 160, 216), (10, 10, 780, 650), 15)
        
        def draw_line(self):
            pygame.draw.line(screen, (216, 160, 216), [400, 80], [400,550], 15)
    
    def update_user(level, speed, score, username):
        sql = """
        update game_snake
        set level = %s,
        speed = %s,
        score = %s
        where username = %s;
        """
        conn = None
        updated_rows = 0
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (level, speed, score, username))
            updated_rows = cur.rowcount
            conn.commit()
            cur.close()
        except Exception as e:
            print(str(e))
        finally:
            if conn is not None:
                conn.close()

    snake1 = Snake(100, 100, s_speed)
    food = Food()
    big = Food_Big()
    sure = Sure()
    running = True
    FPS = 30
    d = 5
    clock = pygame.time.Clock()

    level = s_level
    font = pygame.font.SysFont("Verdana", 40)
    game_over = font.render("Game Over", True, (255, 255, 255))

    cnt = 0
    score = s_score
    second1 = int(round(time.time() * 1000))

    while running:
        clock.tick(snake1.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_RIGHT and snake1.dx != -d:
                    snake1.dx = d
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != d:
                    snake1.dx = -d
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != d:
                    snake1.dx = 0
                    snake1.dy = -d
                if event.key == pygame.K_DOWN and snake1.dy != -d:
                    snake1.dx = 0
                    snake1.dy = d
  
        
        if snake1.eat(food.x, food.y):
                snake1.is_add = True
                food.gen()
                cnt += 1
                score += random.randint(1, 10)
        
        if snake1.eat(big.x, big.y):
                food.gen()
                cnt += 0.1
                score += random.randint(1, 10)

        if cnt >= 3:
                level += 1
                cnt = 0
                big.gen()
                big.draw()
                update_user(level, snake1.speed, score, 'admin')


        x2, y2  = snake1.move()
        if x2 <= 24 or x2 >= 772 or y2 <= 24 or y2 >= 640:
                time.sleep(3)
                pygame.quit()
                sys.exit()
        if level >2 and x2 == 400 and y2>80 and y2< 550:
                time.sleep(3)
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        snake1.draw()
        font_level = font.render(f"Level:{level}", True, (255,255,255))
        screen.blit(font_level, (30,670))
        font_score = font.render(f"Score:{score}", True, (255,255,255))
        screen.blit(font_score, (500,670))
        
        if cnt == 0 and score != 0:
                x1, y1 = big.draw()
        else:
                x1, y1 = food.draw()
        if snake1.dx == x1 or snake1.dy == y1:
                food.draw()
        second2 = int(round(time.time() * 1000))
        if abs(second2 - second1)>= 10000:
                food.gen()
                second1 = second2
        sure.draw()
        if level > 2: 
                sure.draw_line()
        pygame.display.flip()

    pygame.quit()
else:
    print("Login or password is error")
                
                 
