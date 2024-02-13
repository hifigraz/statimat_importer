"""Test the input class."""

import logging
import os
import tempfile

import pytest

import sattler


def test_import() -> None:
    """Test input."""
    assert True
    assert sattler
    assert sattler.GrStatImport
    path = os.path.abspath(__file__)
    test_file_path = os.path.join(
        os.path.dirname(path), "..", "docs", "GrStat.all"
    )
    logging.error(path)
    test_import = sattler.GrStatImport(test_file_path)

    test_import.read()

    for key in test_import:
        assert key in ["FAB_M3", "EAB_M3"]
    assert len(test_import) == 2
    assert test_import["FAB_M3"] == "5.551117"
    assert test_import["EAB_M3"] == "4.536075"


def test_export() -> None:
    """Test export."""
    path = os.path.abspath(__file__)
    test_file_path = os.path.join(
        os.path.dirname(path), "..", "docs", "GrStat.all"
    )
    logging.error(path)
    test_import = sattler.GrStatImport(test_file_path)
    test_import.read()

    test_file_path = os.path.join(
        os.path.dirname(path), "..", "docs", "6632.xml"
    )

    temp_file_path = os.path.join(os.path.dirname(path), "test.xml")

    with open(test_file_path, "r") as in_file:
        with open(temp_file_path, "w") as out_file:
            out_file.write(in_file.read())

    output_write = sattler.GrStatExport(test_import, temp_file_path)

    output_write.update()


def test_failing_export_1() -> None:
    """Test invalid export files."""
    test_path = os.path.dirname(os.path.abspath(__file__))
    test_file_no_dtgroup = os.path.join(test_path, "out_xml_no_dtGroup.xml")
    logging.debug("Testfile is located in %s", test_path)
    test_file_path = os.path.join(
        os.path.dirname(test_path), "docs", "GrStat.all"
    )

    test_file = tempfile.mktemp()

    with open(test_file_no_dtgroup, "r") as in_file:
        with open(test_file, "w") as out_file:
            out_file.write(in_file.read())

    test_importer = sattler.GrStatImport(test_file_path)
    test_importer.read()
    test_exporter = sattler.GrStatExport(test_importer, test_file)
    with pytest.raises(ValueError, match=" is lacking a dtGroup field"):
        test_exporter.update()
    logging.debug("Wrote output to %s", test_file)


def test_failing_export_2() -> None:
    """Test invalid export files."""
    test_path = os.path.dirname(os.path.abspath(__file__))
    test_file_no_dtgroup = os.path.join(test_path, "out_xml_tag_exists.xml")
    logging.debug("Testfile is located in %s", test_path)
    test_file_path = os.path.join(
        os.path.dirname(test_path), "docs", "GrStat.all"
    )

    test_file = tempfile.mktemp()

    with open(test_file_no_dtgroup, "r") as in_file:
        with open(test_file, "w") as out_file:
            out_file.write(in_file.read())

    logging.debug("Wrote temp file to %s", test_file)

    test_importer = sattler.GrStatImport(test_file_path)
    test_importer.read()
    test_exporter = sattler.GrStatExport(test_importer, test_file)
    with pytest.raises(ValueError, match="FAB_M3 already present in dtGroup"):
        test_exporter.update()
    logging.debug("Wrote output to %s", test_file)
