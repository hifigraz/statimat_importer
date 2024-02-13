"""Test the input class."""

import logging
import os

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
    assert test_import["FAB_M3"] == "1581.169"
    assert test_import["EAB_M3"] == "21.35958"


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
