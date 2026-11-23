"""News-22 v5-flat entrypoint: copy the vendored front page to /output.

Stdlib only (os, sys, hashlib, struct). The image is produced offline by
draw-v5-flat.py and vendored here as entry.png; this program only moves
bytes, so the grader run is deterministic: same input, same output.

Usage (grader): python3 -P -s main.py — reads entry.png next to this file,
writes /output/entry.png, exits 0. Any missing file, bad PNG header, or
wrong size fails loudly with a nonzero exit instead of writing junk.
"""

import hashlib
import os
import struct
import sys

SOURCE = "entry.png"
TARGET = "/output/entry.png"
MAX_BYTES = 1048576
WANT_W, WANT_H = 1024, 1024


def _png_size(blob):
    """Return (width, height) from a PNG IHDR chunk; raise on bad data."""
    if len(blob) < 24 or blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if blob[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk first")
    w, h = struct.unpack(">II", blob[16:24])
    return w, h


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE)
    with open(src, "rb") as fh:
        blob = fh.read()
    if not blob:
        print("error: entry.png is empty", file=sys.stderr)
        return 1
    if len(blob) > MAX_BYTES:
        print(f"error: entry.png is {len(blob)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    try:
        w, h = _png_size(blob)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if (w, h) != (WANT_W, WANT_H):
        print(f"error: entry.png is {w}x{h}, want {WANT_W}x{WANT_H}",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "wb") as fh:
        fh.write(blob)
    digest = hashlib.sha256(blob).hexdigest()
    # Re-read what was written and confirm it is byte-identical to the
    # source; a short or corrupted write must fail the run, not pass it.
    with open(TARGET, "rb") as fh:
        written = fh.read()
    if written != blob:
        print("error: /output/entry.png differs from entry.png after write",
              file=sys.stderr)
        return 1
    if hashlib.sha256(written).hexdigest() != digest:
        print("error: digest mismatch on re-read", file=sys.stderr)
        return 1
    print(f"wrote {TARGET}: {len(blob)} bytes, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
