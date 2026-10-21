import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from python_lab.utils import clean_text


def test_clean_text():
    assert clean_text("   hello   world   ") == "hello world"
