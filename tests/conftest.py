import pytest
from playwright.sync_api import APIRequestContext, Playwright, sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def api_request(playwright_instance: Playwright, base_url) -> APIRequestContext:
    request_context = playwright_instance.request.new_context(base_url=base_url)
    yield request_context
    request_context.dispose()
