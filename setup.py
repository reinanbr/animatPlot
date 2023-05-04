from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()


setup(name='animateplot',
    version='0.3.1',
    url='https://github.com/reinanbr/dreams',
    license='BSD v3',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='gif video plot',
    description=u"Library for generate gif or video from plots",
    packages=find_packages(),
    install_requires=['matplotlib','numpy','imageio','opencv-python'])
