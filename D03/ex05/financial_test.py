import pytest
from bs4 import BeautifulSoup
import requests
import os
import sys

# путь до ex03
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ex03")))
from financial import find_row_values

HTML = """
<div class="tableContainer">
  <div class="row">
    <div class="rowTitle">Total Revenue</div>
    <div class="column">1000</div>
    <div class="column alt">2000</div>
  </div>
</div>
"""

def test_find_row_values_returns_tuple():
    soup = BeautifulSoup(HTML, "html.parser")
    result = find_row_values(soup, "Total Revenue")
    assert isinstance(result, tuple)

def test_find_row_values_correct_values():
    soup = BeautifulSoup(HTML, "html.parser")
    result = find_row_values(soup, "Total Revenue")
    assert result[0] == "Total Revenue"
    assert "1000" in result
    assert "2000" in result

def test_find_row_values_raises_exception():
    soup = BeautifulSoup(HTML, "html.parser")
    with pytest.raises(Exception):
        find_row_values(soup, "Fake Field")
