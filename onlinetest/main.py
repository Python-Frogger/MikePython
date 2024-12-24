import pygame
import asyncio

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygbag Test")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 20
ball_speed = [5, 5]

async def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH - ball_radius:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] <= ball_radius or ball_pos[1] >= HEIGHT - ball_radius:
            ball_speed[1] = -ball_speed[1]

        screen.fill(BLACK)
        pygame.draw.circle(screen, RED, ball_pos, ball_radius)
        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())
