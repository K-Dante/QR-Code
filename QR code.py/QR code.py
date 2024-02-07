# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt.QtGui import *
from PyQt.QtCore import *
import qrcode
import sys

# Image class fro QR code
class Image(qrcode.image.base.Baseimage):

    #constrructor
    def __init__(self, border, width, box_size):

        #assigning bother
        self.border = border

        #assignng width
        self.width = width
    
        #assigning bos size
        self.box_size = box_size

        #creating a size
        size = (width + border * 2) * box_size
    
        #image
        self._image = QImage(size, size, QImage.Format_RGB16)
    
        #Initial image as white
        self._image.fill(Qt.white)
    
    #prixmap method
    def pixmap(self):

        # returns image
        return QPixmap.fromImage(self._image)
    
    #drawrect method for drawing rectangle
    def drawrect(self, row, col):

        # creating painter object
        painter = QPainter(self._image)
        
        # drawing rectangle
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.bordeer) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)
        


#Main Window Class
class Window(QMainWindow):

    # constructor
    def __init__(self):

        #setting window title
        self.setWindowTitle("QR code")

        #setting geometry
        self.setGeometry(100, 100, 300, 300)

        #creating a label to show the qr code
        self.label = Qlabel(self)

        #creating a line to edit receive text
        self.edit = QlineEdit(self)

        #adding action when entered in pressed
        self.edit.returnPressed,connect(self.handleTextEntered)

        #setting font to the line edit
        self.edit.setFont(QFont('Times', 9))

        #setting alignemt
        self.edit.setAlignment(Qt.AligCenter)

        #creating a vertical layout
        layout = QVBoxLayout(self)

        #adding label to layout
        layout.addWidget(self.label)

        #adding line to edit the layout
        layout.addWidget(self.edit)
        
        #creating a QWidget object
        widget = QWidget()
          
        #setting layout to the widget
        widget.setLayout(layout)

        #setting widget as a central widget to the main window
        self.setCentralWidget(widget)
    

    # method called by the line edit
    def handleTextEntered(self):

        #get the text
        text = self.edit.text()

        #creating a pix map of qr
        qr_image = qrcode.make(text, image_factory = Image).pixmap()

        # set image to the label
        self.label.setPixmap(qr_image)





#create pyqt5
app = QApplication(sys.argv)

#creating the instance of our Window
window = Window()

# showin window
window.show()

#start the app
sys.exit(app.exec_())