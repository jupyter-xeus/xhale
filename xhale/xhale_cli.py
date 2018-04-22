############################################################################
# Copyright (c) 2018, Johan Mabille, Sylvain Corlay and Loic Gouarin       #
#                                                                          #
# Distributed under the terms of the BSD 3-Clause License.                 #
#                                                                          #
# The full license is in the file LICENSE, distributed with this software. #
############################################################################
import argparse
import xhale

def main():
    parser = argparse.ArgumentParser(description="xhale command line")
    parser.add_argument('-p', '--package', type=str,
                        help="the package name",
                        required=True)
    parser.add_argument('--url', type=str,
                        help="url where to find the object.inv file given by sphinx",
                        required=True)
    args = parser.parse_args()

    url = args.url
    package = args.package
    inventory = xhale.get_sphinx_inventory(url)
    tag_elem = xhale.extract_tag(inventory, url)
    xhale.write_tagfile(tag_elem, package, url)
