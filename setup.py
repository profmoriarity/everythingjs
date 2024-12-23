from setuptools import setup, find_packages

setup(
    name='everythingjs',
    version='0.2.0',  # Incremented version for updates
    author='Siva Krishna',
    author_email='krishna.krish759213@gmail.com',
    description='A Python module for working seamlessly with JavaScript files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/profmoriarity/everythingjs',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4',  # For HTML parsing
        'requests',        # For HTTP requests
    ],
    entry_points={
        'console_scripts': [
            'everythingjs=everythingjs.app:main',  # CLI entry point
        ],
    },
)
