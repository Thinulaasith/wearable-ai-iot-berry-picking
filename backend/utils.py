from pathlib import Path
import sys
import logging


BACKEND_ROOT   = Path(__file__).resolve().parent           
PROJECT_ROOT   = BACKEND_ROOT.parent                  
CLASSIFIER_DIR = PROJECT_ROOT / "classifier"             


if sys.platform == "win32":
    VENV_PY = CLASSIFIER_DIR / ".venv" / "Scripts" / "python.exe"   
else:
    VENV_PY = CLASSIFIER_DIR / ".venv" / "bin" / "python"

CLASSIFIER_SCRIPT = CLASSIFIER_DIR / "classifier2.py"

assert Path(VENV_PY).exists(),      f"[utils] {VENV_PY} not found"
assert Path(CLASSIFIER_SCRIPT).exists(), f"[utils] {CLASSIFIER_SCRIPT} not found"
logging.info("[utils] paths OK")