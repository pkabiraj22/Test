def is_numeric(user_input):
  # Try converting the input to a float. If successful, it's numeric.
  try:
    int(user_input)
    return True
  except ValueError:
    return False
