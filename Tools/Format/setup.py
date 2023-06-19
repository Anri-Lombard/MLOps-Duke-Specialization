from setuptools import setup, find_packages

setup(
    name = 'jformat',
    version = '0.0.1',
    description = 'A JSON formatter',
    install_requires = ["click", "colorama"],
    entry_points = """
        [console_scripts]
        jformat = jformat.main:main
    """,
    author = 'Anri Lombard',
    author_email = 'anri.m.lombard@gmail.com',
    packages = find_packages(),
)