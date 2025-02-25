
def check_password(password):
    """
    Checks if the password length is greater than 5 characters.
    """
    if len(password) > 5:
        return True
    else:
        return False
