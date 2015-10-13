'''
Let's Make a Deal!

Apparently, there used to be a TV Game Show starring Monty Hall.

Contestants were shown three doors they had to choose from.
Behind one door was something great, let's say a new car.
Behind the other two doors, nothing.

The contestant chooses a door and then Monty Hall would open a different
door with nothing behind it. Then the contesant could stick with their
choice or decide to switch and pick the other of the two remaining doors.

It is a classic probability problem because it is always a better idea
to switch than to stick with your first guess. You will win twice as often.

This problem is counter-intuitive at first. But what it boils down to is
that the first time you choose a door there is a 1-in-3 chance of being
right. But the probabilities must add to one, so the second time you
have a 2-in-3 chance.

If you aren't convinced by Bayesian Statistics, then this script actually
runs the Monty Hall Game Show situation for you a huge number of times
for both situations:

1) You always stick with the first door.
2) You always switch to the second door.
'''

from random import randint


def main():
    print("\nLET'S MAKE A DEAL!\n")
    print('\nIF YOU ALWAYS STICK WITH YOUR FIRST DOOR:')
    N = 100000
    number_wins = 0
    for _ in xrange(N):
        if stay_with_your_first_door():
            number_wins += 1

    print('Number of wins ouf of ' + str(N) + ':\t' + str(number_wins))
    print('Percentage of winning rounds:\t' + str(100.0 * float(number_wins) / N))

    print('\nIF YOU ALWAYS SWITCH TO THE OTHER DOOR:')
    number_wins = 0
    for _ in xrange(N):
        if switch_to_other_door():
            number_wins += 1

    print('Number of wins ouf of ' + str(N) + ':\t' + str(number_wins))
    print('Percentage of winning rounds:\t' + str(100.0 * float(number_wins) / N) + '\n')


def set_up_stage():
    '''Monty Hall's people set up the stage with three doors,
    and place a shiny new car behind one of them.
    '''
    new_car = randint(0, 2)
    doors = [0, 0, 0]
    doors[new_car] = 1
    return doors


def select_first_door():
    '''You randomly select your first door.'''
    return randint(0, 2)


def revel_another_door(doors, your_door):
    '''Monty Hall reveals a door with nothing behind it.'''
    for i in xrange(3):
        if i != your_door and doors[i] == 0:
            return i


def select_new_door(your_door, door_revealed):
    '''You decide to switch to the remaining door.'''
    for i in xrange(3):
        if i != your_door and i != door_revealed:
            return i


def stay_with_your_first_door():
    '''You decide to stick with your first door...
    Did you win a new car???
    '''
    doors = set_up_stage()
    your_door = select_first_door()
    return doors[your_door] == 1


def switch_to_other_door():
    '''You decide to switch to the third door...
    Did you win a new car???
    '''
    doors = set_up_stage()
    your_door = select_first_door()
    door_revealed = revel_another_door(doors, your_door)
    your_new_door = select_new_door(your_door, door_revealed)
    return doors[your_new_door] == 1


if __name__ == '__main__':
    main()
