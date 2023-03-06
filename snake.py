import pygame
import random

# Khởi tạo game
pygame.init()

# Cài đặt kích thước màn hình
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Đặt tiêu đề cho cửa sổ game
pygame.display.set_caption("Game rắn đơn giản")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Cài đặt đồ họa font
font = pygame.font.SysFont(None, 25)

# Hàm vẽ rắn
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Hàm chạy trò chơi
def game_loop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí ban đầu cho rắn
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Khởi tạo giá trị ban đầu cho các pixel của rắn
    x1_change = 0       
    y1_change = 0

    # Đặt độ dài ban đầu của rắn
    snake_list = []
    Length_of_snake = 1

    # Tạo thức ăn ban đầu
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Vòng lặp chính của trò chơi
    while not game_over:
        
        # Nếu game bị đóng
        while game_close == True:
            screen.fill(white)
            message("Bạn thua! Nhấn Q để thoát hoặc C để chơi lại", red)
            pygame.display.update()

            # Xử lý các sự kiện khi game bị đóng
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Xử lý các sự kiện trong game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra nếu rắn chạm
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_close = True

    # Cập nhật vị trí của rắn
    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

    # Cập nhật các pixel của rắn
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_list.append(snake_Head)
    if len(snake_list) > Length_of_snake:
        del snake_list[0]

    # Kiểm tra nếu rắn ăn được thức ăn
    for x in snake_list[:-1]:
        if x == snake_Head:
            game_close = True

    # Vẽ rắn và thức ăn
    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Kiểm tra nếu rắn ăn được thức ăn
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    # Cập nhật thông tin độ dài rắn trên màn hình
    message("Độ dài: " + str(Length_of_snake-1), black)

    # Cập nhật màn hình
    pygame.display.update()

    # Cài đặt tốc độ của rắn
    clock.tick(snake_speed)

# Thoát game và tắt pygame
pygame.quit()
quit()
