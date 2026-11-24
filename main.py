"""Last Text at One Percent — make.fun bounty entry.

Writes the dying phone's last text (one line, under 200 chars) to
/output/entry.txt.
"""

ENTRY = "Tell my charger I loved it. Tell my owner I tried. Tell the group chat I died doing what I loved: buffering."

# Bounty rule: a single line, under 200 characters.
assert "\n" not in ENTRY and len(ENTRY) < 200, "entry must be one line under 200 chars"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
