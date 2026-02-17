# src/exception.py

import sys
from typing import Any


def error_message_detail(error: Exception, error_detail: Any) -> str:
    """
    Builds a detailed error message using the current exception traceback.
    Pass `sys` as error_detail while raising CustomException.
    """
    _, _, exc_tb = error_detail.exc_info()

    # Safety: in rare cases exc_tb can be None
    if exc_tb is None:
        return f"Error occurred: {str(error)}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        "Error occurred in python script name [{0}] line number [{1}] error message [{2}]"
        .format(file_name, line_number, str(error))
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message


# Optional test block (run this file directly to test)
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        # Use "from None" if you want to hide the original traceback
        raise CustomException(e, sys) from None

