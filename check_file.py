import os
os.chdir(os.path.dirname(__file__))

with open('dashboard/views.py', 'rb') as f:
    content = f.read()

# Check if product_list is in the file
if b'def product_list' in content:
    print("✓ product_list found in file")
    # Find the line number
    lines = content.split(b'\n')
    for i, line in enumerate(lines, 1):
        if b'def product_list' in line:
            print(f"  at line {i}")
            break
else:
    print("✗ product_list NOT found in file")

# Check total lines
lines_count = content.count(b'\n')
print(f"Total lines in file: {lines_count}")

print(f"File size: {len(content)} bytes")
