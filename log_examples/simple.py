import logging
import logging.config


# logging.basicConfig(level=logging.DEBUG)
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename': 'all.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
        }
    }
})


log = logging.getLogger(__name__)


def log_all():
    log.debug('debug %s', globals())
    log.info('info %s', 123)
    log.warning('warning')
    log.error('error')
    try:
        1 / 0
    except Exception:
    	log.exception('Произошла страшная ошибка.')


if __name__ == '__main__':
	log_all()
