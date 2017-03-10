from Tkinter import *
from random import choice

# TODO - Eventually we'll make this more flexible. For now: Fuck yeah, Nord.

COLORS = [
    "#2E3440",  # Polar Night
    "#3B4252",  # Polar Night
    "#434C5E",  # Polar Night
    "#4C566A",  # Polar Night
    "#D8DEE9",  # Snow storm
    "#ECEFF4",  # Snow storm
    "#E5E9F0",  # Snow storm
    "#8FBCBB",  # Frost
    "#88C0D0",  # Frost
    "#81A1C1",  # Frost
    "#5E81AC",  # Frost
    "#BF616A",  # Aurora
    "#D08770",  # Aurora
    "#EBCB8B",  # Aurora
    "#A3BE8C",  # Aurora
    "#B48EAD",  # Aurora
    ]


class ColorBox:
    def __init__(self, master, x, y, box_size, color):
        master.wm_overrideredirect(True)
        # TODO - Include other shapes
        self.canvas_one = Canvas(master, width=box_size, height=box_size,
                                 bg=color,
                                 highlightthickness=0)
        self.canvas_one.grid(row=x, column=y)
        # TODO - Dragging mouse over window should change box colors
        self.canvas_one.bind("<Button>", self.change_color, self.canvas_one)

    def change_color(self, event):
        c = choice(COLORS)
        self.canvas_one.configure(bg=c)
        return c

    def put_back(self):
        self.master.lower()
        self.master.after(100, self.put_back)


class Run:
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(True)
        self.root.resizable(width=False, height=False)
        self.root.configure(bg=COLORS[0])
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry('%dx%d+%d+%d' % (self.screen_width, self.screen_height, 0, 0))

    def create_squares(self, block_size):
        x = 0
        y = 0
        for x in range(0, int(self.screen_height / block_size) + 1):
            for y in range(0, int(self.screen_width / block_size) + 1):
                win = ColorBox(self.root, x, y, block_size, COLORS[0])

    def push_back(self):
        self.root.lower()
        self.root.after(100, self.push_back)


def main():
    App = Run()
    App.create_squares(50)
    App.push_back()
    App.root.mainloop()


if __name__ == '__main__':
    # TODO - pretty much anything >30 makes this thing process for way too long
    # Note: multiples of 3 - is that standard on other systems?
    size = 27
    if size % 3 == 0 and size > 25:
        main()
    else:
        print("Multiple of 3, please")

# TODO - Add option to save current image or somethin.
# TODO - Make this 'smarter'. Not just random. Some pattern or some shit.
# TODO - It'd be cool if it were a single color and
#        just random squares would change.
