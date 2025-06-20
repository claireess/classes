monster_life = 50
print ('orc: i have ' + str(monster_life) + ' hearts, you wont be able to kill me')
arrow = 8
print ('hero: and with my ' + str(arrow) + ' arrows i\'ll defeat you')


if arrow < monster_life :
  print ('you lose')
if arrow > monster_life :
  print ('you win')
if arrow == monster_life :
  print ('you win')
