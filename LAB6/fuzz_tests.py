'''Fuzz tests for income_tax module using hypothesis'''

from hypothesis import given, strategies as st
from income_tax import taxable_income, tax_due, refund_status

# Fuzz taxable_income
@given(
    gross=st.integers(min_value=0, max_value=10_000_000),
    regime=st.sampled_from(["new", "old"]),
    investments=st.integers(min_value=0, max_value=500_000),
)
def test_taxable_income_fuzz(gross, regime, investments):
    # Should not raise for valid inputs
    result = taxable_income(gross, regime, investments)
    assert isinstance(result, int)
    assert result >= 0

# Fuzz tax_due
@given(
    taxable=st.integers(min_value=0, max_value=10_000_000),
    age=st.integers(min_value=0, max_value=120),
)
def test_tax_due_fuzz(taxable, age):
    result = tax_due(taxable, age)
    assert isinstance(result, int)
    assert result >= 0

# Fuzz refund_status
@given(
    tax_paid=st.integers(min_value=0, max_value=10_000_000),
    tax_due_amount=st.integers(min_value=0, max_value=10_000_000),
    filed_on_time=st.booleans(),
)
def test_refund_status_fuzz(tax_paid, tax_due_amount, filed_on_time):
    result = refund_status(tax_paid, tax_due_amount, filed_on_time)
    assert result in {"refund", "refund delayed", "pay balance", "pay balance with penalty", "settled"}
