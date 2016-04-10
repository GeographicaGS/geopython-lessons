# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2016.
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

import compbuffer

def main():
    in_flname = "../../../data/sampledata/samples.shp"
    out_flname = "/tmp/results/buffsamples.shp"
    find_str = 'ma'
    dist = 500
    field_fltr = 'name'
    find_str = 'ma'

    compbuffer.run(in_flname, out_flname, dist, field_fltr, find_str)

if __name__ == '__main__':
    main()
