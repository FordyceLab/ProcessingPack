from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
	name = 'processingpack',
	version = '0.1.0',
	url = 'https://github.com/mypackage.git',
	author = 'Daniel Mokhtari',
	author_email = '',
	description = 'Mitomi Experimental Image Processing',
	packages = find_packages(),    
	install_requires = requirements,
)