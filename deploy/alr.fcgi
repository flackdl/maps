#!/home8/heracent/python27/bin/python
import sys
import os

# Add a custom Python path.
sys.path.insert(0, '/home8/heracent/python27/site-packages')
sys.path.append('/home8/heracent/alr')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.prod'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")