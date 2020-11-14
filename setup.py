from setuptools import setup, find_packages

setup(
    name='lfig',
    version='0.1.1',
    # package_dir={'': 'src'},
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Latex figures from matplotlib',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'matplotlib'],
    # url='https://github.com/BillMills/python-package-example',
    author='Brian Flynn',
    author_email='flynnbr@tcd.ie'
)