import pygame
import time
from PygameAll.Window.WindowQuick import WindowQuick
from PygameAll.Window.WindowMenu import WindowMenu
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

    # list of random numbers
    # lst = random.sample(range(10, 100), 9)
    lst = [3, 1, 9, 7, 8, 2, 6, 4, 5]

    draw = WindowQuick(width, height, fps, velocity, lst)
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Use event.pos or pg.mouse.get_pos().

                    draw.buttons_clicked_check(event)


if __name__ == "__main__":
    main()
