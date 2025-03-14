from pathlib import Path
import json
from better_json_tools import load_jsonc
import sys

def print_red(text: str):
    print(f"\033[91m{text}\033[00m")

def main():
    for pattern in ["*.json", "*.material"]:
        for root in ["RP", "BP"]:
            for p in Path(root).rglob(pattern):
                try:
                   data = load_jsonc(p).data
                except:
                    continue
                try:
                    with open(p, "w") as f:
                        json.dump(data, f, separators=(',', ':'))
                except Exception as e:
                    print_red(
                        f"Error: Failed to write to file:\n{p.as_posix()}\n")
                    print_red(f"Cause: {e}\n")
                    sys.exit(1)

if __name__ == "__main__":
    main()
