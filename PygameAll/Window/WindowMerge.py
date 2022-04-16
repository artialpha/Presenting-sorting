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

        x = self.width/2
        y = self.height*(3/4)-50
        padding = 10
        self.max_steps = Text(self.window, x + padding, y, str(len(self.list_draw.merge_sort_data.states) - 1))
        max_steps_width = self.max_steps.text.get_size()[0]
        self.current_number = Text(self.window, x - max_steps_width - padding, y, '0')

        self.elements.append(self.current_number)
        self.elements.append(self.max_steps)

    def buttons_clicked_check(self, event, draw=None):
        if self.button_next.rect.collidepoint(event.pos):
            if self.list_draw.state_counter < len(self.list_draw.merge_sort_data.states) - 1:
                print('next merge')
                self.list_draw.state_counter += 1
                self.list_draw.state_display()
        if self.button_prev.rect.collidepoint(event.pos) and self.list_draw.state_counter > 0:
            print('prev megre')
            self.list_draw.reverse_state()
        self.current_number.text = self.list_draw.state_counter




