Important Reminder for Tailwind

Since you are using django-tailwind, remember that you need two separate terminals running at the same time for your design to update:

    Terminal 1: python manage.py runserver (The website)

    Terminal 2: python manage.py tailwind start (The CSS compiler)

If you don't run Terminal 2, your Tailwind classes won't update when you change the HTML.
