from random import randrange


counterh = 0
counter = 0

while counterh < 10:
  if randrange(0,2) == 0:
    counterh += 1
  else:
    counterh = 0

  counter += 1

print counter﻿
