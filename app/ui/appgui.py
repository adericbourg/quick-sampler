from typing import Dict

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

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
        self.keyboard_layout = KeyboardLayout.QWERTY
        self.keyboard_keys: Dict[chr, QPushButton] = dict()

        # Play sound
        vertical_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(vertical_layout)

        open_file_dialog_button = QPushButton("Select sample directory...")
        open_file_dialog_button.clicked.connect(self.open_file)
        vertical_layout.addWidget(open_file_dialog_button)

        for keyboard_line in self.keyboard_layout.keys:
            line_layout = QHBoxLayout()
            for key_cap in keyboard_line:
                key_button = QPushButton(key_cap)
                line_layout.addWidget(key_button)
                self.keyboard_keys[key_cap] = key_button
            vertical_layout.addLayout(line_layout)

        self.setCentralWidget(central_widget)
        self.show()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key_code = event.key()
        try:
            key_char = chr(int(key_code))
            sample = registry.get(key_char)
            print(f"Caught {key_code} ({key_char})")
            if sample is not None:
                print(f"Playing {sample}")
                self.player.play(sample)
        except ValueError:
            pass

    def open_file(self):
        path = QFileDialog.getExistingDirectory(self, "Open samples directory")
        files = fs.list_files(path)
        mappings = registry.register(files, self.keyboard_layout.as_namespace())
        for mapping in mappings:
            if mapping.key in self.keyboard_keys:
                button = self.keyboard_keys[mapping.key]
                button.setText(f"{mapping.key}\n{mapping.file.name}")
