import pytest
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
