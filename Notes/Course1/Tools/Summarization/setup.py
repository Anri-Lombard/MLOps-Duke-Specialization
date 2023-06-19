from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line for line in f.read().split('\n')]

setup(
    name = 'summarize',
    description = 'A text summarizer using HuggingFace Transformers',
    packages = find_packages(),
    author = 'Anri Lombard',
    entry_points = """
        [console_scripts]
        summarize = summarize.main:main
    """,
    install_requires = requirements,
    version = '0.0.1',
    url = 'https://github.com/alfredodeza/huggingface-summarization'
)