import os
import pytest
from exante.api import ExanteAPI
from exante.exceptions import BadEnvironment
from exante.definitions.environment import Environment

import logging

logger = logging.getLogger("unit")
logger.setLevel(level=logging.DEBUG)


def test_bad_api_environment_exception():
    with pytest.raises(BadEnvironment):
        ExanteAPI(
            client_id="",
            application_id="",
            shared_key="",
            api_scopes=[],
            environment="WRONG ENVIRONMENT",
        )

def test_api_environment(exante_api_demo_client):
    assert exante_api_demo_client.environment == Environment.Demo
