from setuptools import setup

setup(name='doc_reader_python',
      version='1',
      packages=['doc_reader_python'],
      entry_points={
          'console_scripts': [
              'doc_reader_python = doc_reader_python.__main__:main'
          ]
      },
)
