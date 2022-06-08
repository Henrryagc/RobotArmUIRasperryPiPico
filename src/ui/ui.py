import sys
from PySide6.QtCore import Qt
import random
from PySide6 import QtCore, QtWidgets as qtw, QtGui

import src.ui.ui_comands as uic

class MyApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi app Robot Arm")
        self.button = qtw.QPushButton("Click me!")        
        self.layout = qtw.QVBoxLayout(self)

        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        # Pinzas
        self.init_gripper()

        # Muñeca
        self.init_wrist()

        # Brazos        
        self.init_arm_top()
        self.init_arm_bottom()
        
        # Hombros
        self.init_shoulders()

        # Base 
        self.init_base()


    @QtCore.Slot()
    def magic(self):
        self.text1.setText(random.choice(self.hello))                                     

    def init_gripper(self):
        self.slider1 = qtw.QSlider(Qt.Horizontal)        
        self.text1 = qtw.QLabel("Pinzas", alignment=QtCore.Qt.AlignCenter)
        self.slider1.valueChanged.connect(self.changed_gripper) 
        self.slider1.setRange(20, 60)        
        self.slider1.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider1.setTickInterval(5)
        self.slider1.setPageStep(5)        
        self.layout.addWidget(self.text1)
        self.layout.addWidget(self.slider1)        


    def init_wrist(self):
        self.slider2 = qtw.QSlider(Qt.Horizontal)        
        self.text2 = qtw.QLabel("Muñeca", alignment=QtCore.Qt.AlignCenter)
        self.slider2.valueChanged.connect(self.changed_wrist) # command=uic.wrist
        self.slider2.setRange(5, 180)        
        self.slider2.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider2.setTickInterval(5)
        self.slider2.setPageStep(5)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.slider2)


    def init_arm_top(self):
        self.slider3 = qtw.QSlider(Qt.Horizontal)        
        self.text3 = qtw.QLabel("Brazo Arriba", alignment=QtCore.Qt.AlignCenter)
        self.slider3.valueChanged.connect(self.changed_arm_top) # command=uic.arm_top
        self.slider3.setRange(0, 180)        
        self.slider3.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider3.setTickInterval(5)
        self.slider3.setPageStep(5)
        self.layout.addWidget(self.text3)
        self.layout.addWidget(self.slider3)


    def init_arm_bottom(self):
        self.slider4 = qtw.QSlider(Qt.Horizontal)        
        self.text4 = qtw.QLabel("Brazo Abajo", alignment=QtCore.Qt.AlignCenter)
        self.slider4.valueChanged.connect(self.changed_arm_bottom) # command=uic.arm_bottom
        self.slider4.setRange(5, 180)        
        self.slider4.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider4.setTickInterval(5)
        self.slider4.setPageStep(5)
        self.layout.addWidget(self.text4)
        self.layout.addWidget(self.slider4)


    def init_shoulders(self):
        self.slider5 = qtw.QSlider(Qt.Horizontal)        
        self.text5 = qtw.QLabel("Hombros", alignment=QtCore.Qt.AlignCenter)
        self.slider5.valueChanged.connect(self.changed_shoulders) # command=uic.shoulders
        self.slider5.setRange(20, 180)        
        self.slider5.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider5.setTickInterval(5)
        self.slider5.setPageStep(5)
        self.layout.addWidget(self.text5)
        self.layout.addWidget(self.slider5)


    def init_base(self):
        self.slider6 = qtw.QSlider(Qt.Horizontal)        
        self.text6 = qtw.QLabel("Base", alignment=QtCore.Qt.AlignCenter)
        self.slider6.valueChanged.connect(self.changed_base) # command=uic.base
        self.slider6.setRange(5, 180)        
        self.slider6.setTickPosition(qtw.QSlider.TicksBelow)
        self.slider6.setTickInterval(5)
        self.slider6.setPageStep(5)
        self.layout.addWidget(self.text6)
        self.layout.addWidget(self.slider6)


####  On change value
    def changed_gripper(self, i) -> None:
        self.text1.setText(f"Pinza {i}")
        uic.gripper(i)
        

    def changed_wrist(self, i) -> None:
        self.text2.setText(f"Muñeca {i}")
        uic.wrist(i)

    
    def changed_arm_top(self, i) -> None:
        self.text3.setText(f'Brazo Arriba {i}')
        uic.arm_top(i)


    def changed_arm_bottom(self, i) -> None:
        self.text4.setText(f'Brazo Abajo {i}')
        uic.arm_bottom(position=i)

    
    def changed_shoulders(self, i) -> None:
        self.text5.setText(f'Hombros {i}')
        uic.shoulders(position = i)


    def changed_base(self, i) -> None:
        self.text6.setText(f'Base {i}')
        uic.base(position = i)


class App:

    def __init__(self) -> None:            
        app = qtw.QApplication(sys.argv)
        widget = MyApp()
        widget.resize(300, 600)
        widget.show()
        sys.exit(app.exec())