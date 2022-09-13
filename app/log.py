import logging
from logging.config import dictConfig

FORMAT = '%(asctime)s - [request_id:%(request_id)s] - %(module)s.%(funcName)s:%(lineno)d - %(levelname)s: %(message)s'

DICT_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': FORMAT
        }
    },
}

dictConfig(DICT_CONFIG)

logger = logging.getLogger(__name__)
