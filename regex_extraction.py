mport re

# Sample text for testing
sample_text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Currencies: $19.99, $1,234.56, €100, ¥5000
"""

# 1. Email Extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, sample_text)

# 2. URL Extraction
url_pattern = r"https?://[^\s]+"
urls = re.findall(url_pattern, sample_text)

# 3. Phone Number Extraction
phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
phones = re.findall(phone_pattern, sample_text)

# 4. Currency Extraction
currency_pattern = r"[$€¥]\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
currencies = re.findall(currency_pattern, sample_text)

# Print extracted data
print("Extracted Emails:", emails)
print("Extracted URLs:", urls)
print("Extracted Phones:", phones)
print("Extracted Currencies:", currencies)
