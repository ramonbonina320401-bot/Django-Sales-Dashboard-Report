import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangowebapp.settings'

import django
django.setup()

try:
    # Try to directly check if we can use login_required
    from django.contrib.auth.decorators import login_required
    print(f"login_required imported: {login_required}")
    
    # Now try to import dashboard.views
    import dashboard.views
    print("views module imported successfully!")
    
    # Check if product_list exists
    if hasattr(dashboard.views, 'product_list'):
        print("product_list found!")
    else:
        print("product_list NOT found")
        
except NameError as e:
    print(f"NameError: {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
