# pylint: disable=no-name-in-module, import-error
import os
import sys
import cv2
from PyQt5.QtWidgets import QApplication
from app.gui import MainWindow

cv2_path = os.path.dirname(cv2.__file__)
plugin_path = os.path.join(cv2_path, "qt", "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
