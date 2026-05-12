
import sys
import os

print("All arguments", sys.argv)

if len(sys.argv) != 2:
    print("Use: python script.py <dir>")

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Dir '{directory}' does not exist.")
    sys.exit(1)

folders = []
files = []

for item in os.listdir(directory):
    full_path = os.path.join(directory, item)

    if os.path.isdir(full_path):
        folders.append(item)
    elif os.path.isfile(full_path):
        files.append(item)

print(f"directory contents '{directory}':")

print("Folder:")
for folder in folders:
    print(f"- {folder}")

print("File:")
for file in files:
    print(f"- {file}")



from pathlib import Path
print("All arguments", sys.argv)

directory = Path(sys.argv[1])
extension = sys.argv[2]

if len(sys.argv) != 2:
    print(f"Use: python script.py -directory -extension")

if not extension.startswith("."):
    extension = "." + extension

if not os.path.isdir(directory):
    print(f"Dir '{directory}' does not exist.")
    sys.exit(1)

files = []

for item in directory.iterdir():
    if item.is_file() and item.suffix == extension:
        files.append(item)
        print(item)

print("-" * 50)
del_files = input("Delete file? (y/n):")
if del_files == "y":
    for file in files:
        os.remove(file)
    print("Deletion completed.")