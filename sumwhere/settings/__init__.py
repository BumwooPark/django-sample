import os
import glob

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


# SECRET_KEY = os.environ['PROJECT_SECRET_KEY']
SECRET_KEY = '-h-_q^cf1daw_j-r--vi(lnk+(d!53p!3tv%2kka61b+w@nayt'

ENV = os.environ.get('PROJECT_ENV', 'dev')

from split_settings.tools import include

COMPONENTS_DIR = os.path.join(
    BASE_DIR,
    'sumwhere',
    'settings',
    'components'
)

COMPONENTS = [
    'components/{}'.format(os.path.basename(component))
    for component in glob.glob(os.path.join(COMPONENTS_DIR, '*.py'))
]

ENVIRONMENTS = ['environments/{}.py'.format(ENV)]

SETTINGS = COMPONENTS + ENVIRONMENTS

include(*SETTINGS)
