from tkinter import simpledialog as sd

import numpy as np

from ..functions import dp, pdd
from ..resources.language import Text
from .profile import ProfileHandler


class Measurement:
    def __init__(self, filepath, type):

        self.filepath = filepath
        self.filename = self.filepath.split("/")[-1][:-4]

        if type == "pdd":
            self.direction = "Z"
        else:
            answer = sd.askquestion(
                "", self.Text().scanaxis[ProfileHandler().get_attribute("language")]
            )
            if answer == "yes":
                self.direction = "X"
            else:
                self.direction = "Y"

        if filepath.endswith(".txt"):
            data = np.loadtxt(self.filepath, unpack=True)
        else:
            data = np.genfromtxt(self.filepath, delimiter=",", unpack=True)

        self.axis, self.dose = data[0], data[1]
        if self.direction != "Z":
            self.axis = np.array(
                [x - (max(self.axis) + min(self.axis)) / 2 for x in self.axis]
            )
        maximum = max(self.dose)
        self.norm_dose = np.array([value / maximum for value in self.dose])

        try:
            self.std_dev = data[2]
        except IndexError:
            self.std_dev = []

        self.normpoint = max(self.dose)

        if self.direction == "Z":
            self.params = pdd.calculate_parameters(
                self.axis, self.dose / max(self.dose), self.std_dev
            )
        else:
            self.params = dp.calculate_parameters(
                self.axis, self.dose / max(self.dose), self.std_dev
            )

        self.axis = self.axis.tolist()

        self.axis = {True: self.axis[len(self.axis) // 2 :], False: self.axis}
        self.dose = {True: self.dose[len(self.dose) // 2 :], False: self.dose}
        if self.std_dev != None:
            self.std_dev = self.std_dev = {
                True: self.std_dev[len(self.std_dev) // 2 :],
                False: self.std_dev,
            }

        else:
            self.std_dev = {
                True: self.std_dev,
                False: self.std_dev,
            }
