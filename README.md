```markdown
# Django Secure Settings Django Package

## Overview

The `django_secure_settings` Django package provides a set of secure default settings for Django projects, with the ability to dynamically adjust security settings based on the `DEBUG` mode. This package is intended to enhance the security posture of Django applications by applying best practices for different environments (development vs. production).

## Installation

Install the package using `pip` download the repo then extract it:

```bash
pip install -e .
```

## Usage

1. **Configuration in Django Project:**

   - Add `'django_secure_settings'` to the `INSTALLED_APPS` list in your main project's `settings.py`:

     ```python
     # settings.py
     INSTALLED_APPS = [
         # ... other apps
         'django_secure_settings',
     ]
     ```

2. **Import Secure Settings in `settings.py`:**

   - In your main project's `settings.py`, import the secure settings:

     ```python
     # settings.py
     from secure_settings.settings import *

     # ... your project-specific settings
     ```

3. **Adjust DEBUG-based Settings:**

   - The package includes conditional logic in `secure_settings/settings.py` to adjust security settings based on the `DEBUG` mode. Customize these settings as needed for your development and production environments.

   - Example of how the security settings are dynamically adjusted based on the `DEBUG` mode:

     ```python
     # In development (DEBUG=True), some security settings are relaxed for ease of debugging.
     if settings.DEBUG:
         SECURE_BROWSER_XSS_FILTER = False
         SECURE_CONTENT_TYPE_NOSNIFF = False
         SESSION_COOKIE_SECURE = False
         CSRF_COOKIE_SECURE = False
         SESSION_COOKIE_HTTPONLY = False
         CSRF_COOKIE_HTTPONLY = False
         X_FRAME_OPTIONS = 'ALLOW'  # Allow framing in development
         SECURE_HSTS_SECONDS = 0  # Disable HSTS in development
         SECURE_SSL_REDIRECT = False
     else:
         # In production (DEBUG=False), apply strict security settings.
         SECURE_BROWSER_XSS_FILTER = True
         SECURE_CONTENT_TYPE_NOSNIFF = True
         SESSION_COOKIE_SECURE = True
         CSRF_COOKIE_SECURE = True
         SESSION_COOKIE_HTTPONLY = True
         CSRF_COOKIE_HTTPONLY = True
         X_FRAME_OPTIONS = 'DENY'
         SECURE_HSTS_SECONDS = 31536000  # One year in seconds
         SECURE_SSL_REDIRECT = True
     ```

## Customization

- Modify the values in `secure_settings/settings.py` to tailor the security settings according to your project's requirements.
- For production deployments, ensure to set `DEBUG = False` in your main project's `settings.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Django best practices for security settings.
```

This expanded usage section provides more context on how to configure and use the `secure_settings` package in a Django project. Feel free to further customize it based on your specific project requirements.
