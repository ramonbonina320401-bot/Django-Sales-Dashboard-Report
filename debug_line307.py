with open('dashboard/views.py', 'r') as f:
    lines = f.readlines()

# Show lines 305-310
for i in range(304, 312):
    if i < len(lines):
        print(f'{i+1:3d}: {lines[i].rstrip()[:100]}')
