import os

start_file_num = 950
total_files = 50

deleted_count = 0

for i in range(total_files):
    file_num = start_file_num + i
    filename = f"catalog-{file_num}.yaml"
    
    # Check if file exists before deleting
    if os.path.isfile(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
        deleted_count += 1
    else:
        print(f"{filename} not found, skipping.")

print(f"\n{deleted_count} files deleted, starting from catalog-{start_file_num}.yaml")
