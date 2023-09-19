### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# There needs to be a ':' after 'else' on line 23.
# It should be == on line 21 not =
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# Syntax error on line 28, 'dif' should be 'def'
# Error on line 31, should return 'card1' not 'card'
# There should be a comma between card1 and card2 in the arguments on line 29
# lines 30 to 33 need to be indented


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
# These back ticks shouldn't be in the code
# Error on line 38 - total should initially equal 0
# The return should be outside the function
#The whole functino needs to be indented