import os

SCHEMAS = (
    ('device-types', 'devicetype.json'),
    ('module-types', 'moduletype.json'),
)

IMAGE_FILETYPES = (
    'bmp', 'gif', 'pjp', 'jpg', 'pjpeg', 'jpeg', 'jfif', 'png', 'tif', 'tiff', 'webp'
)

COMPONENT_TYPES = (
    'console-ports',
    'console-server-ports',
    'power-ports',
    'power-outlets',
    'interfaces',
    'front-ports',
    'rear-ports',
    'device-bays',
    'module-bays',
)

PRECOMMIT_ALL_SWITCHES = [
  '-a',
  '--all-files',
  '--all'
]

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

KNOWN_SLUGS = set()
KNOWN_MODULES = set()

USE_LOCAL_KNOWN_SLUGS = True
USE_UPSTREAM_DIFF = True



NETBOX_DT_LIBRARY_URL = f"https://github.com/nrkno/netbox-devicetype-library.git"