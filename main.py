import os
import shutil
import sys

MAX_BYTES = 1_048_576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        sys.exit(
            f"entry.png is {size} bytes, over the {MAX_BYTES} byte limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dest)
    print(f"wrote {dest} ({size} bytes)")


if __name__ == "__main__":
    main()
