from setuptools import setup, find_packages

NAME = 'gioia'
DESCRIPTION = 'Gioia SV Restaurant Bern CLI'
URL = 'https://github.com/Nachtalb/gioia'
EMAIL = 'nickespig@gmail.com'
AUTHOR = 'Nick Espig'

REQUIRED = [
    'requests-html'
]

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires='>=3.6.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['gioia=gioia.gioia:main'],
    },
    install_requires=REQUIRED,
    setup_requires=REQUIRED,
    license='MIT',
    version='1.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
