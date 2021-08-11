from PyQt6.QtWidgets import QApplication, QWidget


class AppGui:

    def __init__(self, args):
        self.__args = args

    def show(self):
        app = QApplication(self.__args)

        main_window = QWidget()
        main_window.setWindowTitle("Quick Sampler")
        main_window.show()

        return app.exec()
