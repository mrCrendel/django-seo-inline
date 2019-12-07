import os
from setuptools import setup

CLASSIFIERS = [
    "Development Status :: 1 - Beta",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "Framework :: Django :: 2.0",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]

setup(
    name="django-seo-inline",
    version='0.0.1',
    author="Ruslan Tolkun uulu",
    author_email="tggrmi@gmail.com",
    description="Plugs for Seo Model Inline",
    # long_description=LONG_DESCRIPTION,
    url="https://github.com/NursErgesh/django_2gis_maps.git",
    packages=("django-seo-inline",),
    include_package_data=True,
    install_requires=open('requirements/requirements.txt').read().splitlines(),
    tests_require=open('requirements/test.txt').read().splitlines(),
    classifiers=CLASSIFIERS,
    zip_safe=False,
)