from PyQt4.Qt import *

if __name__ == "__main__":
	app = QApplication([])

	label = QLabel("Hello World!")
	label.show()

	app.exec_()

