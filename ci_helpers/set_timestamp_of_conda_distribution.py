#!/usr/bin/env python
import argparse
import tarfile


def set_mtime(input_fname, output_fname, mtime=0):
    with tarfile.open(input_fname) as tf:
        with tarfile.open(output_fname, 'w:bz2') as new_tf:
            for file_info in tf.getmembers():
                file_info.mtime = 0
                new_tf.addfile(file_info)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reset the mtime of files within a tarfile.')
    parser.add_argument('input_fname',
                       help='the tarfile to modify')
    parser.add_argument('output_fname',
                       help='the tarfile to create')
    args = parser.parse_args()
    set_mtime(args.input_fname, args.output_fname)

