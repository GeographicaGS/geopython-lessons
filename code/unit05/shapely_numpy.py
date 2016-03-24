# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2016.
#  cayetano.benavent@geographica.gs
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#



import shapely.wkt
import numpy as np


def main():
    wkt_ln = "LINESTRING(178044.505034367 4080523.32981373,185051.202770193 4115968.97717771,218436.056686834 4125036.46836944,231625.134776712 4158833.48097265,229564.341325156 4174495.51120244,216787.42192546 4189333.22405021,212253.676331916 4213238.42808471,216787.421925395 4231373.41045699)"

    ln = shapely.wkt.loads(wkt_ln)

    ln_np = np.array(ln)

    print(ln_np.shape)
    print(ln_np)

    ln_buf = ln.buffer(20000)

    print(ln_buf.wkt)


if __name__ == '__main__':
    main()
