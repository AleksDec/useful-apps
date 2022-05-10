from PyQt6 import QtCore, QtGui, QtWidgets

import PIL.Image as MyImage
import PIL.ImageDraw as MyImgDraw
import PIL.ImageFont as MyImgFont

from datetime import datetime


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(500, 650)
        AppWindow.setMaximumSize(QtCore.QSize(600, 2000))
        self.centralwidget = QtWidgets.QWidget(AppWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RoundFrame = QtWidgets.QFrame(self.centralwidget)
        self.RoundFrame.setMaximumSize(QtCore.QSize(400, 600))
        self.RoundFrame.setSizeIncrement(QtCore.QSize(20, 20))
        self.RoundFrame.setStyleSheet("background-color: rgb(35, 30, 35);\n"
"border-radius: 20px;\n"
"font: 700 12pt \"Corbel\";\n"
"font-color:rgb(57, 166, 163)")
        self.RoundFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.RoundFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.RoundFrame.setObjectName("RoundFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.RoundFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InnerFrame = QtWidgets.QFrame(self.RoundFrame)
        self.InnerFrame.setMaximumSize(QtCore.QSize(360, 500))
        self.InnerFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.InnerFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.InnerFrame.setObjectName("InnerFrame")
        self.WatermarkCreator = QtWidgets.QLabel(self.InnerFrame)
        self.WatermarkCreator.setGeometry(QtCore.QRect(30, 0, 300, 50))
        self.WatermarkCreator.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.WatermarkCreator.setFont(font)
        self.WatermarkCreator.setStyleSheet("color: rgb(222, 238, 234);\n"
"font: 700 20pt \"Segoe Print\";")
        self.WatermarkCreator.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.WatermarkCreator.setObjectName("WatermarkCreator")
        self.widget = QtWidgets.QWidget(self.InnerFrame)
        self.widget.setGeometry(QtCore.QRect(30, 100, 300, 400))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.WidgetsFrame = QtWidgets.QFrame(self.widget)
        self.WidgetsFrame.setMinimumSize(QtCore.QSize(300, 400))
        self.WidgetsFrame.setMaximumSize(QtCore.QSize(300, 400))
        self.WidgetsFrame.setSizeIncrement(QtCore.QSize(20, 20))
        self.WidgetsFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.WidgetsFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.WidgetsFrame.setMidLineWidth(0)
        self.WidgetsFrame.setObjectName("WidgetsFrame")
        self.ChooseImage = QtWidgets.QLineEdit(self.WidgetsFrame)
        self.ChooseImage.setGeometry(QtCore.QRect(0, 0, 300, 30))
        self.ChooseImage.setMinimumSize(QtCore.QSize(300, 30))
        self.ChooseImage.setMaximumSize(QtCore.QSize(300, 30))
        self.ChooseImage.setStyleSheet("background-color: rgb(57, 166, 163);\n"
"border-radius:10px;")
        self.ChooseImage.setObjectName("ChooseImage")
        self.ChooseWatermarkType = QtWidgets.QComboBox(self.WidgetsFrame)
        self.ChooseWatermarkType.setGeometry(QtCore.QRect(0, 55, 300, 30))
        self.ChooseWatermarkType.setMinimumSize(QtCore.QSize(300, 30))
        self.ChooseWatermarkType.setMaximumSize(QtCore.QSize(300, 30))
        self.ChooseWatermarkType.setStyleSheet("background-color: rgb(191, 19, 99);\n"
"border-radius:5px;\n"
"color: rgb(222, 238, 234);\n"
"font: 12pt \"Segoe Print\";")
        self.ChooseWatermarkType.setObjectName("ChooseWatermarkType")
        self.ChooseWatermarkType.addItem("Image")
        self.ChooseWatermarkType.addItem("Inscription")
        self.Image_Inscription = QtWidgets.QLineEdit(self.WidgetsFrame)
        self.Image_Inscription.setGeometry(QtCore.QRect(0, 110, 300, 30))
        self.Image_Inscription.setMinimumSize(QtCore.QSize(300, 30))
        self.Image_Inscription.setMaximumSize(QtCore.QSize(300, 30))
        self.Image_Inscription.setStyleSheet("background-color: rgb(57, 166, 163);\n"
"border-radius:10px;")
        self.Image_Inscription.setObjectName("Image_Inscription")

        self.ChooseFont = QtWidgets.QComboBox(self.WidgetsFrame)
        self.ChooseFont.setGeometry(QtCore.QRect(0, 170, 300, 30))
        self.ChooseFont.setMinimumSize(QtCore.QSize(300, 30))
        self.ChooseFont.setMaximumSize(QtCore.QSize(300, 30))
        self.ChooseFont.setStyleSheet("background-color: rgb(191, 19, 99);\n"
                                      "border-radius:5px;\n"
                                      "color: rgb(222, 238, 234);\n"
                                      "font: 12pt \"Segoe Print\";")
        self.ChooseFont.setObjectName("ChooseFont")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")
        self.ChooseFont.addItem("")

        self.InputPosition = QtWidgets.QLineEdit(self.WidgetsFrame)
        self.InputPosition.setGeometry(QtCore.QRect(0, 220, 300, 30))
        self.InputPosition.setMinimumSize(QtCore.QSize(300, 30))
        self.InputPosition.setMaximumSize(QtCore.QSize(300, 30))
        self.InputPosition.setStyleSheet("background-color: rgb(57, 166, 163);\n"
"border-radius:10px;")
        self.InputPosition.setObjectName("InputPosition")
        self.InputColor = QtWidgets.QLineEdit(self.WidgetsFrame)
        self.InputColor.setGeometry(QtCore.QRect(0, 275, 300, 30))
        self.InputColor.setMinimumSize(QtCore.QSize(300, 30))
        self.InputColor.setMaximumSize(QtCore.QSize(300, 30))
        self.InputColor.setStyleSheet("background-color: rgb(57, 166, 163);\n"
"border-radius:10px;")
        self.InputColor.setObjectName("InputColor")
        self.pushButton = QtWidgets.QPushButton(self.WidgetsFrame)
        self.pushButton.setGeometry(QtCore.QRect(100, 340, 100, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton.clicked.connect(self.btn_clicked)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(35, 30, 35);\n"
"background-color: rgb(222, 238, 234);\n"
"border-radius:10px;\n"
"font: 700 16pt \"Segoe Print\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.WidgetsFrame)
        self.horizontalLayout.addWidget(self.InnerFrame)
        self.verticalLayout.addWidget(self.RoundFrame)
        AppWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName("menubar")
        AppWindow.setMenuBar(self.menubar)

        self.retranslateUi(AppWindow)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

# ----------  Create Watermark --------------
    def btn_clicked(self):
        # Get the image
        choose_image_path = self.ChooseImage.text()
        img: MyImage.Image = MyImage.open(choose_image_path)
        # choose_type = self.ChooseWatermarkType.currentText()
        # Get Inscription
        inscription = self.Image_Inscription.text()
        # Get Font
        choose_font = self.ChooseFont.currentText()
        MyFont = MyImgFont.truetype(choose_font, 28)
        # Get Position
        position = self.InputPosition.text()
        position = tuple(map(int, position.split(',')))
        # Get Color
        color = self.InputColor.text()
        color = tuple(map(int, color.split(',')))
        # Draw Watermark
        ImgDraw = MyImgDraw.Draw(img)
        ImgDraw.text(position, inscription, font=MyFont, fill=color)#red,green,blue
        # Show image
        img.show()
        # Save image
        img.save(r"Enter your save path")

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "MainWindow"))
        self.WatermarkCreator.setText(_translate("AppWindow", "Watermark Creator"))
        self.ChooseImage.setPlaceholderText("Input image path, Example : C:/Users/... ")
        self.ChooseWatermarkType.setItemText(0, _translate("AppWindow", "Image"))
        self.ChooseWatermarkType.setItemText(1, _translate("AppWindow", "Inscription"))
        self.Image_Inscription.setPlaceholderText("Write Inscription")
        self.InputPosition.setPlaceholderText("Input position, Example : 20,40 ")
        self.InputColor.setPlaceholderText("Input, Example : 20,40,60 ")
        self.pushButton.setText(_translate("AppWindow", "Create"))
        self.ChooseFont.setItemText(0, _translate("AppWindow", "BERNHC.TTF"))
        self.ChooseFont.setItemText(1, _translate("AppWindow", "BAUHS93.TTF"))
        self.ChooseFont.setItemText(2, _translate("AppWindow", "FELIXTI.TTF"))
        self.ChooseFont.setItemText(3, _translate("AppWindow", "lucon.ttf"))
        self.ChooseFont.setItemText(4, _translate("AppWindow", "TEMPSITC.TTF"))
        self.ChooseFont.setItemText(5, _translate("AppWindow", "technic_.ttf"))
        self.ChooseFont.setItemText(6, _translate("AppWindow", "swissko.ttf"))
        self.ChooseFont.setItemText(7, _translate("AppWindow", "supef___.ttf"))
        self.ChooseFont.setItemText(8, _translate("AppWindow", "SCRIPTBL.TTF"))
        self.ChooseFont.setItemText(9, _translate("AppWindow", "Revit_HEB_DWG.ttf"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppWindow = QtWidgets.QMainWindow()
    ui = Ui_AppWindow()
    ui.setupUi(AppWindow)
    AppWindow.show()
    sys.exit(app.exec())
