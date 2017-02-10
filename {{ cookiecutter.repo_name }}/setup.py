from setuptools import setup, find_packages


setup(
    name="{{ cookiecutter.repo_name }}",

    description="{{ cookiecutter.description }}",

    author="{{ cookiecutter.author_name }}",

    packages=find_packages(include='src'),

    package_dir={'{{ cookiecutter.repo_name }}': 'src'},
)
