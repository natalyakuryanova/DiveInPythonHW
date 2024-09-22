import logging

# создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# создаем форматировщик
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# создаем обработчик для DEBUG
handlerDebug = logging.FileHandler(f"debug_info.log", mode='w')
handlerDebug.setLevel(logging.DEBUG)
handlerDebug.setFormatter(formatter)

# линкуем обработчик для DEBUG к логгеру
logger.addHandler(handlerDebug)

# создаем обработчик для WARNING
handlerWarn = logging.FileHandler(f"warnings_errors.log", mode='w')
handlerWarn.setLevel(logging.WARNING)
handlerWarn.setFormatter(formatter)

# линкуем обработчик для WARNING к логгеру
logger.addHandler(handlerWarn)

# Логирование сообщений различных уровней
logger.debug('Это сообщение уровня DEBUG.')
logger.info('Это сообщение уровня INFO.')
logger.warning('Это сообщение уровня WARNING.')
logger.error('Это сообщение уровня ERROR.')
logger.critical('Это сообщение уровня CRITICAL.')
