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

import os
import shutil
import fiona
from shapely.geometry import shape, mapping


def createOutFolder(out_flname):
    try:
        outdir = os.path.dirname(out_flname)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        else:
            shutil.rmtree(outdir)
            os.makedirs(outdir)

        print("Output folder created")

    except Exception as error:
        print("Error creating out folder: {}".format(error))

def run(in_flname, out_flname, dist, fld, fltr):
    try:
        print("Starting proccess...")

        createOutFolder(out_flname)

        with fiona.open(in_flname, 'r') as in_ds:
            in_drv = in_ds.driver
            in_crs = in_ds.crs
            in_sch = in_ds.schema

            out_schema = {'geometry': 'Polygon',
                          'properties': in_sch.get('properties')}

            with fiona.open(out_flname, 'w',
                        driver=in_drv,
                        crs=in_crs,
                        schema=out_schema) as out_ds:
                for ft in in_ds:
                    if fltr in ft['properties'].get(fld):
                        geom_shl = shape(ft.get('geometry')).buffer(dist)
                        out_ds.write({'geometry': mapping(geom_shl),
                                      'properties': ft.get('properties'),
                                      'type': ft.get('type'),
                                      'id': ft.get('id')})

        print("Buffer successfully created!")

    except Exception as error:
        print("Error computing Buffer: {}".format(error))
