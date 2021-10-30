from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mlalgo',
  version='0.0.1',
  description='mlalgo',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Anjani Kumar Keshari',
  author_email='anj.kesh01@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['Machine Learning Algorithms', 'Supervised', 'Algo', 'Unsupervised', 'ML'],
  packages=find_packages(),
  install_requires=[''] 
)