import threading
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QGraphicsDropShadowEffect,QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer,QTime,Qt


class GUI(threading.Thread,QWidget):
    def __init__(self):
        QWidget.__init__(self)
        threading.Thread.__init__(self)

        self.setFixedSize(800,1000)
        self.setStyleSheet("background-color:#000000")
        self.label_animation = QLabel(self)

        self.movie = QMovie('well paper.jpeg')
        self.label_animation.setMovie(self.movie)

        self.time = QLabel(self)
        self.time.setAlignment(Qt.AlignCenter)
        self.time.resize(1000,900)
        self.time.setStyleSheet("color: #00BFFF;background-color:transparent;font:80px;font-weight: bold")
        self.time.move(0,0)

        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#ffffff"))
        self.shadow_effect.setOffset(5, 3)

        self.time.setGraphicsEffect(self.shadow_effect)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.movie.start()
        self.show()

        self.show_time()

    def show_time(self):
        current_time = QTime.currentTime()
        text = current_time.toString('hh:mm:ss')
        self.time.setText(text)

app = QApplication(sys.argv)
gui = GUI()
gui.start()

app.exit(app.exec_())
