from hello import hello_user, hello_world, slow_hello
import pytest
from datetime import datetime as dt
from datetime import timedelta
@pytest.mark.basic
def test_hello_world():
    assert hello_world() == "Hello World!!"

_users = ["Joe", "Alfred", "William", "Averel"]
@pytest.fixture(scope="module", params=_users)
def user(request):
    yield request.param

@pytest.mark.fixtured
def test_hello_fixtured(user):
    assert hello_user(user) == f"Hello {user}!!", "'{hello_user(user)}' != 'Hello {user}!!'"

@pytest.mark.slow
def test_slow_hello():
    start = dt.now()
    result = slow_hello()
    elapsed = dt.now() - start
    assert elapsed >= timedelta(seconds=10), "Slow hello should take 10s minimum!"
