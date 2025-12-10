import os
os.chdir(os.path.dirname(__file__))

with open('dashboard/views.py', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print("\nLast 20 lines:")
for i, line in enumerate(lines[-20:], start=len(lines)-20+1):
    print(f"{i:3d}: {line.rstrip()[:80]}")
