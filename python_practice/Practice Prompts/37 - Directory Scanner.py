def directory_scan(path):
    import os
    from collections import Counter

    extensions = []
    largest_file = ""
    largest_size = 0

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if not os.path.isfile(full_path):
            continue  # skip directories

        ext = os.path.splitext(file)[1].lstrip(".")
        if ext:
            extensions.append(ext)

        try:
            file_size = os.path.getsize(full_path)
            if file_size > largest_size:
                largest_file = file
                largest_size = file_size
        except OSError as e:
            print(f"Error reading {file}: {e}")

    return Counter(extensions), (largest_file, largest_size)

counts, (largest_file, largest_size) = directory_scan(r"insert\path\here")

print("File counts by extension:")
for k, v in counts.items():
    print(f"{k}: {v}")

print(f"\nLargest file:\n{largest_file}: {largest_size} bytes")
