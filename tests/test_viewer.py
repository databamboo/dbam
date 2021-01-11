"""Tests for the dbam.viewer module"""

# Third party imports
import pytest
from dbam import viewer


#
# Tests
#
def test_show(capsys):
    """Test that show adds information to stdout"""
    text = "Lorem ipsum dolor sit amet"
    viewer.show(text)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""

    # It's ok if the viewer adds some information
    assert text in stdout