from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QTextEdit, QVBoxLayout, QWidget

from app.core import player


class AppGui:

    def __init__(self, args) -> None:
        super().__init__()
        self.__args = args

    def run(self):
        app = QApplication(self.__args)

        main_window = MainWindow()
        main_window.show()

        return app.exec()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Play sound
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)

        file_name = QTextEdit()
        self.file_name = file_name
        layout.addWidget(file_name)

        open_file_dialog_button = QPushButton("Select file...")
        open_file_dialog_button.clicked.connect(self.open_file)
        layout.addWidget(open_file_dialog_button)

        play_button = QPushButton("Play!")
        play_button.clicked.connect(self.play)
        layout.addWidget(play_button)

        self.setCentralWidget(central_widget)
        self.show()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open file')
        self.file_name.setText(path)

    def play(self):
        file = self.file_name.toPlainText()
        player.Player().play(file)
