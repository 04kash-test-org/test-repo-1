import os

start_file_num = 150
total_files = 50

for i in range(total_files):
    file_num = start_file_num + i
    filename = f"catalog-{file_num}.yaml"
    
    # Read original content
    with open(filename, "r") as f:
        lines = f.readlines()

    # Modify description line only
    new_lines = []
    for line in lines:
        if line.strip().startswith("description:"):
            new_line = f"  description: Updated description for catalog-{file_num}\n"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Write modified content back to the file
    with open(filename, "w") as f:
        f.writelines(new_lines)

print(f"{total_files} catalog files updated starting from catalog-{start_file_num}.yaml")
