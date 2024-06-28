# pylint: disable=no-name-in-module, import-error
import os
import sys
from PyQt5.QtWidgets import QApplication  # Import de terceiros deve vir antes dos imports locais
from app.gui import MainWindow

# Trocar o path para o diretório onde estão os plugins do Qt
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "/home/thehprogrammer/Documentos/Creche/up_to_date/Semester_08/IA2/forca_em_sinais/.venv/lib/python3.12/site-packages/cv2/qt/plugins"

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
