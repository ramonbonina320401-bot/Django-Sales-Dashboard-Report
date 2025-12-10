import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangowebapp.settings'

# Try to import step by step
try:
    print("1. Importing django...")
    import django
    print("2. Setting up django...")
    django.setup()
    print("3. Importing views...")
    import importlib.util
    
    spec = importlib.util.spec_from_file_location("views_test", "dashboard/views.py")
    module = importlib.util.module_from_spec(spec)
    
    # Add to sys.modules with package context
    sys.modules['dashboard.views'] = module
    sys.modules['dashboard'] = importlib.import_module('dashboard')
    
    print("4. Loading module...")
    spec.loader.exec_module(module)
    print("5. Module loaded successfully!")
    
    if hasattr(module, 'product_list'):
        print("6. product_list found!")
    else:
        print("6. product_list NOT found!")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
