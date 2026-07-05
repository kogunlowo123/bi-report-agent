"""BI Report Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_report():
    """Test Generate a BI report from a natural language business question."""
    tools = AgentTools()
    result = await tools.generate_report(question="test", data_source="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_visualization():
    """Test Create a data visualization from a dataset."""
    tools = AgentTools()
    result = await tools.create_visualization(dataset="test", chart_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_delivery():
    """Test Schedule automated report delivery via email or Slack."""
    tools = AgentTools()
    result = await tools.schedule_delivery(report_id="test", schedule="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_suggest_chart_type():
    """Test Suggest the best chart type for a given dataset and question."""
    tools = AgentTools()
    result = await tools.suggest_chart_type(data_profile="test", question="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.bi_report_agent_agent import BiReportAgentAgent
    agent = BiReportAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
