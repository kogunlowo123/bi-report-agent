"""Test configuration for BI Report Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "bi-report-agent", "category": "Data Engineering"}
