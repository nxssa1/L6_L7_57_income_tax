def clean_pan(pan):
    """
    Removes spaces from a PAN and upper-cases it.
    Returns an empty string for any input that isn't a usable, non-empty string
    instead of crashing (e.g. None, numbers, or whitespace-only text).
    """
    if not isinstance(pan, str):
        return ""
    cleaned = pan.strip().replace(' ', '').upper()
    return cleaned

def parse_amount(text):
    """
    Converts an amount such as 'Rs 12,50,000' into an int.
    Strips 'Rs' and commas/spaces before converting. Returns None (instead of
    raising) when the input isn't a string or doesn't contain a valid integer
    after cleaning.
    """
    if not isinstance(text, str):
        return None
    cleaned = text.replace('Rs', '').replace(',', '').strip()
    if cleaned == "":
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None

def parse_tax_slab(line):
    """
    Parses 'LOW-HIGH:RATE' into a (low, high, rate) tuple.
    Returns None (instead of raising) when the input isn't a string, is
    missing the ':' or '-' separators, or any of the three parts isn't a
    valid integer.
    """
    if not isinstance(line, str):
        return None

    if ':' not in line:
        return None
    parts = line.split(':')
    if len(parts) != 2:
        return None
    limits, rate = parts

    if '-' not in limits:
        return None
    bounds = limits.split('-')
    if len(bounds) != 2:
        return None
    low, high = bounds

    try:
        return int(low), int(high), int(rate)
    except ValueError:
        return None

def main():
    print("==== Running clean_pan ====")
    value = input("Enter a PAN (e.g. abcde 1234f): ")
    print("Cleaned PAN:", clean_pan(value))

    print("\n==== Running parse_amount ====")
    value = input("Enter an amount (e.g. Rs 12,50,000): ")
    print("Amount in rupees:", parse_amount(value))

    print("\n==== Running parse_tax_slab ====")
    value = input("Enter a tax slab as LOW-HIGH:RATE (e.g. 250000-500000:5): ")
    print("Tax slab (low, high, rate):", parse_tax_slab(value))

if __name__ == "__main__":
    main()
