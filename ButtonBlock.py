from PyQt5.QtWidgets import QPushButton, QGridLayout, QGroupBox, QWidget, QSizePolicy
# from PyQt5.QtGui import QPixmap
# from PyQt5 import QtCore
# import os
# import sys

# import counter



class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ground Truthing")
        # self.gridstruct()
        # print("created button widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        # self.show()
    def gridstruct(self, frame_counter, printer):

        self.groupbox = QGroupBox("Counter")
        # print (self.sizeHint())
        # self.groupbox.resize(640, 240)
        gridlayout = QGridLayout()

        small_car_plus = QPushButton("small car +")
        small_car_plus.setStatusTip("Add Small Car (Shortcut : 1)")
        small_car_plus.setShortcut("1")
        gridlayout.addWidget(small_car_plus, 0, 0)
        small_car_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "small_car", True))

        big_car_plus = QPushButton("big car +")
        big_car_plus.setStatusTip("Add Big car (Shortcut : 2)")
        big_car_plus.setShortcut("2")
        gridlayout.addWidget(big_car_plus, 0, 1)
        big_car_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "big_car", True))

        bus_plus = QPushButton("bus +")
        bus_plus.setStatusTip("Add Bus (Shortcut : 3)")
        bus_plus.setShortcut("3")
        gridlayout.addWidget(bus_plus, 0, 2)
        bus_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "buses", True))

        two_wheeler_plus = QPushButton("two wheeler +")
        two_wheeler_plus.setStatusTip("Add Two-Wheeler (Shortcut : 4)")
        two_wheeler_plus.setShortcut("4")
        gridlayout.addWidget(two_wheeler_plus, 0, 3)
        two_wheeler_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "two_wheeler", True))

        three_wheeler_plus = QPushButton("three wheeler +")
        three_wheeler_plus.setStatusTip("Add Three-Wheeler (Shortcut : q)")
        three_wheeler_plus.setShortcut("q")
        gridlayout.addWidget(three_wheeler_plus, 3, 0)
        three_wheeler_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "three_wheeler", True))

        LCV_plus = QPushButton("LCV +")
        LCV_plus.setStatusTip("Add LCV (Shortcut : w)")
        LCV_plus.setShortcut("w")
        gridlayout.addWidget(LCV_plus, 3, 1)
        LCV_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "LCV", True))

        trucks_plus = QPushButton("trucks +")
        trucks_plus.setStatusTip("Add Truck (Shortcut : e)")
        trucks_plus.setShortcut("e")
        gridlayout.addWidget(trucks_plus, 3, 2)
        trucks_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "trucks", True))

        bicycle_plus = QPushButton("bicycle +")
        bicycle_plus.setStatusTip("Shortcut : r")
        bicycle_plus.setShortcut("r")
        gridlayout.addWidget(bicycle_plus, 3, 3)
        bicycle_plus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "bicycle", True))


        small_car_minus = QPushButton("small car -")
        small_car_minus.setStatusTip("Shortcut : Shift+1")
        small_car_minus.setShortcut("!")
        gridlayout.addWidget(small_car_minus, 1, 0)
        small_car_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "small_car", False))

        big_car_minus = QPushButton("big car -")
        big_car_minus.setStatusTip("Shortcut : Shift+2")
        big_car_minus.setShortcut("@")
        gridlayout.addWidget(big_car_minus, 1, 1)
        big_car_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "big_car", False))

        bus_minus = QPushButton("bus -")
        bus_minus.setStatusTip("Shortcut : Shift+3")
        bus_minus.setShortcut("#")
        gridlayout.addWidget(bus_minus, 1, 2)
        bus_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "buses", False))

        two_wheeler_minus = QPushButton("two wheeler -")
        two_wheeler_minus.setStatusTip("Shortcut : Shift+4")
        two_wheeler_minus.setShortcut("$")
        gridlayout.addWidget(two_wheeler_minus, 1, 3)
        two_wheeler_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "two_wheeler", False))

        three_wheeler_minus = QPushButton("three wheeler -")
        three_wheeler_minus.setStatusTip("Shortcut : Shift+q")
        three_wheeler_minus.setShortcut("Shift+Q")
        gridlayout.addWidget(three_wheeler_minus, 4, 0)
        three_wheeler_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "three_wheeler", False))

        LCV_minus = QPushButton("LCV -")
        LCV_minus.setStatusTip("Shortcut : Shift+w")
        LCV_minus.setShortcut("Shift+W")
        gridlayout.addWidget(LCV_minus, 4, 1)
        LCV_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "LCV", False))

        trucks_minus = QPushButton("trucks -")
        trucks_minus.setStatusTip("Shortcut : Shift+e")
        trucks_minus.setShortcut("Shift+E")
        gridlayout.addWidget(trucks_minus, 4, 2)
        trucks_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "trucks", False))

        bicycle_minus = QPushButton("bicycle -")
        bicycle_minus.setStatusTip("Shortcut : Shift+r")
        bicycle_minus.setShortcut("Shift+R")
        gridlayout.addWidget(bicycle_minus, 4, 3)
        bicycle_minus.clicked.connect(lambda: self.button_is_clicked(frame_counter, printer, "bicycle", False))

        print("button block size", self.size())
        # self.resize(640, 240)
        self.groupbox.setLayout(gridlayout)

    def button_is_clicked(self, frame_counter, printer, entity, add_or_minus):
        if add_or_minus == True:
            frame_counter.add_entity(entity)
        elif add_or_minus == False:
            frame_counter.remove_entity(entity)
        printer.show_data(frame_counter)
