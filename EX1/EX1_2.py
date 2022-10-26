def EX1_2(height, base):
  '''
  we give height and base of triangle and python calculate the area of it
  ex:
  >>>EX1_2(7, 8):
  28
  '''
  if height>0 and base>0:
    area= (base*height)/2
    return area
  else:
    return "error"

