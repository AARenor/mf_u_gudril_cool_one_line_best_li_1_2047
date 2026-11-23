#!/usr/bin/env python3
"""Write the one-line entry for make.fun bounty u-gudril-cool-one-line-best-line-b8c41f4d."""

import os
import sys
from pathlib import Path

TEXT = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."

assert 1 <= len(TEXT) <= 280

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
output_path = Path(output_dir)
output_path.mkdir(parents=True, exist_ok=True)
(output_path / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
