from setuptools import setup

setup(
    name='nani_fighter',
    packages=['nani_fighter'],  # this must be the same as the name above
    version='1.1',
    description='A Simple Game',
    long_description=open("README.md").read(),
    author='Fazle Rahat',
    author_email='fr.rahat@gmail.com',
    license='MIT',
    url='https://github.com/frrahat/Nani-Fighter',  # use the URL to the github repo
    download_url='https://github.com/frrahat/Nani-Fighter/archive/1.1.tar.gz',  # I'll explain this in a second
    keywords=['game', 'school', 'shooting'],  # arbitrary keywords
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pygame',
    ],
)
