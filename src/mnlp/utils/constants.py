from pathlib import Path

_utils_dir = Path(__file__).parent
_src_dir = _utils_dir.parent.parent
REPO_ROOT = _src_dir.parent
DATA_DIR = REPO_ROOT / "data"
LOG_DIR = REPO_ROOT / "logs"
