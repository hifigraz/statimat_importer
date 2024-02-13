"""Main methods in this file."""

import logging
import os
from sys import argv

import sattler

USAGE_TEXT = """%s [-h] [-v] <input_csv_file> <output_xml_file>

    -h:                print this help and exit
    -v:                optional to increase debugging information.
    <input_csv_file>:  must be a csv file fitting for statimat.
    <output_xml_file>: must be a xml file containing the desired xml group."""


def main():
    """Run the main method of the command line tool."""

    input_file: str | None = None
    output_file: str | None = None

    def _usage():
        print(USAGE_TEXT % os.path.basename(argv[0]))

    def _parse():
        nonlocal input_file
        nonlocal output_file
        for arg in argv[1:]:
            if arg == "-h":
                _usage()
                exit(0)
            if arg == "-v":
                logging.getLogger().setLevel(logging.DEBUG)
                logging.debug("Debugging enabled")
            elif input_file is None:
                input_file = arg
            elif output_file is None:
                output_file = arg
            else:
                logging.error("Too much parameters!")
                _usage()
                exit(1)
        if output_file is None:
            logging.error("Too view parameters!")
            _usage()
            exit(2)

    _parse()

    assert input_file
    assert output_file

    if not os.path.exists(input_file):
        logging.error("%s does not exist.", input_file)
        exit(3)
    if not os.path.exists(output_file):
        logging.error("%s does not exist.", output_file)
        exit(4)

    importer: sattler.GrStatImport = sattler.GrStatImport(input_file)
    try:
        importer.read()
    except Exception as e:
        logging.error("Exception during read %s", e)
        exit(5)

    exporter = sattler.GrStatExport(importer, output_file)
    try:
        exporter.update()
    except Exception as e:
        logging.error("Exception durring write %s", e)
        exit(6)
