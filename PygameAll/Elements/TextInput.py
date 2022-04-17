import pygame
from PygameAll.Elements.TextArea import TextArea


# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
class TextInput(TextArea):
    def __init__(self, window, x, y, width, height, text='', bg_color=(100,)*3):
        super().__init__(window, x, y, width, height, text, bg_color)
        self.active = False
        self.text_typed = ''
        self.TEXT_COLOR = (0,)*3

    def update(self, event):
        if event.key == pygame.K_BACKSPACE:
            print('kbackspace', self.text_typed)
            self.text_typed = self.text_typed[:-1]
            self.text = self.FONT.render(str(self.text_typed), True, self.TEXT_COLOR)
        else:
            self.text_typed += event.unicode
            self.text = self.FONT.render(str(self.text_typed), True, self.TEXT_COLOR)
            print('pisze', event.unicode)
            print(self.text)



