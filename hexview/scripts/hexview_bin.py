import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication

import hexview


def _main(filename=None):
    import sys

    if filename is None:
        b = []
        for i in range(0x100):
            b.append(i)
        buf = bytearray(b)
    else:
        with open(filename, "rb") as f:
            buf = f.read()

    app = QApplication(sys.argv)
    w = PyQt5.QtWidgets.QFrame()
    screen = hexview.HexViewWidget(buf, w)
    screen.show()
    sys.exit(app.exec_())


def main():
   import sys
   sys.exit(_main(*sys.argv[1:]))
 
if __name__ == "__main__":
    main()
