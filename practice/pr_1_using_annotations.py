from __future__ import annotations  # Required to use list[] in <3.9

from pathlib import Path

from helpers import humanbytes


def get_files(directory: Path) -> list[Path]:
    return [f for f in directory.iterdir() if f.is_file()]

def get_file_sizes(files: list[Path]) -> list[tuple[Path, int]]:
    sizes: list[tuple[Path, int]] = []
    for f in files:
        sizes.append((f, f.stat().st_size))
    return sizes

def largest_files(files: list[tuple[Path, int]], num: int | None = None) -> list[tuple[Path, int]]:
    """Return a sorted list of files with the largest ones first.
    If num is provided, only show the largest num files."""
    largest_first: list[tuple[Path, int]] = sorted(files, key=lambda pair: pair[1], reverse=True)
    if num:
        return largest_first[:num]
    return largest_first


if __name__ == "__main__":
    folder = Path('../examples')

    all_files = get_files(folder)
    files_w_sizes = get_file_sizes(all_files)
    largest = largest_files(files_w_sizes)

    print(largest)  # TODO: print files -> filename: humanbytes(size)