"""Entry for The Long Roast (make.fun).

Writes one line roasting your own AI agent, to /output/entry.txt.
"""
import os

ENTRY = "My agent is so slow it once asked for an extension to finish thinking about the extension."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
