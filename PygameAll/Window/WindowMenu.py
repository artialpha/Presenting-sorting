from PygameAll.Elements.TextArea import TextArea
from PygameAll.Elements.TextInput import TextInput
from PygameAll.Window.Window import Window
from PygameAll.Window.WindowQuick import WindowQuick
from PygameAll.Window.WindowMerge import WindowMerge


class WindowMenu(Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        x = (self.width-self.width_button)/2
        y = self.height*(1/4)
        padding = 10
        self.button_quick = TextArea(self.window, x, y, self.width_button, self.height_button, "quick")
        self.button_merge = TextArea(self.window, x, y + padding + self.height_button, self.width_button,
                                     self.height_button, "merge")
        self.elements.append(self.button_merge)
        self.elements.append(self.button_quick)

        text_input_width = 300
        self.text_input = TextInput(self.window, (self.width-text_input_width)/2, self.height/10, text_input_width,
                                   50, bg_color=(255,)*3)
        self.elements.append(self.text_input)

    def buttons_clicked_check(self, event, draw=None):
        def get_lst_from_input(text):
            return [int(x) for x in text.split()]

        props = [item[1] for item in draw.__dict__.items()]

        if self.button_quick.rect.collidepoint(event.pos):
            lst = get_lst_from_input(self.text_input.text_typed)
            return WindowQuick(*props[:2], lst)
        elif self.button_merge.rect.collidepoint(event.pos):
            lst = get_lst_from_input(self.text_input.text_typed)
            return WindowMerge(*props[:2], lst)
        elif self.text_input.rect.collidepoint(event.pos):
            print(self.text_input.rect, event.pos, 'text input rect')
            self.text_input.active = True
        else:
            self.text_input.active = False

    def type_text(self, event):
        if self.text_input.active:
            self.text_input.update(event)


