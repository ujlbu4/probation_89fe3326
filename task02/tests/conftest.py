import pytest

# enable assertion rewriting for an imported helper modules (detailed introspection of expressions upon assertion failures)
# more details at: https://docs.pytest.org/en/stable/assert.html#assertion-introspection-details
pytest.register_assert_rewrite("tests.client")
