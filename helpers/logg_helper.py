from loguru import logger

logger.add(
    'data/info.log',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
)

