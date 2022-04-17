import pygame
import time


from PygameAll.Window.WindowQuick import WindowQuick
from PygameAll.Window.WindowMerge import WindowMerge
from PygameAll.Window.WindowMenu import WindowMenu
from PygameAll.Window.Window import Window
pygame.init()


def main():

    print("Hello World!")
    clock = pygame.time.Clock()
    fps = 50
    prev_time = time.time()
    velocity = 0.05

    run = True
    width = 600
    height = 600


    # list of random numbers
    # lst = random.sample(range(10, 100), 9)
    lst = [3, 1, 9, 7, 8, 2, 6, 4, 5]
    draw = WindowMenu(width, height)

    while run:
        draw.redraw_window()
        pygame.display.update()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if isinstance(draw, WindowMenu):
                        print('click on button')
                        if res := draw.buttons_clicked_check(event, draw):
                            draw = res
                    else:
                        draw.buttons_clicked_check(event)
            elif event.type == pygame.KEYDOWN:
                draw.type_text(event)


if __name__ == "__main__":
    main()
