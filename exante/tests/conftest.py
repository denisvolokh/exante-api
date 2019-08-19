import os
import pytest
import betamax
from betamax_serializers import pretty_json
from exante.api import ExanteAPI
from exante.definitions.scope import Scope
from exante.definitions.environment import Environment

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "exante/tests/integration/cassettes"
    config.default_cassette_options["serialize_with"] = "prettyjson"


SHARED_KEY = os.getenv("EXANTE__SHARED_KEY", "foo")
CLIENT_ID = os.getenv("EXANTE__CLIENT_ID", "foo")
APPLICATION_ID = os.getenv("EXANTE__APPLICATION_ID", "foo")


@pytest.fixture
def exante_api_demo_client():
    """
        Returns a Exante API instance for DEMO environment
    """

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
