def is_number(_object: object) -> bool:
  if isinstance(_object, int) or isinstance(_object, float):
    return True
  else:
    return False
  

def is_container(_object: object) -> bool:
  if isinstance(_object, tuple):
    return True
  elif isinstance(_object, list):
    return True
  elif isinstance(_object, dict):
    return True
  elif isinstance(_object, set):
    return True
  else:
    return False
  

def clamp(value, _min, _max) -> Number:
  if is_number(value):
    if value < _min:
      return _min
    if value > _max:
      return _max
    else:
      return value
