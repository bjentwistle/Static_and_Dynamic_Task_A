### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame: #class not defined.
#Need a class Card with self and value at least.

  #Need to create an instance of Card called card.

  def check_for_ace(self, card):
    if card.value = 1: #card.value not defined, == needed
      return True
    else #semi colon missing here :
      return False

  # def not dif - comma missing in args between card1 and card2.
  dif highest_card(self, card1 card2): #card1 and card2 are not defined.
  if card1.value > card2.value: #indentation errors
    return card #should return card1 if true.
  else:
    return card2

#missed the indentation error here.
def cards_total(self, cards): #cards is not defined - perhaps a list
  total #not defined, should be =0  to start with
  for card in cards:
    total += card.value
    return "You have a total of" + total #needs () around the returned items
    #missed the concatenation error here and indentation again.

```
