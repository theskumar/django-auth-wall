import setuptools

setuptools.setup(
    name="django-auth-wall",
    version="0.2.0",
    url="https://github.com/theskumar/django-auth-wall",

    author="Saurabh Kumar",
    author_email="saurabh@saurabh-kumar@gmail.com",

    description="Puts your staging site behind a basic auth layer.",
    long_description=open('README.rst').read(),

    py_modules=['django_auth_wall'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',

    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: System Administrators',
    ],
    keywords=(
        'security', 'django', 'python', 'basic authentication'
    ),
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
