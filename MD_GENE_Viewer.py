import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from guess_language import guess_language

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1400, 800)
        self.setWindowTitle("一个属于你的简单基因信息查询软件")
        #self.resize(800,500)

        self.tabs = QtWidgets.QTabWidget()

        self.webtab01 = QWebView()
        self.webtab01.setObjectName("GeneCard")
        self.webtab01.load(QtCore.QUrl("https://www.genecards.org/"))

        self.webtab02 = QWebView()
        self.webtab02.setObjectName("Web-Wiki")
        self.webtab02.load(QtCore.QUrl("https://en.wikipedia.org/wiki/"))

        self.webtab03 = QWebView()
        self.webtab03.setObjectName("ncbi")
        self.webtab03.load(QtCore.QUrl("https://www.ncbi.nlm.nih.gov/gene/"))

        self.webtab04 = QWebView()
        self.webtab04.setObjectName("COSMIC")
        self.webtab04.load(QtCore.QUrl("https://cancer.sanger.ac.uk/cosmic/"))

        self.webtab05 = QWebView()
        self.webtab05.setObjectName("Human Protein Altas")
        self.webtab05.load(QtCore.QUrl("https://www.proteinatlas.org/"))
#
        self.webtab06 = QWebView()
        self.webtab06.setObjectName("Genetics Home Ref")
        self.webtab06.load(QtCore.QUrl("https://ghr.nlm.nih.gov/gene/"))
#
        self.webtab07 = QWebView()
        self.webtab07.setObjectName("OMIM")
        self.webtab07.load(QtCore.QUrl("https://omim.org/"))
#
        #self.webtab12 = QWebView()
        #self.webtab12.setObjectName("Web-谷歌")
        #self.webtab12.load(QtCore.QUrl("https://translate.google.cn/"))
#
        #self.webtab13 = QWebView()
        #self.webtab13.setObjectName("Web-百度")
        #self.webtab13.load(QtCore.QUrl("http://fanyi.baidu.com/"))
#
        #self.webtab15 = QWebView()
        #self.webtab15.setObjectName("Web-OzDict")
        #self.webtab15.load(QtCore.QUrl("https://www.onelook.com/"))

        self.tabs.addTab(self.webtab02, "WIKI")
        self.tabs.addTab(self.webtab06, "GeneticsHome")
        self.tabs.addTab(self.webtab03, "NCBI")
        self.tabs.addTab(self.webtab01, "GeneCard")
        self.tabs.addTab(self.webtab04, "COSMIC")
        self.tabs.addTab(self.webtab05, "HPA")
        self.tabs.addTab(self.webtab07, "OMIM")
        #self.tabs.addTab(self.webtab14, "维基百科")
        #self.tabs.addTab(self.webtab05, "UrbanDict")
        #self.tabs.addTab(self.webtab06, "Webster")
        #self.tabs.addTab(self.webtab15, "OneLook")

        self.inputLine = QtWidgets.QLineEdit()
        self.inputLine.setObjectName("inputLineEditor")
        self.inputLine.setFixedHeight(30)
        self.inputLine.textChanged.connect(self.translateText)

        self.outputLine = QtWidgets.QLineEdit()
        self.outputLine.setObjectName("outputLineEditor")
        self.outputLine.setFixedHeight(20)
        self.webtab01.loadStarted.connect(self.initURL)
        #self.outputLine.setText(self.webtab01.url().toString()) 还不太会搞这个的初始化
        self.tabs.currentChanged.connect(self.getURL)
        #self.outputLine..connect(self.getURL)

        centralLayout = QtWidgets.QVBoxLayout()
        centralLayout.addWidget(self.inputLine, 1)
        centralLayout.addWidget(self.outputLine, 2)
        centralLayout.addWidget(self.tabs, 3)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralWidget)

    def getURL(self):
        self.outputLine.setText(self.tabs.currentWidget().url().toString())
        #print(self.tabs.currentIndex())

    def initURL(self):
        self.outputLine.setText(self.webtab01.url().toString())

    def translateText(self):
        word = self.inputLine.text()
        #print(word)
        self.webtab01.load(QtCore.QUrl("https://www.genecards.org/Search/Keyword?queryString=" + word))
        #self.webtab01.load(QtCore.QUrl("http://www.iciba.com/" + word))
        self.webtab02.load(QtCore.QUrl("https://en.wikipedia.org/wiki/" + word))
        self.webtab03.load(QtCore.QUrl("https://www.ncbi.nlm.nih.gov/gene/?term=" + word))
        self.webtab04.load(QtCore.QUrl("https://cancer.sanger.ac.uk/cosmic/search?q=" + word))
        self.webtab05.load(QtCore.QUrl("https://www.proteinatlas.org/search/" + word))
        self.webtab06.load(QtCore.QUrl("https://ghr.nlm.nih.gov/gene/" + word))
        self.webtab07.load(QtCore.QUrl("https://omim.org/search/?index=entry&sort=score+desc%2C+prefix_sort+desc&start=1&limit=10&search=" + word))
        #self.webtab08.load(QtCore.QUrl("https://www.merriam-webster.com/dictionary/" + word))
        #self.webtab09.load(QtCore.QUrl("https://en.wikipedia.org/wiki/" + word))
        #self.webtab10.load(QtCore.QUrl("https://www.onelook.com/?w=" + word))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()