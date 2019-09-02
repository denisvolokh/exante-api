import logging
import os

import betamax
import pytest
from betamax_serializers import pretty_json

from exante.api import ExanteAPI
from exante.definitions.environment import Environment
from exante.definitions.scope import Scope

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "exante/tests/integration/cassettes"
    config.default_cassette_options["serialize_with"] = "prettyjson"


SHARED_KEY = os.getenv("EXANTE__SHARED_KEY", None)
CLIENT_ID = os.getenv("EXANTE__CLIENT_ID", None)
APPLICATION_ID = os.getenv("EXANTE__APPLICATION_ID", None)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ig.tests.conftest")


@pytest.fixture(scope="session")
def exante_api_demo_client():
    """
        Returns a Exante API instance for DEMO environment
    """

    logger.info(f"[+] Clinet ID from .test.env: {CLIENT_ID}")

    api_client = ExanteAPI(
        client_id=CLIENT_ID,
        application_id=APPLICATION_ID,
        shared_key=SHARED_KEY,
        api_scopes=[
            Scope.Symbols,
            Scope.Change,
            Scope.Crossrates,
            Scope.Feed,
            Scope.Accounts,
            Scope.AccountsSummary,
            Scope.Orders,
        ],
        environment=Environment.Demo,
    )

    return api_client


@pytest.fixture
def exante_api_demo_client_no_scopes():
    """
        Returns a Exante API instance for DEMO environment with no scopes defined
    """

    api_client = ExanteAPI(
        client_id=CLIENT_ID,
        application_id=APPLICATION_ID,
        shared_key=SHARED_KEY,
        api_scopes=[],
        environment=Environment.Demo,
    )

    return api_client
