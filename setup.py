from setuptools import setup
from pathlib import Path

setup(name='biogasmod',
      version='0.1.0',
      author= 'Joana Martins dos Santos'
      author_email= 'joanamlmsantos@gmail.com'
      description='Landfill biogas modulation package',
      long_description=Path("README.rst").read_text(encoding="utf-8"),
      long_description_content_type="text/x-rst", 
      packages=setuptools.find_packages(),
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: BSD (3-clause)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Waste Management',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Simulation',
    ],
    python_requires='>=3.6',
    zip_safe=False)
