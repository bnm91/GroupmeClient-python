from distutils.core import setup

setup(
  name = 'GroupmeClient',
  packages = ['GroupmeClient', 'GroupmeClient.ApiWrapper', 'GroupmeClient.Utilities'],
  version = '0.1.1',
  description = 'A python library for using GroupMes API',
  author = 'Nixon Ball',
  author_email = 'ball.nixonm@gmail.com',
  url = 'https://github.com/bnm91/GroupmeClient-python', 
  download_url = 'https://github.com/bnm91/GroupmeClient-python/archive/0.1.1.tar.gz', 
  keywords = ['GroupMe', 'API', 'client', 'python'], 
  classifiers = [],
  install_requires=['requests']
)
