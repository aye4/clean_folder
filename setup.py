from setuptools import setup

setup(
    name='clean_folder',
    version='1',
    description='File sorting tool',
    url='http://github.com/aye4/clean_folder',
    author='Andrei Yeremenko',
    author_email='aeremenko2022@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean_folder']}
)