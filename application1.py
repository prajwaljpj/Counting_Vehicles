####################################
#                                  #
#  File name: application1.py      #
#  Author: Prajwal Rao             #
#  Date created: 26/6/2018         #
#  Date last modified: 6/07/2018   #
#  Tested on Python Version: 3.5   #
#  Version: "0.9.0 (Beta)"         #
#                                  #
####################################


__author__ = "Prajwal Rao"
__email__ = ["prajwaljpj@gmail.com", "prajwalrao@iisc.ac.in"]
__version__ = "0.9.0"
__status__ = "Beta"
__maintainer__ = "Prajwal Rao"

from ImageBlock import ImageWindow
from ButtonBlock import ButtonWindow
from DataDisplayBlock import DataDisplayWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, \
    QVBoxLayout, QStatusBar, QLabel, QWidget, QFileDialog, QHBoxLayout
import os
import sys
from counter import count
import logging
import json

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1920, 1080)
        self.setWindowTitle("Ground Truthing")
        # self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        self.frame_counter = self.images_handler()
        # self.statusbar_init()
        LOGGER.info("initialised status bar")
        # menubar_init()

        vboxlayout = QVBoxLayout()
        hboxlayout = QHBoxLayout()


        # vboxlayout.addStretch(2)
        # vboxlayout.setStretch(1,2)

        self.topwid = ImageWindow()
        self.topwid.resize(self.topwid.sizeHint())
        self.botwid = ButtonWindow()
        self.botwid.resize(self.botwid.sizeHint())
        self.printer = DataDisplayWindow()
        self.topwid.image(self.frame_counter, self.printer)
        self.botwid.gridstruct(self.frame_counter, self.printer)
        self.printer.show_data(self.frame_counter)

        self.wid = QWidget(self)

        extractAction = QAction("Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        saveFile = QAction("Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save To Location')
        saveFile.triggered.connect(self.save_application)

        LOGGER.debug("frame Length = " + str(len(self.frame_counter.display_all())))

        extractNextImage = QAction("Next Frame", self)
        # extractNextImage.setShortcut("Alt+n")
        extractNextImage.setShortcut("Right")
        extractNextImage.setStatusTip("Next Frame...")
        extractNextImage.triggered.connect(lambda: self.topwid.changeimage("n", self.frame_counter, self.printer))

        extractPrevImage = QAction("Previous Frame", self)
        # extractPrevImage.setShortcut("Alt+b")
        extractPrevImage.setShortcut("Left")
        extractPrevImage.setStatusTip("Previous Frame...")
        extractPrevImage.triggered.connect(lambda: self.topwid.changeimage("b", self.frame_counter, self.printer))

        getshortcuts = QAction("Shortcuts", self)
        getshortcuts.setShortcut("Ctrl+K")
        getshortcuts.setStatusTip("Shortcuts List")
        getshortcuts.triggered.connect(lambda: self.short())

        reportBugs = QAction("Report", self)
        reportBugs.setShortcut("Ctrl+R")
        reportBugs.setStatusTip("Please report bugs")
        reportBugs.triggered.connect(lambda: self.bugreport())


        author = QLabel("Prajwal Rao\nprajwalrao@iisc.ac.in")
        author.setStyleSheet("color : grey")

        self.statusBar = QStatusBar()
        self.statusBar.addPermanentWidget(author)
        self.setStatusBar(self.statusBar)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        helpMenu = mainMenu.addMenu('&Help')


        fileMenu.addAction(extractNextImage)
        fileMenu.addAction(extractPrevImage)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(extractAction)

        helpMenu.addAction(getshortcuts)
        helpMenu.addAction(reportBugs)

        self.setCentralWidget(self.wid)

        # vboxlayout.setAlignment(QtCore.Qt.AlignCenter)
        hboxlayout.addWidget(self.topwid)
        hboxlayout.addWidget(self.printer)
        vboxlayout.addLayout(hboxlayout)
        # vboxlayout.addWidget(self.topwid)
        # print("vbox size hint: ",vboxlayout.sizeHint())
        vboxlayout.addWidget(self.botwid.groupbox)
        self.wid.setLayout(vboxlayout)

        LOGGER.info("initialised menubar")
        # self.home()
        self.show()

    # def get_frame(self, images):
    #     imgs = sorted(images, key=lambda x: int(x[6]))

    def images_handler(self):
        image_path = QFileDialog.getExistingDirectory(self, "Select Image Directory")

        # image_path = input("Enter Image Path:")
        imag = os.listdir(image_path)
        images = [os.path.join(image_path, t) for t in imag]
        # pprint(images)
        # images = self.get_frame(images)
        self.frame_counter = count()

        # images = sorted(images, key=lambda x: int(x[6]))
        for image in images:
            self.frame_counter.set(image)
        self.frame_counter.set_target_as_zero()
        # self.frame_counter.sort_dict()
        # pprint(self.frame_counter.display_all())

        return self.frame_counter

    def bugreport(self):
        reporttext = 'Please report all bugs to <a href="mailto:prajwaljpj@gmail.com">prajwaljpj@gmail.com</a>' \
                              + ' or <a href="mailto:prajwalrao@iisc.ac.in">prajwalrao@iisc.ac.in</a>'

        QMessageBox.about(QWidget(), "Report", reporttext)
        # reportmessage.setIcon(QMessageBox.Information)
        # reportmessage.setText('Please report all bugs to <a href="mailto:prajwaljpj@gmail.com">prajwaljpj@gmail.com</a>'
        #                       + ' or <a href="mailto:prajwalrao@iisc.ac.in">prajwalrao@iisc.ac.in</a>')

    def short(self):
        self.key_bindings = "Ctrl+S\t\t\tSave File as JSON\n" \
                            + "Ctrl+Q\t\t\tQuit\n" \
                            + "Right Arrow\t\t\tNext Frame\n" \
                            + "Left Arrow\t\t\tPrevious Frame\n" \
                            + "1\t\t\tAdd Small Car\n" \
                            + "Shift+1\t\t\tRemove Small Car\n" \
                            + "2\t\t\tAdd Big Car\n" \
                            + "Shift+2\t\t\tRemove Big Car\n" \
                            + "3\t\t\tAdd Bus\n" \
                            + "Shift+3\t\t\tRemove Bus\n" \
                            + "4\t\t\tAdd Two Wheeler\n" \
                            + "Shift+4\t\t\tRemove Two Wheeler\n" \
                            + "Q\t\t\tAdd Three Wheeler\n" \
                            + "Shift+Q\t\t\tRemove Three Wheeler\n" \
                            + "W\t\t\tAdd LCV\n" \
                            + "Shift+W\t\t\tRemove LCV\n" \
                            + "E\t\t\tAdd Truck\n" \
                            + "Shift+E\t\t\tRemove Truck\n" \
                            + "R\t\t\tAdd Bicycle\n" \
                            + "Shift+R\t\t\tRemove Bicycle\n\n" \
                            + "Ctrl+K\t\t\tShow Key Bindings\n" \
                            + "Ctrl+R\t\t\tReport Bugs\n"

        QMessageBox.about(QWidget(), "Shortcuts", self.key_bindings)

    def save_application(self):
        save_location = QFileDialog.getSaveFileName(self, "Save File")
        LOGGER.info(save_location)
        if not save_location[0].endswith(".json"):
            save_location[0]+=".json"
        with open(save_location[0], "w+") as file:
            writedata = self.frame_counter.display_all()
            json.dump(writedata, file)

    def close_application(self):

        choice = QMessageBox.question(self, 'Extract!',
                                      "Do you really want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)
        LOGGER.info("Quit")
        sys.exit()



def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


App = QApplication(sys.argv)

run()
