

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
