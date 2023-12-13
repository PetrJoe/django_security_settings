from setuptools import setup, find_packages

project_name = 'django-secure-settings'
project_version = '1.0'

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='django-secure-settings',
    version='1.0',
    description='Secure default settings for Django projects with dynamic adjustment based on DEBUG mode',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Akanmu Akinkunmi Joseph',
    author_email='petrjoe01@gmail.com',
    url='https://github.com/petrjoe/django-secure-settings',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='django security settings',
    install_requires=[
        'Django>=3.0',
    ],
    extras_require={
        'dev': [
            # List development dependencies here
        ],
    },
    entry_points={
        'console_scripts': [
            # Add any console scripts here
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/petrjoe/django-secure-settings/issues',
        'Source': 'https://github.com/petrjoe/django-secure-settings',
    },
)
