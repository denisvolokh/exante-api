import setuptools

import exante

packages = setuptools.find_packages(exclude=[
    'tests',
    'tests.integration',
    'tests.unit'
])
requires = [
    'requests'
]


setuptools.setup(
   name='exante',
   version=exante.__version__,
   description='Exante REST API python library',
   author='Denis Volokh',
   author_email='denis.volokh@gmail.com',
   packages=packages,
   install_requires=requires
)
