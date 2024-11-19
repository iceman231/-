import pygame
import sys
import time

# 초기 설정
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("반응 속도 측정 프로그램")
clock = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 원 초기 설정
large_circle = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100)
small_circle_pos = [WIDTH//2, 50]
small_circle_radius = 10
speed = 2

# 시작 시간
start_time = None

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if large_circle.collidepoint(small_circle_pos):
                end_time = time.time()
                print(f"반응 시간: {end_time - start_time:.3f}초")
                running = False

    # 화면 업데이트
    screen.fill(WHITE)

    # 큰 원 그리기
    pygame.draw.ellipse(screen, BLUE, large_circle)

    # 작은 원 이동 및 그리기
    small_circle_pos[1] += speed
    pygame.draw.circle(screen, RED, small_circle_pos, small_circle_radius)

    # 시작 시간 기록
    if start_time is None:
        start_time = time.time()

    # 화면 갱신
    pygame.display.flip()
    clock.tick(60)
