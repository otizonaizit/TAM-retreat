# Analog programming
Two exercises to activate the body and the mind

Common goal of both exercises is to sort a deck of tarot cards by value

Before starting, make yourself acquainted with the meaning and the power of the tarot cards. Carefully read [this booklet](https://aspp.school/_media/tarot-runic.pdf)

# First experiment: human sorting
## Setup
- 1 volunteer to keep the time spent sorting
- each person picks up a runic tarot card from the randomly shuffled deck on the table
- moving around and speaking is allowed until the tarot cards are displayed sorted on the table

# Second experiment: machine sorting
## Setup
We will keep some timings:
- time spent *programming* and *compiling*
- time spent *executing* the program

## Programming in groups
Divide in groups and write pseudo-code on paper to sort a randomly shuffled deck of runic tarot cards.

## Rules
- You have to "compile" the program in our special Assembly language, which consists of the following instructions:
  - **`fetch(ADDRESS, REGISTER)`**: fetch a value from the memory address `ADDRESS` and store it into register `REGISTER`
  - **`push(ADDRESS, REGISTER)`**: push a value from the register `REGISTER` into the memory address `ADDRESS`
  - **`sort(REGISTERX, REGISTERY)`**: sort the values in `REGISTERX` and `REGISTERY` so that the value in `REGISTERX`is **bigger or equal** than the value in `REGISTERY`
- "compile" in this context means translating the pseudo-code in a long sequence of the three instructions above
- note that if you use loops, you have to "unroll" them when you compile the program
- you are going to be using the following hardware to execute the compiled program

Present your solution to the general assembly and choose one implementation to try out!

## Hardware setup
- distribute manga tarot cards in front of the seats (or on the table in front of every seat): they represent memory addresses and should not be touched
- distribute runic tarot cards to every participant: they represent values and are hold by participants 
- 2 volunteers to be two CPUs. A CPU can only execute one of the above instructions at a time
- 4 empty seats will be the 4 registers: `R1`, `R2`, `R3`, `R4`
- Everyone who is not a CPU is data:
  - you'll have an address when you are stored in memory (the manga tarot card in front of your sit)
  - you'll have a value (the runic tarot card you hold on your hand): don't let it go!
  - when `fetch`-ed by the CPU, you'll take the PCI-bus and go sit on the corresponding register, taking the runic card with you
  - when `push`-ed by the CPU, you'll take the PCI-bus and go sit on the corresponding memory address, taking the runic card with you
  - when `sort`-ed, move to the appropriate register, according the semantics of the `sort` instruction defined above 

## Run the compiled code!
The CPUs will run the program by saying the instructions out loud and everyone else will move around accordingly. You can also literally "run" if you want to speed up the process a bit.

Do not forget to start the timing!

## Stopping condition
- The program will finish when the runic tarot cards are stored sorted in memory
