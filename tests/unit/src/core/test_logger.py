import pytest

from src.data_provider.core.logger import Logger


@pytest.mark.asyncio
async def test_logger():
    logger = Logger()
    assert hasattr(logger, "info")
    assert hasattr(logger, "error")
