from setuptools import setup, find_packages

setup(
    name='beensi_messages',
    version='0.001',
    license='BEENSI',
    author='nvd',
    author_email='navidsoleymani@ymail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/b-packages/messages.git',
    keywords='_messages',
    install_requires=[
        'pydantic',
    ],
)
