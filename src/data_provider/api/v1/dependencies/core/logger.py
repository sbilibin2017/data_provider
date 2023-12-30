from src.data_provider.core import Logger
from src.data_provider.interfaces import ILogger


def get_logger() -> ILogger:
    return Logger()
