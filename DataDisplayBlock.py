from PyQt5.QtWidgets import QTextEdit
# from PyQt5.QtGui import QPixmap
# from PyQt5 import QtCore
# import os
# import sys



class DataDisplayWindow(QTextEdit):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Ground Truthing")
        self.setReadOnly(True)



    def show_data(self, frame_counter):

        # self.textEdit = QTextEdit()
        # print("ahsdfivuhasidhv`ASDASUDHFIUAWHEFIHASD")
        self.current_frame = frame_counter.find_target_frame()
        self.frame_data = frame_counter.display(self.current_frame)
        # self.setText(str(self.frame_data).replace("{", "\n\n\t").replace("}", "\n\n").replace(",", "\n\t"))
        self.setText("CURRENT FRAME DATA\n")
        for kz, va in self.frame_data.items():
            if type(va) == type({}):
                for akz, ava in va.items():
                    self.append(akz + " = " + str(ava) + "\n")
            else:
                self.append(kz + " = " + str(va) + "\n")
        # self.resize(self.sizeHint())

        # self.textEdit.show()
        # self.frame_number = frame_counter.find_target_frame()
        # self.frame_num = self.textEdit.add("Frame Number : "+str(self.frame_number))
        #
        # self.current_frame_data = frame_counter.display(self.frame_number)
        # self.frame_tim = QLabel("Frame Time Stamp : "+str(self.current_frame_data["frame_time"]))
        #
        # self.frame_pat = QLabel("Frame Path : "+self.current_frame_data["frame_path"])
        #
        # self.frame_classes = QLabel("CLASSES")

        # for entit in self.current_frame_data["classes"]:
        #     entit =

