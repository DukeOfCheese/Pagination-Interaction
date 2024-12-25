import discord
import pytest
from paginator.simple import Simple

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
    paginator = Simple()
    await paginator.start(mock_context, sample_pages)

    assert paginator.pages == sample_pages
    assert paginator.total_page_count == len(sample_pages)
    assert paginator.current_page == 0

@pytest.mark.asyncio
async def test_next(mock_context, sample_pages):
    paginator = Simple()
    await paginator.start(mock_context, sample_pages)
    
    await paginator.next()
    assert paginator.current_page == 1

@pytest.mark.asyncio
async def test_previous(mock_context, sample_pages):
    paginator = Simple()
    await paginator.start(mock_context, sample_pages)
    
    await paginator.previous()
    assert paginator.current_page == len(sample_pages) - 1