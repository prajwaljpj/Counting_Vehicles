from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
# import os
# import sys
# import logging


class ImageWindow(QLabel):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Ground Truthing")
        # self.height = 1080
        # self.width = 1920
        # self.resize(960, 540)
        print("size hint op: ", self.sizeHint())
        self.ImageWidth = 1450
        self.ImageHeight = 1000
        # sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # sizePolicy.setHeightForWidth(True)
        # self.setSizePolicy(sizePolicy)
        # self.frame_label = QLabel(self)
        # self.frame_label.setScaledContents(True)
        # self.image()
        # print("created image widget")
        # self.show()

    def image(self, frame_counter, printer):
        # self.frame_label = QLabel(self)
        # self.frame_label.setGeometry(0, 0, 1500, 1000)
        frame_extract = QPixmap(frame_counter.display(0)["frame_path"])
        printer.show_data(frame_counter)
        # frame_extract = frame_extract.scaled(960, 540, QtCore.Qt.KeepAspectRatio)
        frame_extract = frame_extract.scaled(self.ImageWidth, self.ImageHeight, QtCore.Qt.KeepAspectRatio)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(frame_extract)
        # print(self.frame_label.sizeHint())

        # self.frame_label.resize(self.frame_label.sizeHint())
        print("widget size: ", self.size())

    def changeimage(self, command, frame_counter, printer):
        # print(command, frame_counter)
        if command == "n" or command == "N":
            tf = frame_counter.find_target_frame()
            nf = tf+1
            worked, path = frame_counter.set_target_frame(nf)
            if worked:
                frame_extract = QPixmap(path)
                # frame_extract = frame_extract.scaled(960, 540, QtCore.Qt.KeepAspectRatio)
                frame_extract = frame_extract.scaled(self.ImageWidth, self.ImageHeight, QtCore.Qt.KeepAspectRatio)
                self.setAlignment(QtCore.Qt.AlignCenter)
                self.setPixmap(frame_extract)
                printer.show_data(frame_counter)
            # return worked
            # return self.fromlist(frame_counter, True)

        elif command == "b" or command == "B":
            tf = frame_counter.find_target_frame()
            bf = tf-1
            worked, path = frame_counter.set_target_frame(bf)
            if worked:
                frame_extract = QPixmap(path)
                # frame_extract = frame_extract.scaled(960, 540, QtCore.Qt.KeepAspectRatio)
                frame_extract = frame_extract.scaled(self.ImageWidth, self.ImageHeight, QtCore.Qt.KeepAspectRatio)
                self.setAlignment(QtCore.Qt.AlignCenter)
                self.setPixmap(frame_extract)
                printer.show_data(frame_counter)
            # return worked

            # return self.fromlist(frame_counter, False)
