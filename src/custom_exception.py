import sys
class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_error_message(message, error_detail):
        """Format the error message with traceback details."""
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code if exc_tb else "Unknown"
        return f"{message} | Error: {error_detail} | File: {file_name}"

    def __str__(self):
        return self.error_message