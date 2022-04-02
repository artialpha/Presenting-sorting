import pygame
import time
from Window.Draw import Draw
pygame.init()


def main():

    print("Hello World!")
    clock = pygame.time.Clock()
    fps = 50
    prev_time = time.time()
    velocity = 0.05

    run = True
    width = 600
    height = 400

    draw = Draw(width, height, fps, velocity)
    while run:
        draw.redraw_window()
        pygame.display.update()
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()

        # Limit framrate
        # if fps=50 then for every second at most 50 frames should pass
        clock.tick(fps)
        # compute delta time
        now = time.time()
        dt = now - prev_time
        prev_time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("click!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    draw.move(dt, fps, velocity)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Use event.pos or pg.mouse.get_pos().
                    if draw.button_next.rect.collidepoint(event.pos):
                        draw.next_clicked()
                        # for x in draw.list_to_display.steps.steps:
                            # print(x)
                    if draw.button_prev.rect.collidepoint(event.pos):
                        print('prev clicked')


if __name__ == "__main__":
    main()
