

import os
import shutil
import rasterio
from rasterio.warp import calculate_default_transform, reproject, RESAMPLING



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


def run(input_file, out_file, dst_crs):
    try:
        print("Starting proccess...")

        createOutFolder(out_file)

        with rasterio.open(input_file) as src:

            affine, width, height = calculate_default_transform(
                src.crs, dst_crs, src.width, src.height,*src.bounds)
            kwargs = src.meta.copy()
            kwargs.update({
                'crs': dst_crs,
                'transform': affine,
                'affine': affine,
                'width': width,
                'height': height,
                'compress': 'lzw',
                'nodata': 0
            })

            with rasterio.open(out_file, 'w', **kwargs) as dst:

                reproject(
                    source=rasterio.band(src, 1),
                    destination=rasterio.band(dst, 1),
                    src_transform=src.affine,
                    src_crs=src.crs,
                    dst_transform=affine,
                    dst_crs=dst_crs,
                    resampling=RESAMPLING.nearest)

                for i in dst.indexes:
                    band_dst = dst.read(i) / 100
                    dst.write_band(i, band_dst)

        print("Successfully finished proccess!")

    except Exception as error:
        print("Error creating out folder: {}".format(error))

def main():
    input_file = "../../../data/mslp_gfs/mslp_europe.nc"
    out_file = "/tmp/res_raster/mslp_europe_rst.tif"
    dst_crs = 'EPSG:3034'
    run(input_file, out_file, dst_crs)

if __name__ == '__main__':
    main()
