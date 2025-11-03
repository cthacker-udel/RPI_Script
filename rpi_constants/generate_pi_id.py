"""
Represents the callback used to generate new pi ids each time a PI boots.
"""

import shortuuid

"""
Callback for generating a new raspberry pi id.    
"""
def generate_pi_id() -> str:
    """
    Generates a new pi id for the given raspberry pi device.

    Returns:
        str: The generated raspberry pi id.
    """
    return shortuuid.ShortUUID().random(length=6)