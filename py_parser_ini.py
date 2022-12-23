#!/usr/bin/env python3

#https://docs.python.org/3/library/configparser.html

import configparser

config = configparser.ConfigParser()
config.sections()
config.read('./conf.ini')

str = config['bitbucket.org']['User']
print(str)

str = config['DEFAULT']['Compression']
print(str)
#yes

# config.read('./conf.ini')
print(config.read('./conf.ini'))

# config.sections()
print(config.sections())
"""
['bitbucket.org', 'topsecret.server.com']
"""

# 'bitbucket.org' in config
print('bitbucket.org' in config)
#True

#'bytebong.com' in config
print('bytebong.com' in config)
#False

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])

for key in config['bitbucket.org']:  
    print(key)

"""

>>> 
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'
"""