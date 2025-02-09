import pygame
import sys
import random

pygame.init()


width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Морской бой")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GRAY = (200, 200, 200)
GRID_SIZE = 50
CELL_SIZE = 50


def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, BLACK, (x, y, width, height))
    text_surface = font.render(text, 1, WHITE)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


grid_positions = []

def get_grid_positions(rect):
    global grid_positions
    for x in range(rect.left // CELL_SIZE, (rect.right + CELL_SIZE - 1) // CELL_SIZE):
        for y in range(rect.top // CELL_SIZE, (rect.bottom + CELL_SIZE - 1) // CELL_SIZE):
            if (x, y) not in grid_positions:
                grid_positions.append((x, y))
    return grid_positions



def move_image(rect, dx, dy):
    rect.x += dx
    rect.y += dy


WIDTH, HEIGHT = 1000, 1000
GRID_SIZE = 11
CELL_SIZE = 50

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

grid_positions2 = []
k2 = 20
k1 = 20

def get_grid_positions2(rect):
    global grid_positions2
    for x in range(rect.left // CELL_SIZE, (rect.right + CELL_SIZE - 1) // CELL_SIZE):
        for y in range(rect.top // CELL_SIZE, (rect.bottom + CELL_SIZE - 1) // CELL_SIZE):
            if (x, y) not in grid_positions2:
                grid_positions2.append((x, y))
    return grid_positions2

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False

def create_board():
    global grid_positions2
    board = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    positions = []
    positions.extend(grid_positions2)
    for x, y in positions:
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            board[y][x].is_mine = True

    return board


def create_board2():
    global grid_positions
    board2 = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    positions = []
    positions.extend(grid_positions)
    for x, y in positions:
        board2[y][x].is_mine = True

    return board2


def draw_board(screen, board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell = board[y][x]
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE)

            if cell.is_revealed:
                if cell.is_mine:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, BLACK, rect, 1)


def draw_board2(screen, board2):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell = board2[y][x]
            rect = pygame.Rect(700 + x * CELL_SIZE, y * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE)

            if cell.is_revealed:
                if cell.is_mine:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, BLACK, rect, 1)


class Character:
    def __init__(self):
        self.images = [pygame.image.load(f'elf{i}.png') for i in range(1, 11)]
        self.current_frame = 0
        self.rect = self.images[0].get_rect(center=(500, 800))
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.images)
            self.frame_counter = 0

    def draw(self, surface):
        surface.blit(self.images[self.current_frame], self.rect)


class Star:
    def __init__(self, x, y):
        self.size = random.randint(5, 15)
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-5, -1)
        self.gravity = 0.1

    def move(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 1000 or self.x < 0 or self.x > 1000:
            return False
        return True

    def draw(self, surface):
        pygame.draw.circle(surface,YELLOW, (int(self.x), int(self.y)), self.size)


class Star2:
    def __init__(self, x, y):
        self.size = random.randint(5, 15)
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-5, -1)
        self.gravity = 0.1

    def move(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 1000 or self.x < 0 or self.x > 1000:
            return False
        return True

    def draw(self, surface):
        pygame.draw.circle(surface,RED, (int(self.x), int(self.y)), self.size)


class Star3:
    def __init__(self, x, y):
        self.size = random.randint(5, 15)
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-5, -1)
        self.gravity = 0.1

    def move(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 1000 or self.x < 0 or self.x > 1000:
            return False
        return True

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), self.size)


class Star4:
    def __init__(self, x, y):
        self.size = random.randint(5, 15)
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-3, 3)
        self.speed_y = random.uniform(-5, -1)
        self.gravity = 0.1

    def move(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 1000 or self.x < 0 or self.x > 1000:
            return False
        return True

    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y)), self.size)


class Cell2:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.neighbor_mines = 0



def create_board3():
    board = [[Cell2() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


    mines_placed = 0
    while mines_placed < 20:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if not board[y][x].is_mine:
            board[y][x].is_mine = True
            mines_placed += 1


    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board[y][x].is_mine:
                continue
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE:
                        if board[y + dy][x + dx].is_mine:
                            board[y][x].neighbor_mines += 1

    return board


def read_number_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return None
    except ValueError:
        print("Ошибка: Файл содержит недопустимое значение.")
        return None

def write_number_to_file(filename, number):
    with open(filename, 'w') as file:
        file.write(str(number))


def draw_board3(board):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell = board[y][x]
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE)

            if cell.is_revealed:
                if cell.is_mine:
                    pygame.draw.rect(screen, RED, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                    if cell.neighbor_mines > 0:
                        text = font.render(str(cell.neighbor_mines), True, BLACK)
                        screen.blit(text, (x * CELL_SIZE + 10, y * CELL_SIZE + 50 + 5))
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, BLACK, rect, 1)



def open_new_window7(k3):
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Сапер")
    filename = 'number.txt'
    max_ = read_number_from_file(filename)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)

        font = pygame.font.SysFont('None', 64)
        a1 = font.render("К сожалению вы проиграли", 1, BLACK)
        screen.blit(a1, (260, 50))
        if k3 >max_:
            font = pygame.font.SysFont('None', 64)
            a1 = font.render(f"У вас новый рекорд {k3} очков", 1, BLACK)
            screen.blit(a1, (260, 150))
        else:
            font = pygame.font.SysFont('None', 64)
            a1 = font.render(f"Вы набрали {k3} очков ", 1, BLACK)
            screen.blit(a1, (260, 150))
            write_number_to_file(filename, k3)

        pygame.display.flip()


def open_new_window8():
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Сапер")
    filename = 'number.txt'
    max_ = read_number_from_file(filename)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)

        font = pygame.font.SysFont('None', 64)
        a1 = font.render("Вы победили", 1, BLACK)
        screen.blit(a1, (260, 50))
        pygame.display.flip()


def open_new_window5():
    k3 = 0
    k4 = 121
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Сапер")
    board = create_board3()
    running = True
    while running:
        screen.fill(WHITE)
        draw_board3(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                if mouse_y > 50:
                    x = mouse_x // CELL_SIZE
                    y = (mouse_y - 50) // CELL_SIZE

                    if not board[y][x].is_revealed:
                        board[y][x].is_revealed = True
                        if board[y][x].is_mine:
                            open_new_window7(k3)
                        else:
                            k3 += 50
                            k4 -= 1
            if k4 == 0:
                k4 += 100
                open_new_window8()
        pygame.display.flip()


def open_new_window4():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Морской бой")
    clock = pygame.time.Clock()
    character = Character()
    stars = []
    stars2 = []
    stars3 = []
    stars4 = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for _ in range(50):
                    stars.append(Star(mouse_x, mouse_y))
        character.update()
        screen.fill(WHITE)
        character.draw(screen)
        stars = [star for star in stars if star.move()]
        stars2.append(Star2(200, 200))
        stars2 = [star for star in stars2 if star.move()]
        for star in stars:
            star.draw(screen)
        for star in stars2:
            star.draw(screen)
        stars3.append(Star3(800, 200))
        stars3 = [star for star in stars3 if star.move()]
        for star in stars3:
            star.draw(screen)
        stars4.append(Star4(500, 500))
        stars4 = [star for star in stars4 if star.move()]
        for star in stars4:
            star.draw(screen)
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("Поздравляю с победой", 1, BLACK)
        screen.blit(a1, (260, 50))
        pygame.display.flip()
        clock.tick(60)

def open_new_window3():
    pygame.init()
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Морской бой")
    rect = pygame.Rect(2000, 2000, 200, 200)
    get_grid_positions2(rect)
    board = create_board()
    board2 = create_board2()
    running = True
    global k1
    global k2
    while running:
        screen.fill(WHITE)
        draw_board(screen, board)
        draw_board2(screen, board2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                if  mouse_y > 50 and mouse_x<600:
                    x = mouse_x // CELL_SIZE
                    y = (mouse_y - 50) // CELL_SIZE
                    if not board[y][x].is_revealed:
                        board[y][x].is_revealed = True
                        if board[y][x].is_mine:
                            k1  = k1 -1

                if mouse_y > 50 and mouse_x>600:
                    x = mouse_x // CELL_SIZE - 14
                    y = (mouse_y - 50) // CELL_SIZE
                    if not board2[y][x].is_revealed:
                        board2[y][x].is_revealed = True
                        if board2[y][x].is_mine:
                            k2 = k2 - 1
        if k1 == 0 or k2 == 0:
            k1 = k1 + 100
            k2 = k2 + 100
            open_new_window4()
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("A", 1, BLACK)
        screen.blit(a1, (760, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("B", 1, BLACK)
        screen.blit(a1, (810, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("C", 1, BLACK)
        screen.blit(a1, (860, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("D", 1, BLACK)
        screen.blit(a1, (910, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("E", 1, BLACK)
        screen.blit(a1, (960, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("F", 1, BLACK)
        screen.blit(a1, (1010, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("G", 1, BLACK)
        screen.blit(a1, (1060, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("H", 1, BLACK)
        screen.blit(a1, (1110, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("I", 1, BLACK)
        screen.blit(a1, (1160, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("J", 1, BLACK)
        screen.blit(a1, (1210, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("1", 1, BLACK)
        screen.blit(a1, (0, 110))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("2", 1, BLACK)
        screen.blit(a1, (0, 160))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("3", 1, BLACK)
        screen.blit(a1, (0, 210))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("4", 1, BLACK)
        screen.blit(a1, (0, 260))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("5", 1, BLACK)
        screen.blit(a1, (0, 310))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("6", 1, BLACK)
        screen.blit(a1, (0, 360))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("7", 1, BLACK)
        screen.blit(a1, (0, 410))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("8", 1, BLACK)
        screen.blit(a1, (0, 460))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("9", 1, BLACK)
        screen.blit(a1, (0, 510))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("10", 1, BLACK)
        screen.blit(a1, (0, 560))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("A", 1, BLACK)
        screen.blit(a1, (60, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("B", 1, BLACK)
        screen.blit(a1, (110, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("C", 1, BLACK)
        screen.blit(a1, (160, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("D", 1, BLACK)
        screen.blit(a1, (210, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("E", 1, BLACK)
        screen.blit(a1, (260, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("F", 1, BLACK)
        screen.blit(a1, (310, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("G", 1, BLACK)
        screen.blit(a1, (360, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("H", 1, BLACK)
        screen.blit(a1, (410, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("I", 1, BLACK)
        screen.blit(a1, (460, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("J", 1, BLACK)
        screen.blit(a1, (510, 50))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("1", 1, BLACK)
        screen.blit(a1, (700, 110))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("2", 1, BLACK)
        screen.blit(a1, (700, 160))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("3", 1, BLACK)
        screen.blit(a1, (700, 210))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("4", 1, BLACK)
        screen.blit(a1, (700, 260))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("5", 1, BLACK)
        screen.blit(a1, (700, 310))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("6", 1, BLACK)
        screen.blit(a1, (700, 360))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("7", 1, BLACK)
        screen.blit(a1, (700, 410))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("8", 1, BLACK)
        screen.blit(a1, (700, 460))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("9", 1, BLACK)
        screen.blit(a1, (700, 510))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("10", 1, BLACK)
        screen.blit(a1, (700, 560))
        pygame.display.flip()





def open_new_window2():
    new_window = pygame.display.set_mode((1000, 1000))
    new_window.fill(WHITE)
    pygame.display.set_caption("Морской бой")
    font = pygame.font.SysFont('comicsansms', 32)
    a1 = font.render("Первый игрок расставляет корабли", 1, BLACK)
    screen.blit(a1, (200, 0))
    pygame.draw.lines(screen, BLACK, False, [[200, 200], [200, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[250, 200], [250, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[300, 200], [300, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[350, 200], [350, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[400, 200], [400, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[450, 200], [450, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[500, 200], [500, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[550, 200], [550, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[600, 200], [600, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[650, 200], [650, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[700, 200], [700, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[750, 200], [750, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 200], [750, 200]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 250], [750, 250]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 300], [750, 300]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 350], [750, 350]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 400], [750, 400]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 450], [750, 450]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 500], [750, 500]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 550], [750, 550]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 600], [750, 600]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 650], [750, 650]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 700], [750, 700]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 750], [750, 750]], 5)
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("A", 1, BLACK)
    screen.blit(a1, (260, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("B", 1, BLACK)
    screen.blit(a1, (310, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("C", 1, BLACK)
    screen.blit(a1, (360, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("D", 1, BLACK)
    screen.blit(a1, (410, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("E", 1, BLACK)
    screen.blit(a1, (460, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("F", 1, BLACK)
    screen.blit(a1, (510, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("G", 1, BLACK)
    screen.blit(a1, (560, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("H", 1, BLACK)
    screen.blit(a1, (610, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("I", 1, BLACK)
    screen.blit(a1, (660, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("J", 1, BLACK)
    screen.blit(a1, (710, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("1", 1, BLACK)
    screen.blit(a1, (210, 260))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("2", 1, BLACK)
    screen.blit(a1, (210, 310))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("3", 1, BLACK)
    screen.blit(a1, (210, 360))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("4", 1, BLACK)
    screen.blit(a1, (210, 410))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("5", 1, BLACK)
    screen.blit(a1, (210, 460))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("6", 1, BLACK)
    screen.blit(a1, (210, 510))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("7", 1, BLACK)
    screen.blit(a1, (210, 560))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("8", 1, BLACK)
    screen.blit(a1, (210, 610))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("9", 1, BLACK)
    screen.blit(a1, (210, 660))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("10", 1, BLACK)
    screen.blit(a1, (200, 710))
    image1 = pygame.image.load('корабль4.png')
    image1 = pygame.transform.scale(image1, (200, 50))
    width1 = 100
    height1 = 800
    image_rect1 = image1.get_rect(center=(width1, height1))
    image2 = pygame.image.load('корабль3.png')
    image2 = pygame.transform.scale(image2, (150, 50))
    width2 = 100
    height2 = 900
    image_rect2 = image2.get_rect(center=(width2, height2))
    image3 = pygame.image.load('корабль3.png')
    image3 = pygame.transform.scale(image3, (150, 50))
    width3 = 300
    height3 = 900
    image_rect3 = image3.get_rect(center=(width3, height3))
    image4 = pygame.image.load('корабль2.png')
    image4 = pygame.transform.scale(image4, (100, 50))
    width4 = 350
    height4 = 800
    image_rect4 = image4.get_rect(center=(width4, height4))
    image5 = pygame.image.load('корабль2.png')
    image5 = pygame.transform.scale(image5, (100, 50))
    width5 = 500
    height5 = 800
    image_rect5 = image5.get_rect(center=(width5, height5))
    image6 = pygame.image.load('корабль2.png')
    image6 = pygame.transform.scale(image6, (100, 50))
    width6 = 500
    height6 = 900
    image_rect6 = image6.get_rect(center=(width6, height6))
    image7 = pygame.image.load('корабль.png')
    image7 = pygame.transform.scale(image7, (50, 50))
    width7 = 650
    height7 = 900
    image_rect7 = image7.get_rect(center=(width7, height7))
    image8 = pygame.image.load('корабль.png')
    image8 = pygame.transform.scale(image8, (50, 50))
    width8 = 650
    height8 = 800
    image_rect8 = image8.get_rect(center=(width8, height8))
    image9 = pygame.image.load('корабль.png')
    image9 = pygame.transform.scale(image9, (50, 50))
    width9 = 750
    height9 = 900
    image_rect9 = image9.get_rect(center=(width9, height9))
    image = pygame.image.load('корабль.png')
    image = pygame.transform.scale(image, (50, 50))
    width10 = 750
    height10 = 800
    image_rect10 = image.get_rect(center=(width10, height10))
    ugol1 = 0
    ugol2 = 0
    ugol3 = 0
    ugol4 = 0
    ugol5 = 0
    ugol6 = 0
    ugol7 = 0
    ugol8 = 0
    ugol9 = 0
    ugol10 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    x10 = 0
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    y5 = 0
    y6 = 0
    y7 = 0
    y8 = 0
    y9 = 0
    y10 = 0
    Selected10 = False
    Selected1 = False
    Selected2 = False
    Selected3 = False
    Selected4 = False
    Selected5 = False
    Selected6 = False
    Selected7 = False
    Selected8 = False
    Selected9 = False
    new_running = True
    keys = pygame.key.get_pressed()
    while new_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = event.pos
                if 800 <= mouse_x <= 900 and 400 <= mouse_y <= 500:
                    #if (200 < x1 + width1 < 750 and 200 < y1 + height1 < 750) and (
                            #200 < x2 + width2 < 750 and 200 < y2 + height2 < 750) and (
                            #200 < x3 + width3 < 750 and 200 < y3 + height3 < 750) and (
                            #200 < x4 + width4 < 750 and 200 < y4 + height4 < 750) and (
                            #200 < x5 + width5 < 750 and 200 < y5 + height5 < 750) and (
                            #200 < x6 + width6 < 750 and 200 < y6 + height6 < 750) and (
                            #200 < x7 + width7 < 750 and 200 < y7 + height7 < 750) and (
                            #200 < x8 + width8 < 750 and 200 < y8 + height8 < 750) and (
                            #200 < x9 + width9 < 750 and 200 < y9 + height9 < 750) and (
                            #200 < x10 + width10 < 750 and 200 < y10 + height10 < 750):
                    open_new_window3()

                    #else:
                        #a1 = font.render("Не все корабли выставлены", 1, BLACK)
                        #screen.blit(a1, (200, 0))

                if image_rect10.collidepoint(mouse_pos):
                    Selected10 = True
                if image_rect1.collidepoint(mouse_pos):
                    Selected1 = True
                if image_rect2.collidepoint(mouse_pos):
                    Selected2 = True
                if image_rect3.collidepoint(mouse_pos):
                    Selected3 = True
                if image_rect4.collidepoint(mouse_pos):
                    Selected4 = True
                if image_rect5.collidepoint(mouse_pos):
                    Selected5 = True
                if image_rect6.collidepoint(mouse_pos):
                    Selected6 = True
                if image_rect7.collidepoint(mouse_pos):
                    Selected7 = True
                if image_rect8.collidepoint(mouse_pos):
                    Selected8 = True
                if image_rect9.collidepoint(mouse_pos):
                    Selected9 = True
            if event.type == pygame.MOUSEBUTTONUP:
                Selected10 = False
                Selected1 = False
                Selected2 = False
                Selected3 = False
                Selected4 = False
                Selected5 = False
                Selected6 = False
                Selected7 = False
                Selected8 = False
                Selected9 = False
            keys = pygame.key.get_pressed()
            if Selected10:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect10, -25, 0)
                    x10 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect10, 25, 0)
                    x10 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect10, 0, -25)
                    y10 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect10, 0, 25)
                    y10 += 25

                ugol10 += 90
            if Selected1:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect1, -25, 0)
                    x1 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect1, 25, 0)
                    x1 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect1, 0, -25)
                    y1 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect1, 0, 25)
                    y1 += 25

                ugol1 += 90

            if Selected2:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect2, -25, 0)
                    x2 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect2, 25, 0)
                    x2 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect2, 0, -25)
                    y2 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect2, 0, 25)
                    y2 += 25

                ugol2 += 90
            if Selected3:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect3, -25, 0)
                    x3 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect3, 25, 0)
                    x3 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect3, 0, -25)
                    y3 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect3, 0, 25)
                    y3 += 25

                ugol3 += 90
            if Selected4:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect4, -25, 0)
                    x4 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect4, 25, 0)
                    x4 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect4, 0, -25)
                    y4 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect4, 0, 25)
                    y4 += 25

                ugol4 += 90
            if Selected5:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect5, -25, 0)
                    x5 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect5, 25, 0)
                    x5 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect5, 0, -25)
                    y5 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect5, 0, 25)
                    y5 += 25

                ugol5 += 90
            if Selected6:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect6, -25, 0)
                    x6 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect6, 25, 0)
                    x6 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect6, 0, -25)
                    y6 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect6, 0, 25)
                    y6 += 25

                ugol6 += 90
            if Selected7:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect7, -25, 0)
                    x7 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect7, 25, 0)
                    x7 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect7, 0, -25)
                    y7 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect7, 0, 25)
                    y7 += 25

                ugol7 += 90
            if Selected8:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect8, -25, 0)
                    x8 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect8, 25, 0)
                    x8 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect8, 0, -25)
                    y8 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect8, 0, 25)
                    y8 += 25

                ugol8 += 90
            if Selected9:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect9, -25, 0)
                    x9 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect9, 25, 0)
                    x9 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect9, 0, -25)
                    y9 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect9, 0, 25)
                    y9 += 25

                ugol9 += 90

        new_window.fill(WHITE)
        pygame.display.set_caption("Морской бой")
        font = pygame.font.SysFont('comicsansms', 32)
        a1 = font.render("Второй игрок расставляет корабли", 1, BLACK)
        start_x = 0
        start_y = 0
        end_x = 500
        end_y = 500
        square_size = 50
        for x in range(start_x, end_x + square_size, square_size):
            for y in range(start_y, end_y + square_size, square_size):
                pygame.draw.rect(screen, BLACK, (x, y, square_size, square_size), 1)
        draw_button("Готово", 800, 400, 100, 100)
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("A", 1, BLACK)
        screen.blit(a1, (60, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("B", 1, BLACK)
        screen.blit(a1, (110, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("C", 1, BLACK)
        screen.blit(a1, (160, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("D", 1, BLACK)
        screen.blit(a1, (210, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("E", 1, BLACK)
        screen.blit(a1, (260, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("F", 1, BLACK)
        screen.blit(a1, (310, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("G", 1, BLACK)
        screen.blit(a1, (360, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("H", 1, BLACK)
        screen.blit(a1, (410, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("I", 1, BLACK)
        screen.blit(a1, (460, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("J", 1, BLACK)
        screen.blit(a1, (510, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("1", 1, BLACK)
        screen.blit(a1, (0, 60))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("2", 1, BLACK)
        screen.blit(a1, (0, 110))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("3", 1, BLACK)
        screen.blit(a1, (0, 160))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("4", 1, BLACK)
        screen.blit(a1, (0, 210))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("5", 1, BLACK)
        screen.blit(a1, (0, 260))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("6", 1, BLACK)
        screen.blit(a1, (0, 310))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("7", 1, BLACK)
        screen.blit(a1, (0, 360))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("8", 1, BLACK)
        screen.blit(a1, (0, 410))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("9", 1, BLACK)
        screen.blit(a1, (0, 460))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("10", 1, BLACK)
        screen.blit(a1, (0, 510))
        rotated_image10 = pygame.transform.rotate(image, ugol10)
        rotated_rect10 = rotated_image10.get_rect(center=image_rect10.center)
        rotated_image1 = pygame.transform.rotate(image1, ugol1)
        rotated_rect1 = rotated_image1.get_rect(center=image_rect1.center)
        rotated_image2 = pygame.transform.rotate(image2, ugol2)
        rotated_rect2 = rotated_image2.get_rect(center=image_rect2.center)
        rotated_image3 = pygame.transform.rotate(image3, ugol3)
        rotated_rect3 = rotated_image3.get_rect(center=image_rect3.center)
        rotated_image4 = pygame.transform.rotate(image4, ugol4)
        rotated_rect4 = rotated_image4.get_rect(center=image_rect4.center)
        rotated_image5 = pygame.transform.rotate(image5, ugol5)
        rotated_rect5 = rotated_image5.get_rect(center=image_rect5.center)
        rotated_image6 = pygame.transform.rotate(image6, ugol6)
        rotated_rect6 = rotated_image6.get_rect(center=image_rect6.center)
        rotated_image7 = pygame.transform.rotate(image7, ugol7)
        rotated_rect7 = rotated_image7.get_rect(center=image_rect7.center)
        rotated_image8 = pygame.transform.rotate(image8, ugol8)
        rotated_rect8 = rotated_image8.get_rect(center=image_rect8.center)
        rotated_image9 = pygame.transform.rotate(image9, ugol9)
        rotated_rect9 = rotated_image9.get_rect(center=image_rect9.center)
        screen.blit(rotated_image10, rotated_rect10.topleft)
        screen.blit(rotated_image1, rotated_rect1.topleft)
        screen.blit(rotated_image2, rotated_rect2.topleft)
        screen.blit(rotated_image3, rotated_rect3.topleft)
        screen.blit(rotated_image4, rotated_rect4.topleft)
        screen.blit(rotated_image5, rotated_rect5.topleft)
        screen.blit(rotated_image6, rotated_rect6.topleft)
        screen.blit(rotated_image7, rotated_rect7.topleft)
        screen.blit(rotated_image8, rotated_rect8.topleft)
        screen.blit(rotated_image9, rotated_rect9.topleft)
        for z in grid_positions2:
            if z != rotated_rect10 or z != rotated_rect9 or z != rotated_rect8 or z != rotated_rect7 or z != rotated_rect6 or z != rotated_rect5 or z != rotated_rect4 or z != rotated_rect3 or z != rotated_rect2 or z != rotated_rect1:
                grid_positions2.remove(z)
        x, y = rotated_rect1.topleft
        if ugol1 == 0 or ugol1 % 180 == 0:
            new_position = (int((x/50)) + 1, int((y/50)) + 0)
            new_position1 = (int((x/50)) + 2, int((y/50)) + 0)
            new_position2 = (int((x/50)) + 3, int((y/50)) + 0)
            new_position8 = (int((x / 50)) + 0, int((y / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position1)
            grid_positions2.append(new_position2)
            grid_positions2.append(new_position8)
        elif ugol1 != 0 or ugol1 % 180 != 0:
            new_position7 = (int((x / 50)) + 0, int((y / 50)) + 0)
            new_position3 = (int((x/50)) + 0, int((y/50)) + 1)
            new_position4 = (int((x/50)) + 0, int((y/50)) + 2)
            new_position5 = (int((x/50)) + 0, int((y/50)) + 3)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position4)
            grid_positions2.append(new_position5)
            grid_positions2.append(new_position7)
        x1, y1 = rotated_rect2.topleft
        if ugol2 == 0 or ugol2 % 180 == 0:
            new_position = (int((x1 / 50)) + 1, int((y1 / 50)) + 0)
            new_position1 = (int((x1 / 50)) + 2, int((y1 / 50)) + 0)
            new_position8 = (int((x1 / 50)) + 0, int((y1 / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position1)
            grid_positions2.append(new_position8)
        elif ugol2 != 0 or ugol2 % 180 != 0:
            new_position7 = (int((x1 / 50)) + 0, int((y1 / 50)) + 0)
            new_position3 = (int((x1 / 50)) + 0, int((y1 / 50)) + 1)
            new_position4 = (int((x1 / 50)) + 0, int((y1 / 50)) + 2)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position4)
            grid_positions2.append(new_position7)
        x2, y2 = rotated_rect3.topleft
        if ugol3 == 0 or ugol3 % 180 == 0:
            new_position = (int((x2 / 50)) + 1, int((y2 / 50)) + 0)
            new_position1 = (int((x2 / 50)) + 2, int((y2 / 50)) + 0)
            new_position8 = (int((x2 / 50)) + 0, int((y2 / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position1)
            grid_positions2.append(new_position8)
        elif ugol3 != 0 or ugol3 % 180 != 0:
            new_position7 = (int((x2 / 50)) + 0, int((y2 / 50)) + 0)
            new_position3 = (int((x2 / 50)) + 0, int((y2 / 50)) + 1)
            new_position4 = (int((x2 / 50)) + 0, int((y2 / 50)) + 2)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position4)
            grid_positions2.append(new_position7)
        x3, y3 = rotated_rect4.topleft
        if ugol4 == 0 or ugol4 % 180 == 0:
            new_position = (int((x3 / 50)) + 1, int((y3 / 50)) + 0)
            new_position8 = (int((x3 / 50)) + 0, int((y3 / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position8)
        elif ugol4 != 0 or ugol4 % 180 != 0:
            new_position7 = (int((x3 / 50)) + 0, int((y3 / 50)) + 0)
            new_position3 = (int((x3 / 50)) + 0, int((y3 / 50)) + 1)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position7)
        x4, y4 = rotated_rect5.topleft
        if ugol5 == 0 or ugol5 % 180 == 0:
            new_position = (int((x4 / 50)) + 1, int((y4 / 50)) + 0)
            new_position8 = (int((x4 / 50)) + 0, int((y4 / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position8)
        elif ugol5 != 0 or ugol5 % 180 != 0:
            new_position7 = (int((x4 / 50)) + 0, int((y4 / 50)) + 0)
            new_position3 = (int((x4 / 50)) + 0, int((y4 / 50)) + 1)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position7)
        x5, y5 = rotated_rect6.topleft
        if ugol6 == 0 or ugol6 % 180 == 0:
            new_position = (int((x5 / 50)) + 1, int((y5 / 50)) + 0)
            new_position8 = (int((x5 / 50)) + 0, int((y5 / 50)) + 0)
            grid_positions2.append(new_position)
            grid_positions2.append(new_position8)
        elif ugol6 != 0 or ugol6 % 180 != 0:
            new_position7 = (int((x5 / 50)) + 0, int((y5 / 50)) + 0)
            new_position3 = (int((x5 / 50)) + 0, int((y5 / 50)) + 1)
            grid_positions2.append(new_position3)
            grid_positions2.append(new_position7)
        x6, y6 = rotated_rect7.topleft
        if ugol7 == 0 or ugol7 % 180 == 0:
            new_position8 = (int((x6 / 50)) + 0, int((y6 / 50)) + 0)
            grid_positions2.append(new_position8)
        elif ugol7 != 0 or ugol7 % 180 != 0:
            new_position7 = (int((x6 / 50)) + 0, int((y6 / 50)) + 0)
            grid_positions2.append(new_position7)
        x7, y7 = rotated_rect8.topleft
        if ugol8 == 0 or ugol8 % 180 == 0:
            new_position8 = (int((x7 / 50)) + 0, int((y7 / 50)) + 0)
            grid_positions2.append(new_position8)
        elif ugol8 != 0 or ugol8 % 180 != 0:
            new_position7 = (int((x7 / 50)) + 0, int((y7 / 50)) + 0)
            grid_positions2.append(new_position7)
        x8, y8 = rotated_rect9.topleft
        if ugol9 == 0 or ugol9 % 180 == 0:
            new_position8 = (int((x8 / 50)) + 0, int((y8 / 50)) + 0)
            grid_positions2.append(new_position8)
        elif ugol9 != 0 or ugol9 % 180 != 0:
            new_position7 = (int((x8 / 50)) + 0, int((y8 / 50)) + 0)
            grid_positions2.append(new_position7)
        x9, y9 = rotated_rect10.topleft
        if ugol10 == 0 or ugol10 % 180 == 0:
            new_position8 = (int((x9 / 50)) + 0, int((y9 / 50)) + 0)
            grid_positions2.append(new_position8)
        elif ugol10 != 0 or ugol10 % 180 != 0:
            new_position7 = (int((x9 / 50)) + 0, int((y9 / 50)) + 0)
            grid_positions2.append(new_position7)
        pygame.display.flip()


def open_new_window():
    new_window = pygame.display.set_mode((1000, 1000))
    new_window.fill(WHITE)
    pygame.display.set_caption("Морской бой")
    font = pygame.font.SysFont('comicsansms', 32)
    a1 = font.render("Первый игрок расставляет корабли", 1, BLACK)
    screen.blit(a1, (200, 0))
    pygame.draw.lines(screen, BLACK, False, [[200, 200], [200, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[250, 200], [250, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[300, 200], [300, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[350, 200], [350, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[400, 200], [400, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[450, 200], [450, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[500, 200], [500, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[550, 200], [550, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[600, 200], [600, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[650, 200], [650, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[700, 200], [700, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[750, 200], [750, 750]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 200], [750, 200]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 250], [750, 250]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 300], [750, 300]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 350], [750, 350]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 400], [750, 400]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 450], [750, 450]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 500], [750, 500]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 550], [750, 550]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 600], [750, 600]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 650], [750, 650]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 700], [750, 700]], 5)
    pygame.draw.lines(screen, BLACK, False, [[200, 750], [750, 750]], 5)
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("A", 1, BLACK)
    screen.blit(a1, (260, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("B", 1, BLACK)
    screen.blit(a1, (310, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("C", 1, BLACK)
    screen.blit(a1, (360, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("D", 1, BLACK)
    screen.blit(a1, (410, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("E", 1, BLACK)
    screen.blit(a1, (460, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("F", 1, BLACK)
    screen.blit(a1, (510, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("G", 1, BLACK)
    screen.blit(a1, (560, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("H", 1, BLACK)
    screen.blit(a1, (610, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("I", 1, BLACK)
    screen.blit(a1, (660, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("J", 1, BLACK)
    screen.blit(a1, (710, 210))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("1", 1, BLACK)
    screen.blit(a1, (210, 260))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("2", 1, BLACK)
    screen.blit(a1, (210, 310))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("3", 1, BLACK)
    screen.blit(a1, (210, 360))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("4", 1, BLACK)
    screen.blit(a1, (210, 410))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("5", 1, BLACK)
    screen.blit(a1, (210, 460))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("6", 1, BLACK)
    screen.blit(a1, (210, 510))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("7", 1, BLACK)
    screen.blit(a1, (210, 560))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("8", 1, BLACK)
    screen.blit(a1, (210, 610))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("9", 1, BLACK)
    screen.blit(a1, (210, 660))
    font = pygame.font.SysFont('None', 64)
    a1 = font.render("10", 1, BLACK)
    screen.blit(a1, (200, 710))
    image10 = pygame.image.load('корабль4.png')
    image10 = pygame.transform.scale(image10, (200, 50))
    width1 = 100
    height1 = 800
    image_rect1 = image10.get_rect(center=(width1, height1))
    image20 = pygame.image.load('корабль3.png')
    image20 = pygame.transform.scale(image20, (150, 50))
    width2 = 100
    height2 = 900
    image_rect2 = image20.get_rect(center=(width2, height2))
    image30 = pygame.image.load('корабль3.png')
    image30 = pygame.transform.scale(image30, (150, 50))
    width3 = 300
    height3 = 900
    image_rect3 = image30.get_rect(center=(width3, height3))
    image40 = pygame.image.load('корабль2.png')
    image40 = pygame.transform.scale(image40, (100, 50))
    width4 = 350
    height4 = 800
    image_rect4 = image40.get_rect(center=(width4, height4))
    image50 = pygame.image.load('корабль2.png')
    image50 = pygame.transform.scale(image50, (100, 50))
    width5 = 500
    height5 = 800
    image_rect5 = image50.get_rect(center=(width5, height5))
    image60 = pygame.image.load('корабль2.png')
    image60 = pygame.transform.scale(image60, (100, 50))
    width6 = 500
    height6 = 900
    image_rect6 = image60.get_rect(center=(width6, height6))
    image70 = pygame.image.load('корабль.png')
    image70 = pygame.transform.scale(image70, (50, 50))
    width7 = 650
    height7 = 900
    image_rect7 = image70.get_rect(center=(width7, height7))
    image80 = pygame.image.load('корабль.png')
    image80 = pygame.transform.scale(image80, (50, 50))
    width8 = 650
    height8 = 800
    image_rect8 = image80.get_rect(center=(width8, height8))
    image90 = pygame.image.load('корабль.png')
    image90 = pygame.transform.scale(image90, (50, 50))
    width9 = 750
    height9 = 900
    image_rect9 = image90.get_rect(center=(width9, height9))
    image0 = pygame.image.load('корабль.png')
    image0 = pygame.transform.scale(image0, (50, 50))
    width10 = 750
    height10 = 800
    image_rect10 = image0.get_rect(center=(width10, height10))
    ugol1 = 0
    ugol2 = 0
    ugol3 = 0
    ugol4 = 0
    ugol5 = 0
    ugol6 = 0
    ugol7 = 0
    ugol8 = 0
    ugol9 = 0
    ugol10 = 0
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    x10 = 0
    y1 = 0
    y2  = 0
    y3 = 0
    y4 = 0
    y5 = 0
    y6 = 0
    y7 = 0
    y8 = 0
    y9 = 0
    y10 = 0
    Selected10 = False
    Selected1 = False
    Selected2 = False
    Selected3 = False
    Selected4 = False
    Selected5 = False
    Selected6 = False
    Selected7 = False
    Selected8 = False
    Selected9 = False
    new_running = True
    keys = pygame.key.get_pressed()
    while new_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = event.pos
                if 600 <= mouse_x <= 700 and 400 <= mouse_y <= 500:
                    # if (200 <x1 + width1<750 and 200 <y1 + height1<750) and (200 <x2 + width2<750 and 200 <y2 + height2<750) and (200 <x3 + width3<750 and 200 <y3 + height3<750) and (200 <x4 + width4<750 and 200 <y4 + height4<750) and (200 <x5 + width5<750 and 200 <y5 + height5<750) and (200 <x6 + width6<750 and 200 <y6 + height6<750)and (200 <x7 + width7<750 and 200 <y7 + height7<750) and (200 <x8 + width8<750 and 200 <y8 + height8<750) and (200 <x9 + width9<750 and 200 <y9 + height9<750) and (200 <x10 + width10<750 and 200 <y10 + height10<750):
                    open_new_window2()
                    # else:
                    # a1 = font.render("Не все корабли выставлены", 1, BLACK)
                    # screen.blit(a1, (200, 0))

                if image_rect10.collidepoint(mouse_pos):
                    Selected10 = True
                if image_rect1.collidepoint(mouse_pos):
                    Selected1 = True
                if image_rect2.collidepoint(mouse_pos):
                    Selected2 = True
                if image_rect3.collidepoint(mouse_pos):
                    Selected3 = True
                if image_rect4.collidepoint(mouse_pos):
                    Selected4 = True
                if image_rect5.collidepoint(mouse_pos):
                    Selected5 = True
                if image_rect6.collidepoint(mouse_pos):
                    Selected6 = True
                if image_rect7.collidepoint(mouse_pos):
                    Selected7 = True
                if image_rect8.collidepoint(mouse_pos):
                    Selected8 = True
                if image_rect9.collidepoint(mouse_pos):
                    Selected9 = True
            if event.type == pygame.MOUSEBUTTONUP:
                Selected10 = False
                Selected1 = False
                Selected2 = False
                Selected3 = False
                Selected4 = False
                Selected5 = False
                Selected6 = False
                Selected7 = False
                Selected8 = False
                Selected9 = False
            keys = pygame.key.get_pressed()
            if Selected10:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect10, -25, 0)
                    x10 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect10, 25, 0)
                    x10 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect10, 0, -25)
                    y10 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect10, 0, 25)
                    y10 += 25

                ugol10 += 90
            if Selected1:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect1, -25, 0)
                    x1 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect1, 25, 0)
                    x1 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect1, 0, -25)
                    y1 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect1, 0, 25)
                    y1 += 25

                ugol1 += 90

            if Selected2:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect2, -25, 0)
                    x2 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect2, 25, 0)
                    x2 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect2, 0, -25)
                    y2 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect2, 0, 25)
                    y2 += 25

                ugol2 += 90
            if Selected3:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect3, -25, 0)
                    x3 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect3, 25, 0)
                    x3 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect3, 0, -25)
                    y3 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect3, 0, 25)
                    y3 += 25

                ugol3 += 90
            if Selected4:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect4, -25, 0)
                    x4 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect4, 25, 0)
                    x4 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect4, 0, -25)
                    y4 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect4, 0, 25)
                    y4 += 25

                ugol4 += 90
            if Selected5:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect5, -25, 0)
                    x5 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect5, 25, 0)
                    x5 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect5, 0, -25)
                    y5 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect5, 0, 25)
                    y5 += 25

                ugol5 += 90
            if Selected6:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect6, -25, 0)
                    x6 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect6, 25, 0)
                    x6 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect6, 0, -25)
                    y6 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect6, 0, 25)
                    y6 += 25

                ugol6 += 90
            if Selected7:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect7, -25, 0)
                    x7 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect7, 25, 0)
                    x7 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect7, 0, -25)
                    y7 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect7, 0, 25)
                    y7 += 25

                ugol7 += 90
            if Selected8:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect8, -25, 0)
                    x8 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect8, 25, 0)
                    x8 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect8, 0, -25)
                    y8 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect8, 0, 25)
                    y8 += 25

                ugol8 += 90
            if Selected9:
                if keys[pygame.K_LEFT]:
                    move_image(image_rect9, -25, 0)
                    x9 -= 25
                if keys[pygame.K_RIGHT]:
                    move_image(image_rect9, 25, 0)
                    x9 += 25
                if keys[pygame.K_UP]:
                    move_image(image_rect9, 0, -25)
                    y9 -= 25
                if keys[pygame.K_DOWN]:
                    move_image(image_rect9, 0, 25)
                    y9 += 25

                ugol9 += 90



        new_window.fill(WHITE)
        pygame.display.set_caption("Морской бой")
        font = pygame.font.SysFont('comicsansms', 32)
        a1 = font.render("Первый игрок расставляет корабли", 1, BLACK)
        start_x = 000
        start_y = 0
        end_x = 500
        end_y = 500
        square_size = 50
        for x in range(start_x, end_x + square_size, square_size):
            for y in range(start_y, end_y + square_size, square_size):
                pygame.draw.rect(screen, BLACK, (x, y, square_size, square_size), 1)
        draw_button("Готово", 600, 400, 100, 100)
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("A", 1, BLACK)
        screen.blit(a1, (60, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("B", 1, BLACK)
        screen.blit(a1, (110, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("C", 1, BLACK)
        screen.blit(a1, (160, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("D", 1, BLACK)
        screen.blit(a1, (210, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("E", 1, BLACK)
        screen.blit(a1, (260, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("F", 1, BLACK)
        screen.blit(a1, (310, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("G", 1, BLACK)
        screen.blit(a1, (360, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("H", 1, BLACK)
        screen.blit(a1, (410, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("I", 1, BLACK)
        screen.blit(a1, (460, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("J", 1, BLACK)
        screen.blit(a1, (510, 0))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("1", 1, BLACK)
        screen.blit(a1, (0, 60))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("2", 1, BLACK)
        screen.blit(a1, (0, 110))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("3", 1, BLACK)
        screen.blit(a1, (0, 160))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("4", 1, BLACK)
        screen.blit(a1, (0, 210))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("5", 1, BLACK)
        screen.blit(a1, (0, 260))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("6", 1, BLACK)
        screen.blit(a1, (0, 310))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("7", 1, BLACK)
        screen.blit(a1, (0, 360))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("8", 1, BLACK)
        screen.blit(a1, (0, 410))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("9", 1, BLACK)
        screen.blit(a1, (0, 460))
        font = pygame.font.SysFont('None', 64)
        a1 = font.render("10", 1, BLACK)
        screen.blit(a1, (0, 510))
        rotated_image10 = pygame.transform.rotate(image0, ugol10)
        rotated_rect10 = rotated_image10.get_rect(center=image_rect10.center)
        rotated_image1 = pygame.transform.rotate(image10, ugol1)
        rotated_rect1 = rotated_image1.get_rect(center=image_rect1.center)
        rotated_image2 = pygame.transform.rotate(image20, ugol2)
        rotated_rect2 = rotated_image2.get_rect(center=image_rect2.center)
        rotated_image3 = pygame.transform.rotate(image30, ugol3)
        rotated_rect3 = rotated_image3.get_rect(center=image_rect3.center)
        rotated_image4 = pygame.transform.rotate(image40, ugol4)
        rotated_rect4 = rotated_image4.get_rect(center=image_rect4.center)
        rotated_image5 = pygame.transform.rotate(image50, ugol5)
        rotated_rect5 = rotated_image5.get_rect(center=image_rect5.center)
        rotated_image6 = pygame.transform.rotate(image60, ugol6)
        rotated_rect6 = rotated_image6.get_rect(center=image_rect6.center)
        rotated_image7 = pygame.transform.rotate(image70, ugol7)
        rotated_rect7 = rotated_image7.get_rect(center=image_rect7.center)
        rotated_image8 = pygame.transform.rotate(image80, ugol8)
        rotated_rect8 = rotated_image8.get_rect(center=image_rect8.center)
        rotated_image9 = pygame.transform.rotate(image90, ugol9)
        rotated_rect9 = rotated_image9.get_rect(center=image_rect9.center)

        screen.blit(rotated_image10, rotated_rect10.topleft)
        screen.blit(rotated_image1, rotated_rect1.topleft),
        screen.blit(rotated_image2, rotated_rect2.topleft)
        screen.blit(rotated_image3, rotated_rect3.topleft)
        screen.blit(rotated_image4, rotated_rect4.topleft)
        screen.blit(rotated_image5, rotated_rect5.topleft)
        screen.blit(rotated_image6, rotated_rect6.topleft)
        screen.blit(rotated_image7, rotated_rect7.topleft)
        screen.blit(rotated_image8, rotated_rect8.topleft)
        screen.blit(rotated_image9, rotated_rect9.topleft)
        for z in grid_positions:
            if z != rotated_rect10 or z != rotated_rect9 or z != rotated_rect8 or z != rotated_rect7 or z != rotated_rect6 or z != rotated_rect5 or z != rotated_rect4 or z != rotated_rect3 or z != rotated_rect2 or z != rotated_rect1:
                grid_positions.remove(z)
        x, y = rotated_rect1.topleft
        if ugol1 == 0 or ugol1 % 180 == 0:
            new_position = (int((x/50)) + 1, int((y/50)) + 0)
            new_position1 = (int((x/50)) + 2, int((y/50)) + 0)
            new_position2 = (int((x/50)) + 3, int((y/50)) + 0)
            new_position8 = (int((x / 50)) + 0, int((y / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position1)
            grid_positions.append(new_position2)
            grid_positions.append(new_position8)
        elif ugol1 != 0 or ugol1 % 180 != 0:
            new_position7 = (int((x / 50)) + 0, int((y / 50)) + 0)
            new_position3 = (int((x/50)) + 0, int((y/50)) + 1)
            new_position4 = (int((x/50)) + 0, int((y/50)) + 2)
            new_position5 = (int((x/50)) + 0, int((y/50)) + 3)
            grid_positions.append(new_position3)
            grid_positions.append(new_position4)
            grid_positions.append(new_position5)
            grid_positions.append(new_position7)
        x1, y1 = rotated_rect2.topleft
        if ugol2 == 0 or ugol2 % 180 == 0:
            new_position = (int((x1 / 50)) + 1, int((y1 / 50)) + 0)
            new_position1 = (int((x1 / 50)) + 2, int((y1 / 50)) + 0)
            new_position8 = (int((x1 / 50)) + 0, int((y1 / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position1)
            grid_positions.append(new_position8)
        elif ugol2 != 0 or ugol2 % 180 != 0:
            new_position7 = (int((x1 / 50)) + 0, int((y1 / 50)) + 0)
            new_position3 = (int((x1 / 50)) + 0, int((y1 / 50)) + 1)
            new_position4 = (int((x1 / 50)) + 0, int((y1 / 50)) + 2)
            grid_positions.append(new_position3)
            grid_positions.append(new_position4)
            grid_positions.append(new_position7)
        x2, y2 = rotated_rect3.topleft
        if ugol3 == 0 or ugol3 % 180 == 0:
            new_position = (int((x2 / 50)) + 1, int((y2 / 50)) + 0)
            new_position1 = (int((x2 / 50)) + 2, int((y2 / 50)) + 0)
            new_position8 = (int((x2 / 50)) + 0, int((y2 / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position1)
            grid_positions.append(new_position8)
        elif ugol3 != 0 or ugol3 % 180 != 0:
            new_position7 = (int((x2 / 50)) + 0, int((y2 / 50)) + 0)
            new_position3 = (int((x2 / 50)) + 0, int((y2 / 50)) + 1)
            new_position4 = (int((x2 / 50)) + 0, int((y2 / 50)) + 2)
            grid_positions.append(new_position3)
            grid_positions.append(new_position4)
            grid_positions.append(new_position7)
        x3, y3 = rotated_rect4.topleft
        if ugol4 == 0 or ugol4 % 180 == 0:
            new_position = (int((x3 / 50)) + 1, int((y3 / 50)) + 0)
            new_position8 = (int((x3 / 50)) + 0, int((y3 / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position8)
        elif ugol4 != 0 or ugol4 % 180 != 0:
            new_position7 = (int((x3 / 50)) + 0, int((y3 / 50)) + 0)
            new_position3 = (int((x3 / 50)) + 0, int((y3 / 50)) + 1)
            grid_positions.append(new_position3)
            grid_positions.append(new_position7)
        x4, y4 = rotated_rect5.topleft
        if ugol5 == 0 or ugol5 % 180 == 0:
            new_position = (int((x4 / 50)) + 1, int((y4 / 50)) + 0)
            new_position8 = (int((x4 / 50)) + 0, int((y4 / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position8)
        elif ugol5 != 0 or ugol5 % 180 != 0:
            new_position7 = (int((x4 / 50)) + 0, int((y4 / 50)) + 0)
            new_position3 = (int((x4 / 50)) + 0, int((y4 / 50)) + 1)
            grid_positions.append(new_position3)
            grid_positions.append(new_position7)
        x5, y5 = rotated_rect6.topleft
        if ugol6 == 0 or ugol6 % 180 == 0:
            new_position = (int((x5 / 50)) + 1, int((y5 / 50)) + 0)
            new_position8 = (int((x5 / 50)) + 0, int((y5 / 50)) + 0)
            grid_positions.append(new_position)
            grid_positions.append(new_position8)
        elif ugol6 != 0 or ugol6 % 180 != 0:
            new_position7 = (int((x5 / 50)) + 0, int((y5 / 50)) + 0)
            new_position3 = (int((x5 / 50)) + 0, int((y5 / 50)) + 1)
            grid_positions.append(new_position3)
            grid_positions.append(new_position7)
        x6, y6 = rotated_rect7.topleft
        if ugol7 == 0 or ugol7 % 180 == 0:
            new_position8 = (int((x6 / 50)) + 0, int((y6 / 50)) + 0)
            grid_positions.append(new_position8)
        elif ugol7 != 0 or ugol7 % 180 != 0:
            new_position7 = (int((x6 / 50)) + 0, int((y6 / 50)) + 0)
            grid_positions.append(new_position7)
        x7, y7 = rotated_rect8.topleft
        if ugol8 == 0 or ugol8 % 180 == 0:
            new_position8 = (int((x7 / 50)) + 0, int((y7 / 50)) + 0)
            grid_positions.append(new_position8)
        elif ugol8 != 0 or ugol8 % 180 != 0:
            new_position7 = (int((x7 / 50)) + 0, int((y7 / 50)) + 0)
            grid_positions.append(new_position7)
        x8, y8 = rotated_rect9.topleft
        if ugol9 == 0 or ugol9 % 180 == 0:
            new_position8 = (int((x8 / 50)) + 0, int((y8 / 50)) + 0)
            grid_positions.append(new_position8)
        elif ugol9 != 0 or ugol9 % 180 != 0:
            new_position7 = (int((x8 / 50)) + 0, int((y8 / 50)) + 0)
            grid_positions.append(new_position7)
        x9, y9 = rotated_rect10.topleft
        if ugol10 == 0 or ugol10 % 180 == 0:
            new_position8 = (int((x9 / 50)) + 0, int((y9 / 50)) + 0)
            grid_positions.append(new_position8)
        elif ugol10 != 0 or ugol10 % 180 != 0:
            new_position7 = (int((x9 / 50)) + 0, int((y9 / 50)) + 0)
            grid_positions.append(new_position7)
        pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if 375 <= mouse_x <= 675 and 400 <= mouse_y <= 500:
                open_new_window()
            if 375 <= mouse_x <= 675 and 700 <= mouse_y <= 800:
                open_new_window5()


    background = pygame.image.load('fon.jpg')
    background = pygame.transform.scale(background, (1000, 1000))
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont('comicsansms', 32)
    a = font.render("Добро пожаловать в Морской Бой", 1, WHITE)
    pygame.display.set_caption("Морской бой")
    screen.blit(a, (250, 200))
    draw_button("Играть с другом", 375, 400, 300, 100)
    draw_button("Сапер", 375, 700, 300, 100)



    pygame.display.flip()


pygame.quit()
sys.exit()