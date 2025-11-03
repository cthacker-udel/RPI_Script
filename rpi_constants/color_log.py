"""
Simple script to print color logs for debugging purposes.    
"""

import inspect
import hashlib
from typing import Callable, TypedDict
from datetime import datetime
from typing import Optional

RESET_COLOR = "\033[0m"

class LogDictionary(TypedDict):
    info: Callable[[str], None]
    invalid: Callable[[str], None]

def name_to_color(name: str) -> str:
    h = hashlib.md5(name.encode()).hexdigest()
    r, g, b = int(h[:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"\033[38;2;{r};{g};{b}m"


def color_log(debug: Optional[bool] = False) -> LogDictionary:
    call_stack = None
    callee_name = "<unknown>"
    info_color = name_to_color("info")
    invalid_color = name_to_color("invalid")

    try:
        call_stack = inspect.stack()
        callee_name = ""
        if len(call_stack) > 1:
            callee_name = call_stack[1].function
    finally:
        del call_stack
    
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S")
    method_color = name_to_color(callee_name)
    log_dict: LogDictionary = {
        "info": lambda message: print(f"{method_color}{callee_name}{RESET_COLOR}{info_color} [info] {message}{RESET_COLOR} {timestamp}") if debug else None,
        "invalid": lambda message: print(f"{method_color}{callee_name}{RESET_COLOR}{invalid_color} [invalid] {message}{RESET_COLOR} {timestamp}") if debug else None
    }

    return log_dict
