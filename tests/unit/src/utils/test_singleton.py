import pytest

from src.data_provider.utils import singleton


@pytest.mark.asyncio
async def test_singleton():
    @singleton
    class TestSingleton:
        pass

    obj1 = TestSingleton()
    obj2 = TestSingleton()

    assert id(obj1) == id(obj2)
