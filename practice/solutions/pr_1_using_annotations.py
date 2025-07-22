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
    folder = Path('../../examples')  # In solution folder, so need to go another level up

    all_files: list[Path] = get_files(folder)
    files_w_sizes: list[tuple[Path, int]] = get_file_sizes(all_files)
    largest: list[tuple[Path, int]] = largest_files(files_w_sizes)

    for file, size in largest:
        print(f"{file.name}, {humanbytes(size)}")