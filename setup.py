from setuptools import setup, find_packages

setup(
    name="discord.py-interaction-pagination",
    version="1.0.0",
    description="Easily create pagination for your embeds with interaction (using discord.Interaction)",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    py_modules=["Pagination"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
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
    ],
    install_requires=[
        "discord.py>=2.0.0",
    ],
)