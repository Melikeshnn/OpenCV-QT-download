from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(536, 571)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setText("")
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider.setObjectName("verticalSlider")
		self.horizontalLayout.addWidget(self.verticalSlider)
		self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
		self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
		self.verticalSlider_2.setObjectName("verticalSlider_2")
		self.horizontalLayout.addWidget(self.verticalSlider_2)
		self.horizontalLayout_3.addLayout(self.horizontalLayout)
		self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_2.addWidget(self.pushButton)
		self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
		self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)
		self.pushButton_2.clicked.connect(self.loadImage)
		self.pushButton.clicked.connect(self.savePhoto)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	######### KODLAR BU SATIRDAN SONRA BA??LIYOR #########
	
	
		self.filename = None          # G??rselin yolunu tutar
		self.tmp = None               # G??rseli ge??ici olarak tutar
		self.brightness_value_now = 0 # Parlakl??k de??eri
		self.blur_value_now = 0       # Blur de??eri
	 
	def loadImage(self):
	
		#Bu fonksiyon kullan??c??n??n g??rsel se??mesini sa??lar
		
		self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
		self.image = cv2.imread(self.filename)
		self.setPhoto(self.image)
	
	
	def setPhoto(self,image):
		
		#Bu fonksiyon g??rseli label konumuna yerle??tirir
		
		self.tmp = image
		image = imutils.resize(image,width=640)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
		self.label.setPixmap(QtGui.QPixmap.fromImage(image))
	
	
	def brightness_value(self,value):
		
		#Bu fonksiyon parlakl??k bar??ndaki de??eri al??
		
		self.brightness_value_now = value
		print('Brightness: ',value)
		self.update()
		
		
	def blur_value(self,value):
		
		#Bu fonksiyon blur bar??ndaki de??eri al??r
		
		self.blur_value_now = value
		print('Blur: ',value)
		self.update()
	
	
	def changeBrightness(self,img,value):
		
		# H --> Hue(Renk) 
		# S --> Saturation(Doyum)
		# V --> Value of Brightness (Parlakl??k De??eri)
		
		#Bu fonksiyon g??rselin parlakl??????n?? ayarlar
		
		hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		h,s,v = cv2.split(hsv)
		lim = 255 - value
		v[v>lim] = 255
		v[v<=lim] += value
		final_hsv = cv2.merge((h,s,v))
		img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
		return img
		
	def changeBlur(self,img,value):
		
		#Bu fonksiyon g??rseli blurlar
		
		kernel_size = (value+1,value+1) # +1, 0 olmamas?? i??in
		img = cv2.blur(img,kernel_size)
		return img
	
	def update(self):
		
		#Bu fonksiyon foto??arfataki de??i??iklikleri g??nceller 
		
		img = self.changeBrightness(self.image,self.brightness_value_now)
		img = self.changeBlur(img,self.blur_value_now)
		self.setPhoto(img)
	
	def savePhoto(self):
		
		#Bu fonksiyon g??rselde yap??lan de??i??ikli??i kaydeder.
		
		filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
		
		cv2.imwrite(filename,self.tmp)
		print('Image saved as:',self.filename)
	
	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "KM PHOTO EDITOR"))
		self.pushButton_2.setText(_translate("MainWindow", "Open"))
		self.pushButton.setText(_translate("MainWindow", "Save"))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())




