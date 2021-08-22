"""See README.md for package documentation."""

from setuptools import setup, find_namespace_packages

setup(
    name='kivyx.uix.behavior.tablikelooks',
    version='0.1.0.dev0',
    description='A mix-in class that adds tab-like graphical representation to BoxLayout.',
    author='Nattōsai Mitō',
    author_email='flow4re2c@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='Kivy',
    packages=find_namespace_packages(include=['kivyx.*']),
    package_data={},
    data_files=[],
    entry_points={},
)
