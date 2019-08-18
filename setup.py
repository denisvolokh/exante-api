import setuptools

import exanteapi

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
   version=exanteapi.__version__,
   description='Exante REST API python library',
   author='Denis Volokh',
   author_email='denis.volokh@gmail.com',
   packages=packages,
   install_requires=requires
)