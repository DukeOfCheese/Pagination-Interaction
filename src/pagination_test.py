import discord
import pytest
import pagination_interaction

@pytest.fixture
def mock_context():
    class MockContext:
        author = discord.Object(id=123456789)
    return MockContext()

@pytest.fixture
def mock_interaction():
    class MockInteraction:
        user = discord.Object(id=123456789)
    return MockInteraction()

@pytest.fixture
def sample_pages():
    return [discord.Embed(title=f"Page {i}") for i in range(5)]

@pytest.mark.asyncio
async def test_paginator_start(mock_context, sample_pages):
    await pagination_interaction.Simple().start(mock_context, sample_pages)