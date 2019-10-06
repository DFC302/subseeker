import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='subseeker',
	version='2.0',
	author="Matthew Greer",
	author_email="dfc302@protonmail.com",
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
        package_data={'': ['LICENSE'], '': ['README.md'], '': ['keywords.txt'], '': ['config.json'],},
        include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
     ],
)
