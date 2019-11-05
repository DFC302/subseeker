import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='subseeker',
	version='2.1.1',
	author="Matthew Greer",
	author_email="pydev302@gmail.com",
        license='MIT',
	description="A sub enumeration tool.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DFC302/subseeker",
        keywords=['enumeration', 'domain', 'sub', 'tool'],
	packages=setuptools.find_packages(),
        install_requires=[
            "requests",
            "argparse",
            "termcolor",
        ],
        package_data={'': ['LICENSE'], '': ['README.md'], '': ['wordlists.keywords.txt'], '': ['core.subseeker_config.json'],},
        include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
     ],
     entry_points={
            'console_scripts': [
                "subseeker = subseeker_core.subseeker:main",
            ],
        },
)
