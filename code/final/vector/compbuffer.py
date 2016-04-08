

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
