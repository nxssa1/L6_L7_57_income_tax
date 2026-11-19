def taxable_income(gross, regime, investments):
    """Calculate taxable income based on gross income, tax regime, and investment deductions.

    Args:
        gross (int or float): Gross income; must be non‑negative.
        regime (str): "new" or "old".
        investments (int or float): Amount invested under old regime; must be non‑negative.

    Returns:
        int: Taxable income (>= 0).
    """
    if gross < 0:
        raise ValueError("invalid income")
    if investments < 0:
        raise ValueError("invalid investments")
    if gross < 0:
        raise ValueError("invalid income")
    if regime == "new":
        deduction = 75000
    elif regime == "old":
        if investments > 150000:
            investments = 150000
        deduction = 50000 + investments
    else:
        raise ValueError("unknown regime")
    taxable = gross - deduction
    if taxable < 0:
        return 0
    return taxable


def tax_due(taxable, age):
    """Calculate tax due based on taxable income and age.

    Args:
        taxable (int or float): Taxable income; must be non‑negative.
        age (int): Age of the taxpayer; must be non‑negative.
    Returns:
        int: Tax due amount.
    """
    if taxable < 0:
        raise ValueError("invalid amount")
    if age < 0:
        raise ValueError("invalid age")
    if taxable < 0:
        raise ValueError("invalid amount")
    if age >= 80:
        exempt = 500000
    elif age >= 60:
        exempt = 300000
    else:
        exempt = 250000
    if taxable <= exempt:
        return 0
    slab = taxable - exempt
    if slab <= 250000:
        return slab * 5 // 100
    return 12500 + (slab - 250000) * 20 // 100


def refund_status(tax_paid, tax_due_amount, filed_on_time):
    difference = tax_paid - tax_due_amount
    if difference > 0:
        if filed_on_time:
            return "refund"
        return "refund delayed"
    elif difference < 0:
        if filed_on_time:
            return "pay balance"
        return "pay balance with penalty"
    return "settled"
