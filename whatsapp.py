import re
from urllib.parse import quote

ALLOWED_CHARACTERS = re.compile(r'[\d\s+().-]+')


def normalize_whatsapp(value):
    """Return a number in international format (628...), or None if it is invalid."""
    value = (value or '').strip()
    if not ALLOWED_CHARACTERS.fullmatch(value):
        return None

    digits = re.sub(r'\D', '', value)
    if digits.startswith('0'):
        digits = '62' + digits[1:]
    elif digits.startswith('8'):
        digits = '62' + digits

    return digits if 10 <= len(digits) <= 15 else None


def whatsapp_link(contact, message):
    """Return a link that opens WhatsApp with the message ready to send."""
    number = normalize_whatsapp(contact)
    if number is None:
        return None
    return f'https://wa.me/{number}?text={quote(message)}'
