#!/usr/bin/env python3
"""One-time reconstruction of the Ultra Web Design source package."""

from __future__ import annotations

import base64
import hashlib
import shutil
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / ".bootstrap"
ARCHIVE = BOOTSTRAP / "repo.tar.gz"
PART_NAMES = (
    "part-00-a.txt",
    "part-00-b.txt",
    "part-00-c.txt",
    "part-01.txt",
    "part-02.txt",
    "part-03.txt",
    "part-04.txt",
    "part-05.txt",
    "part-06.txt",
)
EXPECTED_SHA256 = "28275957770f4aa3f3e360d3b401d099b35e6557b14e8a3d2e745b48adf8529e"


def main() -> None:
    parts = [BOOTSTRAP / name for name in PART_NAMES]
    missing = [path.name for path in parts if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing payload parts: {', '.join(missing)}")

    encoded = "".join(
        "".join(path.read_text(encoding="utf-8").split()) for path in parts
    )
    archive_bytes = base64.b64decode(encoded, validate=True)
    digest = hashlib.sha256(archive_bytes).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Payload checksum mismatch: {digest}")

    ARCHIVE.write_bytes(archive_bytes)

    with tarfile.open(ARCHIVE, "r:gz") as archive:
        for member in archive.getmembers():
            target = (ROOT / member.name).resolve()
            if target != ROOT and ROOT not in target.parents:
                raise SystemExit(f"Unsafe archive path: {member.name}")
        archive.extractall(ROOT, filter="data")

    shutil.rmtree(BOOTSTRAP)
    Path(__file__).unlink()

    print("Bootstrapped Ultra Web Design repository")


if __name__ == "__main__":
    main()
