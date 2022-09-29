from Hopfield import Hopfield
from tkinter import filedialog
import numpy as np
import matplotlib.patches as patches
import random
import os

# temp
# import tkinter as tk
# from functools import partial
# import tkinter.font as tkFont
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

NOISE_FACTOR = 0.2


def browse(obj, target):
    filename = filedialog.askopenfilename(
        initialdir="./Data",
        title="Select a File",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )

    if target == "train":
        obj.data_train_explorer_label.configure(text=filename)
    elif target == "test":
        obj.data_test_explorer_label.configure(text=filename)


def load_attribute(obj, target):
    if target == "train":
        pattern_num = int(obj.attribute_pattern_num_entry.get())
        dim_x = int(obj.attribute_dimension_x_entry.get())
        dim_y = int(obj.attribute_dimension_y_entry.get())
        obj.model = Hopfield(n=pattern_num, dim=[dim_x, dim_y])
    # elif target == "test":
    #     test_num = int(obj.attribute_test_num_entry.get())
    #     obj.testcase_num = test_num


def train(obj):
    directory = obj.data_train_explorer_label.cget("text")
    obj.model.train(directory=directory)


def noise_test(obj):
    directory = obj.data_train_explorer_label.cget("text")
    with open(directory, "r") as f:
        with open("./Data/noise.txt", "w") as f2:
            for line in f:
                for c in line:
                    if c != "\n" and random.random() < NOISE_FACTOR:
                        f2.write(" " if c == "1" else "1")
                    else:
                        f2.write(c)
            f2.write("\n")

    obj.model.test(directory="./Data/noise.txt", case=obj.model.n)
    obj.showing_index = 0
    show(obj)
    # os.remove("./noise.txt")


def test(obj):
    directory = obj.data_test_explorer_label.cget("text")
    obj.model.test(directory=directory, case=obj.model.n)
    obj.showing_index = 0
    show(obj)


def show(obj):
    index = obj.showing_index
    obj.result_controlls_label.configure(text="Index : {:d}".format(index))
    x = obj.model.origins[index]
    y = obj.model.results[index]

    for i in range(obj.model.dim[0]):
        for j in range(obj.model.dim[1]):
            rect = patches.Rectangle(
                (j, obj.model.dim[0] - 1 - i),
                1,
                1,
                edgecolor="white",
                facecolor="black" if x[i * obj.model.dim[1] + j] == 1 else "white",
                fill=True,
            )
            obj.orig_plot.add_patch(rect)

    obj.orig_plot.set_xlim([0, obj.model.dim[1]])
    obj.orig_plot.set_ylim([0, obj.model.dim[0]])

    for i in range(obj.model.dim[0]):
        for j in range(obj.model.dim[1]):
            rect = patches.Rectangle(
                (j, obj.model.dim[0] - 1 - i),
                1,
                1,
                edgecolor="white",
                facecolor="black" if y[i * obj.model.dim[1] + j] == 1 else "white",
                fill=True,
            )
            obj.result_plot.add_patch(rect)

    obj.result_plot.set_xlim([0, obj.model.dim[1]])
    obj.result_plot.set_ylim([0, obj.model.dim[0]])

    obj.result_canvas.draw()
    obj.window.update()


def change_show(obj, action):
    if action == ">":
        if obj.showing_index + 1 >= obj.model.n:
            return
        obj.showing_index += 1
        show(obj)
    elif action == "<":
        if obj.showing_index - 1 < 0:
            return
        obj.showing_index -= 1
        show(obj)


# class tmp:
#     def __init__(self):
#         self.model = Hopfield()
#         self.model.train()
#         self.model.test()
#         self.showing_index = 0

#         self.window = tk.Tk()
#         self.window.title("Hopfield")
#         self.window.geometry("1600x600")
#         self.window.configure(background="white")
#         self.default_font = tkFont.nametofont("TkDefaultFont")
#         self.default_font.configure(family="Consolas", size=12)

#         # 以下為 result_frame 群組
#         self.result_frame = tk.Frame(self.window, height=5, width=4)
#         self.result_frame.grid(row=0, column=0)
#         self.result_figure = Figure()
#         self.orig_plot = self.result_figure.add_subplot(121)
#         self.orig_plot.set_title("Orignal:")
#         self.orig_plot.axis("off")
#         self.result_plot = self.result_figure.add_subplot(122)
#         self.result_plot.set_title("Result:")
#         self.result_plot.axis("off")
#         self.result_canvas = FigureCanvasTkAgg(
#             self.result_figure, master=self.result_frame
#         )
#         self.result_canvas.get_tk_widget().grid(
#             column=0, row=0, rowspan=2, columnspan=4
#         )
#         self.result_controlls_label = tk.Label(self.result_frame, text="Index : 0")
#         self.result_controlls_label.grid(row=2, column=0, columnspan=4)
#         self.result_controlls_button_left = tk.Button(
#             self.result_frame, text="<", command=partial(change_show, self, action="<")
#         )
#         self.result_controlls_button_left.grid(row=3, column=0, columnspan=2)
#         self.result_controlls_button_right = tk.Button(
#             self.result_frame, text=">", command=partial(change_show, self, action=">")
#         )
#         self.result_controlls_button_right.grid(row=3, column=2, columnspan=2)
#         self.SHOWBtn = tk.Button(
#             self.result_frame, text="SHOW", command=partial(show, self)
#         )
#         self.SHOWBtn.grid(row=4, column=0, columnspan=4)


# if __name__ == "__main__":
#     obj = tmp()
#     obj.window.mainloop()
