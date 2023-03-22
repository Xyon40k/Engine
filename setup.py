from setuptools import setup, find_packages


setup(
    name='Engine',
    version='0.1',
    license='MIT',
    author="Alberto Rossani",
    author_email='albertopulcinik@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Xyon40k/Engine',
    keywords='project',
    install_requires=[
          'pygame',
        ],
)