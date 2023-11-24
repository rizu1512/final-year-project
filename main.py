from import_sys import *
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LungDiseaseClassifier()
    window.show()
    sys.exit(app.exec_())
