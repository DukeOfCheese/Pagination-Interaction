from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="discord.py-interaction-pagination",
    version="0.0.6",
    description="Easily create pagination for your embeds with interaction.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["Pagination"],
    package_dir={'': "src"},
    url="https://github.com/DukeOfCheese/Pagination-Interaction",
    author="soosBot and DukeOfCheese",
    author_email="dukeofcheesebusiness@gmail.com",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
