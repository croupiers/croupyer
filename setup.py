from distutils.core import setup

setup(
    name='Croupyer',
    version='0.0.1',
    author='Sergio Arbeo',
    author_email='serabe@gmail.com',
    packages=['croupyer', 'croupyer.test'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Generators generating random stuff.',
    long_description=open('README.md').read(),
    install_requires= [
    ],
)
