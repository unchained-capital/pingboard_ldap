from os      import environ
from logging import getLogger, DEBUG

LOG = getLogger(__name__)
if environ.get('DEBUG'):
    LOG.setLevel(DEBUG)
