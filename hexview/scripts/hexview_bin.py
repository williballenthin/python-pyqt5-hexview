import os
import sys
import stat
import mmap
import contextlib

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication

import hexview


def _main(filename=None, ooffset="0", olength="0"):
    if ooffset.startswith("0x"):
        offset = int(ooffset, 0x10)
    else:
        offset = int(ooffset)

    if olength.startswith("0x"):
        length = int(olength, 0x10)
    else:
        length = int(olength)

    if filename is None:
        b = []
        for i in range(0x100):
            b.append(i)
        buf = bytearray(b)
    else:
        with open(filename, "rb") as f:
            fno = f.fileno()
            size = os.stat(filename)[stat.ST_SIZE]

            if size > 0:
                length = min(size, offset + length)

            with contextlib.closing(mmap.mmap(f.fileno(), 
                                    length, 
                                    offset=offset, 
                                    access=mmap.ACCESS_READ)) as buf:
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
