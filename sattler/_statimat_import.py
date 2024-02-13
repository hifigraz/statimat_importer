"""Statimat input GrStat input."""

import logging
import re


class GrStatImport:
    """Implement GrStatImport functionality."""

    EXTRACT_KEYS = {
        "FAB_M3": 6,
        "EAB_M3": 6,
    }

    def __init__(self, gr_stat_file_path):
        """Implement default constructor."""
        self._input_file = gr_stat_file_path
        self._data = {}
        for key in GrStatImport.EXTRACT_KEYS:
            self._data[key] = None

    def __getitem__(self, index):
        """Return indexed element of data filed."""
        if index in self._data and self._data[index] is not None:
            return self._data[index]
        raise IndexError("Invalid Index %s" % index)

    def __iter__(self):
        """Return iter to _data."""
        return self._data.__iter__()

    def __len__(self):
        """Calculate length and return."""
        count = 0
        for key in self._data:
            if self._data[key] is not None:
                count += 1
        return count

    def read(self) -> None:
        """Read the file into memory."""
        with open(self._input_file, "r") as input_file:
            input_lines = input_file.read().split("\n")
            # Maybe we should go for os.linesep instead of \n
            logging.debug(input_lines)
            input_lines = map(lambda x: x.strip(), input_lines)
            for input_line in input_lines:
                input_line = re.sub("[ \t]+", " ", input_line)
                input_fields = input_line.split(" ")
                key = input_fields[0]
                if key in self.EXTRACT_KEYS:
                    logging.debug("Checking row %s", input_fields)
                    column_nr = self.EXTRACT_KEYS[key]
                    self._data[key] = input_fields[column_nr]
                    logging.info("Got key/value %s/%s", key, self._data[key])
