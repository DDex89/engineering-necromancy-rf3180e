#!/usr/bin/env python3
"""Read-only binary image comparison.

Reports changed bytes and flipped bits. This utility does not repair anything,
parse proprietary images, access devices or produce an output binary.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def compare_files(left: Path, right: Path, chunk_size: int = 1024 * 1024) -> dict:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    left_size = left.stat().st_size
    right_size = right.stat().st_size
    a_hash = hashlib.sha256()
    b_hash = hashlib.sha256()
    different_bytes = 0
    flipped_bits = 0
    compared_bytes = 0
    with left.open('rb') as a, right.open('rb') as b:
        while True:
            x = a.read(chunk_size)
            y = b.read(chunk_size)
            if not x and not y:
                break
            a_hash.update(x)
            b_hash.update(y)
            for u, v in zip(x, y):
                different_bytes += (u != v)
                flipped_bits += (u ^ v).bit_count()
            compared_bytes += min(len(x), len(y))
    return {
        "left_size": left_size,
        "right_size": right_size,
        "compared_bytes": compared_bytes,
        "different_bytes": different_bytes,
        "flipped_bits": flipped_bits,
        "unpaired_bytes": abs(left_size - right_size),
        "left_sha256": a_hash.hexdigest(),
        "right_sha256": b_hash.hexdigest(),
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('baseline', type=Path)
    p.add_argument('candidate', type=Path)
    args = p.parse_args()
    data = compare_files(args.baseline, args.candidate)
    print(f"Baseline size: {data['left_size']:,} bytes")
    print(f"Candidate size: {data['right_size']:,} bytes")
    print(f"Compared: {data['compared_bytes']:,}")
    print(f"Different bytes: {data['different_bytes']:,}")
    print(f"Changed bits: {data['flipped_bits']:,}")
    print(f"Unpaired trailing bytes: {data['unpaired_bytes']:,}")
    print(f"Baseline SHA256: {data['left_sha256']}")
    print(f"Candidate SHA256: {data['right_sha256']}")
    if data['unpaired_bytes']:
        print("Note: the changed-bit count excludes unpaired trailing bytes.")


if __name__ == '__main__':
    main()
