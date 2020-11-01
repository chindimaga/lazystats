from setuptools import find_packages, setup

with open('README.md') as readme_file:
    README = readme_file.read()

with open('CHANGELOG.txt') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='lazystats',
    version='0.0.3',
    description='This library has basic mathematical implementations which can increase your working pace',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT License',
    packages=find_packages(),
    author='Rahul D & Samarth',
    author_email='d18b@iitg.ac.in',
    keywords=['Statistics', 'Probability', 'Maths'],
    url='https://github.com/chindimaga/lazystats',
    download_url='https://pypi.org/project/lazystats/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)