"""Export the statimat data to an xml."""

import logging
import xml.etree.ElementTree as ET

from ._statimat_import import GrStatImport

# <dataSetGroup>
#   <dtGroup>


class GrStatExport:
    """Export formerly imported data to xml."""

    ADD_TO_TAG = "dtGroup"

    def __init__(self, gr_stat: GrStatImport, xml_file: str):
        """Implement the default constructor."""
        self._import = gr_stat
        self._export_path = xml_file

    def update(self):
        """Update the given file, with all found values."""
        tree = ET.parse(self._export_path)
        root = tree.getroot()

        dt_group = root.find(GrStatExport.ADD_TO_TAG)
        if type(dt_group) is ET.Element:

            for key in self._import:
                logging.debug("looking for key %s in %s", key, dt_group)
                logging.debug(dt_group.find(key))
                if type(dt_group.find(key)) is ET.Element:
                    logging.error(
                        "%s already present in %s",
                        key,
                        GrStatExport.ADD_TO_TAG,
                    )
                    raise ValueError(
                        "%s already present in %s"
                        % (key, GrStatExport.ADD_TO_TAG)
                    )
                new_element = ET.Element(key)
                new_element.text = self._import[key]
                dt_group.append(new_element)
            ET.indent(tree, space="  ", level=0)
            tree.write(self._export_path)
        else:
            error_message = "%s is lacking a %s field" % (
                self._export_path,
                GrStatExport.ADD_TO_TAG,
            )
            logging.error(error_message)
            raise ValueError(error_message)
