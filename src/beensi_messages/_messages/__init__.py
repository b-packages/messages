from ._info import info
from ._warning import warning
from ._error import error

from . import (
    _beanser_name_not_correct,
    _beanser_name_correct_format,
    _password_not_correct,
    _password_correct_format,
    _email_address_incorrect,
    _beanser_does_not_exist,
    _please_choose_another_beanser_name,
    _please_choose_another_email_address,
    _information_about_the_desired_id_was_not_found,
)

BEANSER_NAME_NOT_CORRECT = error(_beanser_name_not_correct.message)
BEANSER_NAME_CORRECT_FORMAT = info(_beanser_name_correct_format.message)
PASSWORD_NOT_CORRECT = error(_password_not_correct.message)
PASSWORD_CORRECT_FORMAT = info(_password_correct_format.message)
EMAIL_ADDRESS_INCORRECT = error(_email_address_incorrect.message)
BEANSER_DOES_NOT_EXIST = error(_beanser_does_not_exist.message)
PLEASE_CHOOSE_ANOTHER_BEANSER_NAME = error(_please_choose_another_beanser_name.message)
PLEASE_CHOOSE_ANOTHER_EMAIL_ADDRESS = error(_please_choose_another_email_address.message)
INFORMATION_ABOUT_THE_DESIRED_ID_WAS_NOT_FOUND = error(_information_about_the_desired_id_was_not_found.message)
