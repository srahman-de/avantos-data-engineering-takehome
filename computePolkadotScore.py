def computePolkadotScore(ascii_art: str) -> int:
    lines = ascii_art.splitlines()

    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        return 0

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    pupils_row = None
    pupil_count = 0

    for y, row in enumerate(grid):
        if "•" in row:
            pupils_row = y
            pupil_count = row.count("•")
            break

    if pupils_row is None:
        raise ValueError("Could not find pupils")

    lips_row = None
    lips_start = None
    lips_end = None

    for y in range(pupils_row, min(len(grid), pupils_row + 8)):
        row = grid[y]
        xs = [x for x, ch in enumerate(row) if ch not in {" ", '"', "`", ",", "-", "'"}]

        if len(xs) > 5:
            lips_row = y
            lips_start = min(xs)
            lips_end = max(xs)
            break

    if lips_start is None:
        raise ValueError("Could not find lips")

    inside = 0
    outside = 0

    for y in range(lips_row + 1, len(grid)):
        for x, ch in enumerate(grid[y]):
            if ch == "O":
                if lips_start <= x <= lips_end:
                    inside += 1
                else:
                    outside += 1

    return outside + inside * pupil_count


with open("ascii_art.txt", "r", encoding="utf-8") as f:
    ASCII_ART = f.read()

print(computePolkadotScore(ASCII_ART))