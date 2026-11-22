"""Flappy Bird Clone - Python/Pygame college project.
Controls: SPACE to flap; R to restart after game over; ESC to quit.
"""
import random
import sys
import pygame

WIDTH, HEIGHT = 400, 600
BIRD_X = 100
BIRD_SIZE = 30
GROUND_Y = 600
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_INTERVAL = 1800
GRAVITY = 1
FLAP_VELOCITY = -10
FPS = 60

WHITE = (255, 255, 255)
SKY = (135, 206, 235)
GREEN = (70, 180, 70)
DARK_GREEN = (35, 120, 35)
YELLOW = (255, 220, 40)
BLACK = (20, 20, 20)


def create_pipe(x=WIDTH):
    """Create a pipe pair with a gap positioned within playable bounds."""
    gap_center = random.randint(180, 420)
    return {"x": float(x), "gap_center": gap_center, "scored": False}


def pipe_rects(pipe):
    """Return upper and lower pipe rectangles for a pipe pair."""
    x = int(pipe["x"])
    top_height = pipe["gap_center"] - PIPE_GAP // 2
    bottom_y = pipe["gap_center"] + PIPE_GAP // 2
    return (
        pygame.Rect(x, 0, PIPE_WIDTH, top_height),
        pygame.Rect(x, bottom_y, PIPE_WIDTH, HEIGHT - bottom_y),
    )


def draw_pipe_pair(screen, pipe):
    top, bottom = pipe_rects(pipe)
    pygame.draw.rect(screen, GREEN, top)
    pygame.draw.rect(screen, GREEN, bottom)
    pygame.draw.rect(screen, DARK_GREEN, top, 3)
    pygame.draw.rect(screen, DARK_GREEN, bottom, 3)


def check_collision(bird_rect, pipes):
    """Check collision with the screen ceiling, ground or any pipe."""
    if bird_rect.top <= 0 or bird_rect.bottom >= GROUND_Y:
        return True
    return any(bird_rect.colliderect(rect) for p in pipes for rect in pipe_rects(p))


def reset_game():
    return 300.0, 0.0, [], 0, False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird Clone")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 25)

    bird_y, velocity, pipes, score, game_over = reset_game()
    last_pipe_time = pygame.time.get_ticks()
    running = True

    while running:
        clock.tick(FPS)
        flap = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE and not game_over:
                    flap = True
                elif event.key == pygame.K_r and game_over:
                    bird_y, velocity, pipes, score, game_over = reset_game()
                    last_pipe_time = pygame.time.get_ticks()

        if not game_over:
            if flap:
                velocity = FLAP_VELOCITY
            velocity += GRAVITY
            bird_y += velocity

            now = pygame.time.get_ticks()
            if now - last_pipe_time >= PIPE_INTERVAL:
                pipes.append(create_pipe())
                last_pipe_time = now

            for pipe in pipes:
                pipe["x"] -= PIPE_SPEED
                if not pipe["scored"] and pipe["x"] + PIPE_WIDTH < BIRD_X:
                    pipe["scored"] = True
                    score += 1
            pipes = [p for p in pipes if p["x"] + PIPE_WIDTH > 0]

            bird_rect = pygame.Rect(BIRD_X, int(bird_y), BIRD_SIZE, BIRD_SIZE)
            if check_collision(bird_rect, pipes):
                game_over = True

        screen.fill(SKY)
        for pipe in pipes:
            draw_pipe_pair(screen, pipe)
        bird_rect = pygame.Rect(BIRD_X, int(bird_y), BIRD_SIZE, BIRD_SIZE)
        pygame.draw.ellipse(screen, YELLOW, bird_rect)
        pygame.draw.circle(screen, BLACK, (BIRD_X + 21, int(bird_y) + 9), 3)
        pygame.draw.polygon(screen, (255, 140, 0), [(BIRD_X + 27, int(bird_y) + 14), (BIRD_X + 36, int(bird_y) + 18), (BIRD_X + 27, int(bird_y) + 20)])
        pygame.draw.rect(screen, (210, 170, 100), (0, GROUND_Y - 10, WIDTH, 10))

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (12, 12))
        if game_over:
            title = font.render("Game Over", True, BLACK)
            restart = small_font.render("Press R to restart or ESC to quit", True, BLACK)
            screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 15)))
            screen.blit(restart, restart.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25)))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
