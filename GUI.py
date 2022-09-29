import tkinter as tk
import tkinter.font as tkFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial
from Hopfield import Hopfield
from utils import *


class GUI:
    def __init__(self):
        self.model = Hopfield()
        self.testcase_num = 3
        self.showing_index = 0

        self.window = tk.Tk()
        self.window.title("Hopfield")
        self.window.geometry("1600x600")
        self.window.configure(background="white")
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(family="Consolas", size=12)

        # 以下為 result_frame 群組
        self.result_frame = tk.Frame(self.window, height=4, width=4)
        self.result_frame.grid(row=0, column=0)
        self.result_figure = Figure()
        self.orig_plot = self.result_figure.add_subplot(121)
        self.orig_plot.set_title("Orignal:")
        self.orig_plot.axis("off")
        self.result_plot = self.result_figure.add_subplot(122)
        self.result_plot.set_title("Result:")
        self.result_plot.axis("off")
        self.result_canvas = FigureCanvasTkAgg(
            self.result_figure, master=self.result_frame
        )
        self.result_canvas.get_tk_widget().grid(
            column=0, row=0, rowspan=2, columnspan=4
        )
        self.result_controlls_label = tk.Label(self.result_frame, text="Index : 0")
        self.result_controlls_label.grid(row=2, column=0, columnspan=4)
        self.result_controlls_button_left = tk.Button(
            self.result_frame, text="<", command=partial(change_show, self, action="<")
        )
        self.result_controlls_button_left.grid(row=3, column=0, columnspan=2)
        self.result_controlls_button_right = tk.Button(
            self.result_frame, text=">", command=partial(change_show, self, action=">")
        )
        self.result_controlls_button_right.grid(row=3, column=2, columnspan=2)

        # 以下為 data_frame 群組
        self.data_frame = tk.Frame(self.window, height=7, width=4)
        self.data_frame.grid(row=0, column=1)
        self.data_train_label = tk.Label(self.data_frame, text="Select train data:")
        self.data_train_label.grid(row=0, column=0)
        self.data_train_explorer_label = tk.Label(
            self.data_frame, text="Not chosen yet"
        )
        self.data_train_explorer_label.grid(row=1, column=0, columnspan=3)
        self.data_train_explore_button = tk.Button(
            self.data_frame,
            text="Browse",
            command=partial(browse, self, target="train"),
        )
        self.data_train_explore_button.grid(row=1, column=3)
        self.data_train_button = tk.Button(
            self.data_frame, text="Train", command=partial(train, self)
        )
        self.data_train_button.grid(row=2, column=0, columnspan=4)
        self.data_noise_test_button = tk.Button(
            self.data_frame, text="noise test", command=partial(noise_test, self)
        )
        self.data_noise_test_button.grid(row=3, column=0, columnspan=4)
        self.data_test_label = tk.Label(self.data_frame, text="Select test data:")
        self.data_test_label.grid(row=4, column=0)
        self.data_test_explorer_label = tk.Label(self.data_frame, text="Not chosen yet")
        self.data_test_explorer_label.grid(row=5, column=0, columnspan=3)
        self.data_test_explore_button = tk.Button(
            self.data_frame, text="Browse", command=partial(browse, self, target="test")
        )
        self.data_test_explore_button.grid(row=5, column=3)
        self.data_test_button = tk.Button(
            self.data_frame, text="Test", command=partial(test, self)
        )
        self.data_test_button.grid(row=6, column=0, columnspan=4)

        # 以下為 attribute_frame 群組
        self.attribute_frame = tk.Frame(self.window, height=6, width=3)
        self.attribute_frame.grid(row=0, column=2)
        self.attribute_label = tk.Label(self.attribute_frame, text="Attributes")
        self.attribute_label.grid(row=0, column=0, columnspan=3)
        self.attribute_pattern_num_label = tk.Label(
            self.attribute_frame, text="Pattern Number:"
        )
        self.attribute_pattern_num_label.grid(row=1, column=0)
        self.attribute_pattern_num_entry = tk.Entry(self.attribute_frame, width=10)
        self.attribute_pattern_num_entry.grid(row=1, column=1, columnspan=2)
        self.attribute_dimension_label = tk.Label(
            self.attribute_frame, text="Dimension:"
        )
        self.attribute_dimension_label.grid(row=2, column=0)
        self.attribute_dimension_x_entry = tk.Entry(self.attribute_frame, width=5)
        self.attribute_dimension_x_entry.grid(row=2, column=1)
        self.attribute_dimension_y_entry = tk.Entry(self.attribute_frame, width=5)
        self.attribute_dimension_y_entry.grid(row=2, column=2)
        self.attribute_train_load_button = tk.Button(
            self.attribute_frame,
            text="Load",
            command=partial(load_attribute, self, target="train"),
        )
        self.attribute_train_load_button.grid(row=3, column=0, columnspan=3)
        # self.attribute_test_num_label = tk.Label(
        #     self.attribute_frame, text="Test Number:"
        # )
        # self.attribute_test_num_label.grid(row=4, column=0)
        # self.attribute_test_num_entry = tk.Entry(self.attribute_frame, width=10)
        # self.attribute_test_num_entry.grid(row=4, column=1, columnspan=2)
        # self.attribute_test_load_button = tk.Button(
        #     self.attribute_frame,
        #     text="Load",
        #     command=partial(load_attribute, self, target="test"),
        # )
        # self.attribute_test_load_button.grid(row=5, column=0, columnspan=3)


if __name__ == "__main__":
    gui = GUI()
    # model = Hopfield()
    gui.window.mainloop()
