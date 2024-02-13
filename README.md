# Statimat importer

This project implements a simple importer to statimat files. 

Basic usage is as follows:

```
statimat_input [-h] [-v] <input_csv_file> <output_xml_file>

    -h:                print this help and exit
    -v:                optional to increase debugging information.
    <input_csv_file>:  must be a csv file fitting for statimat.
    <output_xml_file>: must be a xml file containing the desired xml group.
```

## Prerequisites

The input file is in the form of a white-space separated table. The two interesting values are:

EAB_M3 and FAB_M3. In both cases the 8th value, if counting starts at zero, is chosen. 

The output file must be an existing XML document. This document is required to have exactly one 
dtGroup tag. On nonexistence of this tag, the program fails, it will not try to add this tag.

If the dtGroup tag already has a EAB_M3 tag or a FAB_M3 tag, the program will also fail.

If everything is as expected, the two tags will be generated as child of dtGroup containing the extracted values.
