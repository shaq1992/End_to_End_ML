import sys, os

def create_custom_error_message(error_message):
    exc_type, exc_obj, tb = sys.exc_info()
    fname = tb.tb_frame.f_code.co_filename
    line_no = tb.tb_lineno
    custom_error_message = f"----Error Occured In File: {fname} ||| Line Number {line_no} with Error Message {str(error_message)}"
    
    return custom_error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super.__init__(error_message)
        self.error_message=create_custom_error_message(error_message)
        
    def __str__(self):
        return self.error_message
    
    
