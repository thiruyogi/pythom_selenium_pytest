import pytest
import logging
import inspect


@pytest.mark.usefixtures("one_time_setup")
class BaseClass:
    pass