import os
import shutil

def create_ver1():
    src_base = r"d:\BI304"
    dest_base = r"d:\BI304\ver1"

    if os.path.exists(dest_base):
        print(f"Cleaning existing directory {dest_base}")
        shutil.rmtree(dest_base)

    os.makedirs(dest_base, exist_ok=True)
    print(f"Created {dest_base}")

    # Copy files
    files_to_copy = [
        "index.html",
        "package.json",
        "package-lock.json",
        "README.md",
        "START_HERE.bat",
        "RUN_WEB.bat",
        ".gitignore"
    ]

    for fname in files_to_copy:
        src = os.path.join(src_base, fname)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dest_base, fname))
            print(f"Copied file: {fname}")

    # Copy directories
    dirs_to_copy = [
        "assets",
        "data"
    ]

    for dname in dirs_to_copy:
        src = os.path.join(src_base, dname)
        dst = os.path.join(dest_base, dname)
        if os.path.exists(src):
            shutil.copytree(src, dst)
            print(f"Copied directory: {dname}")

    # Verify contents
    all_items = os.listdir(dest_base)
    print(f"Total items in ver1: {len(all_items)}")
    for item in sorted(all_items):
        item_path = os.path.join(dest_base, item)
        if os.path.isdir(item_path):
            count = len(os.listdir(item_path))
            print(f"  [DIR]  {item} ({count} items)")
        else:
            size = os.path.getsize(item_path)
            print(f"  [FILE] {item} ({size:,} bytes)")

if __name__ == '__main__':
    create_ver1()
