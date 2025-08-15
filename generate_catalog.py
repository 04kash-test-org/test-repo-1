import os

start_file_num = 1009
total_files = 40
start_name_num = 1005 # first name_num value

for i in range(total_files):
    file_num = start_file_num + i
    name_num = start_name_num + i  # increases with no repeats
    
    filename = f"catalog-{file_num}.yaml"
    
    content = f"""# This file contains 1 Backstage Component entities

apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: example-ib-{name_num}
  description: Our squirrel-friendly Gloves ensures grandiose comfort for your pets {name_num}
spec:
  owner: team-a
  type: service
  lifecycle: experimental
"""
    
    with open(filename, "w") as f:
        f.write(content)

print(f"{total_files} catalog files created starting from catalog-{start_file_num}.yaml with name_num starting at {start_name_num}.")
