with open('dashboard/views.py', 'r') as f:
    lines = f.readlines()

# Find all decorators
for i, line in enumerate(lines):
    if line.strip().startswith('@'):
        print(f'Line {i+1}: {line.rstrip()}')
        if i+1 < len(lines):
            print(f'Line {i+2}: {lines[i+1].rstrip()[:60]}')
        print()
