from setuptools import setup, find_packages
import re, io

# Following https://gist.github.com/arsho/fc651bfadd8a0f42be72156fd21bd8a9 to update package on PyPi

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open("lfig/__init__.py", encoding="utf_8_sig").read(),
).group(1)


setup(
    name="lfig",
    version="0.1.3",
    # package_dir={'': 'src'},
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="Latex figures from matplotlib",
    long_description=open("README.md").read(),
    install_requires=["numpy", "matplotlib"],
    # url='https://github.com/BillMills/python-package-example',
    url="https://github.com/flynnbr11/lfig-py",
    author="Brian Flynn",
    author_email="flynnbr@tcd.ie",
)
