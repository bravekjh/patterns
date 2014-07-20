from setuptools import setup

setup(
    name='patterns',
    version='0.1.2',
    author='Alexander Schepanovski',
    author_email='suor.web@gmail.com',

    description='Pattern matching for python',
    long_description=open('README.rst').read(),
    url='http://github.com/Suor/patterns',
    license='BSD',

    packages=['patterns'],
    install_requires=['codegen'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Pre-processors',
        'Intended Audience :: Developers',
    ]
)
