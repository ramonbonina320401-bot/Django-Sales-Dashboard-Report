import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangowebapp.settings'

try:
    import django
    print("Django imported")
    
    django.setup()
    print("Django setup complete")
    
    # Now try importing views
    from dashboard import views
    print("Views imported successfully")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
