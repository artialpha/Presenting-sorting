from PygameAll.Window.Window import Window
from PygameAll.Elements.TextArea import TextArea
from PygameAll.Elements.Text import Text
from PygameAll.AlgsDraw.MergeListDraw import MergeListDraw


class WindowMerge(Window):

    def __init__(self, width, height, lst):
        super().__init__(width, height)
        self.list_draw = MergeListDraw(lst, self.window, self.width, self.height)
        self.elements = []
        self.elements.append(self.list_draw)

        # Buttons
        x = self.width/2
        y = self.height*(3/4)
        padding = 10
        self.button_prev = TextArea(self.window, x - self.width_button - padding, y, self.width_button,
                                    self.height_button, "prev")
        self.button_next = TextArea(self.window, x + padding, y, self.width_button, self.height_button, "next")
        self.elements.append(self.button_next)
        self.elements.append(self.button_prev)

    def buttons_clicked_check(self, event, draw=None):
        if self.button_next.rect.collidepoint(event.pos):
            print('next merge')
            self.list_draw.state_counter += 1
            self.list_draw.state_display()
        if self.button_prev.rect.collidepoint(event.pos):
            print('prev megre')
            self.list_draw.state_counter -= 1
            self.list_draw.state_display()




