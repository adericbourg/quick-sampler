from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget

from app.core import player, fs
from app.core import registry, KeyboardLayout


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

        self.player = player.Player()

        # Play sound
        vertical_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(vertical_layout)

        open_file_dialog_button = QPushButton("Select file...")
        open_file_dialog_button.clicked.connect(self.open_file)
        vertical_layout.addWidget(open_file_dialog_button)

        play_button = QPushButton("Play!")
        play_button.clicked.connect(self.play)
        vertical_layout.addWidget(play_button)

        self.setCentralWidget(central_widget)
        self.show()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        sample = registry.get(event.key())
        print(f"Caught {event.key()}")
        if sample is not None:
            print(f"Playing {sample}")
            self.player.play(sample)

    def open_file(self):
        path = QFileDialog.getExistingDirectory(self, "Open samples directory")
        files = fs.list_files(path)
        registry.register(files, KeyboardLayout.QWERTY.as_namespace())

    def play(self):
        file = self.file_name.toPlainText()
        self.player.play(file)
