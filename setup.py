from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='django_flash_templatetag',
      version=version,
      description="convenience templatetag for django-flash package",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Robert Marianski',
      author_email='rmarianski@openplans.org',
      url='',
      license='gpl',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'django-flash',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
