# Analog programming
Two exercises to activate the body and the mind

Common goal of both exercises is to sort a deck of tarot cards by value

Before starting, make yourself acquainted with the meanining and the power of the tarot cards. Carefully read [this booklet](https://aspp.school/wiki/_media/tarot-runic.pdf)

## First experiment: human sorting
Setup:
- 1 volunteer to keep the time spent sorting
- each person picks up a tarot card from the randomly shuffled deck on the table
- moving around and speaking is allowed until the tarot cards are displayed sorted on the table

## Second experiment: machine sorting
Setup:
- 2 volunteers to keep the time:
  - one volunteer keeps the time spent *programming*
  - one volunteer keeps the time spent *executing* the program
- 2 volunteers to be the *programmers*:
  - can use the whiteboard
  - can and should speak and think loudly and ask for help
- 2 volunteers to be two CPUs:
  - only understand the instructions:
    - **fetch** a value from a memory address into register `N` ➔ returns `0` if succeded else `1` 
    - **push** the value from register `N` to a memory address ➔ returns `0` if succeded else `1` 
    - **compare** var0 and var1 ➔ returns `0` if `var0 ≥ var1` else `1`
- 4 volunteers to be CPU registers:
  - each register has a tag: `R1`, `R2`, `R3`, `R4`
  - a value fetched from memory is kept in short-term memory by the registers
  - the result value of an operation is stored in one register
- everyone else sits on their seats and represent RAM:
  - they own a *value*, i.e. they hold on a tarot card
  - they have an address based on their seating order: 0th seat, 1st seat, 2nd seat, 3rd seat, 4th seat, etc…
  - when *fetched*, walk to the corresponding register and hand in their *value* (card)
  - when *pushed*, walk to the corresponding register and fetch their new *value* (card)
- each RAM address comes and picks up a random tarot card as initialization step

