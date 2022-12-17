from beensi_messages._conf import BASE_SETTINGS


def info(message: dict) -> dict:
    language_code = BASE_SETTINGS.LANGUAGE_CODE
    if BASE_SETTINGS.LANGUAGE_CODE not in message:
        language_code = 'en'
    return {
        'language_code': language_code,
        'status': 'info',
        'message': message[language_code],
    }