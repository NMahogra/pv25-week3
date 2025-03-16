import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel

class MouseTracking (QWidget):
    def __init__(self):
        super().__init__()
        self.ini_ui()

    def ini_ui(self):
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Task Week 3 - (Apta Mahogra Bhamakerti - F1D022035)')
        layout = QVBoxLayout()
        self.moving_label = QLabel('x: 0, y: 0', self)
        self.moving_label.move(0, 0)
        self.setMouseTracking(True)
        self.setLayout(layout)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.moving_label.setText(f'x: {x}, y: {y}')

    def eventFilter(self, object, event):
        if object == self.moving_label and event.type() == event.Enter:
            self.move_label()
        return super().eventFilter(object, event)
    
    def move_label(self):
        max_x = self.width() - self.moving_label.width()
        max_y = self.height() - self.moving_label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.moving_label.move(new_x, new_y)
    
    def showEvent(self, event):
        self.moving_label.installEventFilter(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracking()
    ex.show()
    sys.exit(app.exec())    