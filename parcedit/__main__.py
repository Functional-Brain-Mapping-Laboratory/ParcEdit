from importlib import import_module
import sys

from PyQt5.QtWidgets import QApplication

from .gui import LabelsDialog


if __name__ == '__main__':
    modern = False
    try:
        import_module('qtmodern')
        modern = True
    except ModuleNotFoundError as e:
        pass
    app = QApplication(sys.argv)
    if modern is True:
        import qtmodern.styles
        qtmodern.styles.dark(app)
    LabelsDialog = LabelsDialog(QApplication=app)
    LabelsDialog.show()
    sys.exit(app.exec_())
