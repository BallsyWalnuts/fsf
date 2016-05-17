#!/usr/bin/python
#
# Basic configuration attributes for scanner. Used as default
# unless the user overrides them. 
#

import socket

SCANNER_CONFIG = { 'LOG_PATH' : '/tmp/',
                   'YARA_PATH' : '/FULL/PATH/TO/fsf-server/yara/rules.yara',
                   'YARA_TRIGGER_PATH' : '/FULL/PATH/TO/fsf-server/yara/module_triggers/triggers.yara',
                   'EXPORT_PATH' : '/data/malware/',
                   'TIMEOUT' : 60,
                   'MAX_DEPTH' : 10 }

SERVER_CONFIG = { 'IP_ADDRESS' : socket.gethostname(),
                  'PORT' : 5800 }
