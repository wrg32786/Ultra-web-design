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
EXPECTED_PARTS = 7
EXPECTED_SHA256 = "28275957770f4aa3f3e360d3b401d099b35e6557b14e8a3d2e745b48adf8529e"


def main() -> None:
    parts = sorted(BOOTSTRAP.glob("part-*.txt"))
    if len(parts) != EXPECTED_PARTS:
        raise SystemExit(f"Expected {EXPECTED_PARTS} payload parts, found {len(parts)}")

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
    (ROOT / ".github" / "workflows" / "bootstrap.yml").unlink(missing_ok=True)

    print("Bootstrapped Ultra Web Design repository")


if __name__ == "__main__":
    main()
