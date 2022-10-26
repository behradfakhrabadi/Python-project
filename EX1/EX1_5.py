def EX1_5(age):
  '''
  classify the age group of people by taking their age
  ex:
  >>>EX1_5(12):
  child
  '''
  if age<=1 and age>0:
    return "infant"
  if age>1 and age<13:
    return "child"
  if age>=13 and age<20:
    return "teenager"
  if age>=20:
    return "adult"
  else:
    return "error"
