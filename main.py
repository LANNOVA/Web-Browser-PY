import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTabWidget, QTabBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SRAVstudios Web Browser")

        self.tab_widget.setCornerWidget(self.create_new_tab_button())

        self.add_new_tab()

        self.show()

    def create_new_tab_button(self):
        new_tab_button = QPushButton("+")
        new_tab_button.clicked.connect(self.add_new_tab)
        return new_tab_button

    def add_new_tab(self):
        new_tab = QWidget()
        layout = QVBoxLayout()

        url_input = QLineEdit()
        url_input.returnPressed.connect(lambda: self.load_url(url_input))
        
        go_button = QPushButton("Search")
        go_button.clicked.connect(lambda: self.load_url(url_input))

        browser = QWebEngineView()
        browser.setMinimumSize(800, 600)

        layout.addWidget(url_input)
        layout.addWidget(go_button)
        layout.addWidget(browser)

        new_tab.setLayout(layout)
        self.tab_widget.addTab(new_tab, "New Tab")
        self.tab_widget.setCurrentWidget(new_tab)

    def load_url(self, url_input):
        url = url_input.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        current_tab = self.tab_widget.currentWidget()
        browser = current_tab.layout().itemAt(2).widget()
        browser.setUrl(QUrl(url))

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    sys.exit(app.exec_())
