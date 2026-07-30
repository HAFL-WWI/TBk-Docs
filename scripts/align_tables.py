# -*- coding: utf-8 -*-
import re
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

out = []
i = 0
n = len(lines)
while i < n:
    line = lines[i]
    stripped = line.rstrip("\n")
    if stripped.lstrip().startswith("|") and stripped.rstrip().endswith("|"):
        block = []
        j = i
        while j < n:
            s = lines[j].rstrip("\n")
            if s.lstrip().startswith("|") and s.rstrip().endswith("|"):
                block.append(s)
                j += 1
            else:
                break
        # parse cells
        rows = []
        sep_idx = None
        for idx, row in enumerate(block):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            rows.append(cells)
            if idx == 1 and all(re.fullmatch(r":?-+:?", c) for c in cells):
                sep_idx = idx
        ncols = max(len(r) for r in rows)
        MAX_COL_WIDTH = 80  # cap padding for huge free-text cells - avoids absurd 300+ char separator lines
        widths = [0] * ncols
        for idx, cells in enumerate(rows):
            if idx == sep_idx:
                continue
            for c_i, c in enumerate(cells):
                widths[c_i] = max(widths[c_i], len(c))
        widths = [max(min(w, MAX_COL_WIDTH), 3) for w in widths]

        new_block = []
        for idx, cells in enumerate(rows):
            if idx == sep_idx:
                parts = []
                for c_i in range(ncols):
                    parts.append("-" * widths[c_i])
                new_block.append("| " + " | ".join(parts) + " |")
            else:
                parts = []
                for c_i in range(ncols):
                    val = cells[c_i] if c_i < len(cells) else ""
                    parts.append(val.ljust(widths[c_i]))  # no-op padding if val already longer than width
                new_block.append("| " + " | ".join(parts) + " |")
        out.extend(nb + "\n" for nb in new_block)
        i = j
    else:
        out.append(line)
        i += 1

with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.writelines(out)

print("done")
