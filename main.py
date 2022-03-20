from Window.Draw import Draw
import pygame
import random


def main():
    print("Hello World!")

    run = True
    black = (0, 0, 0)
    width = 600
    height = 400

    lst = random.sample(range(10, 100), 9)
    print(len(lst))

    draw = Draw(width, height, lst)
    draw.display_list()
    print(draw.list_display)

    while run:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
