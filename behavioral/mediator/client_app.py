from participant import Participant
from room import Room


def main() -> None:
    """
    Client app
    """
    room = Room()
    tim = Participant('Tim', room)
    alex = Participant('Alex', room)

    print(f"Tim have {tim.points} point(s).\nAlex have {alex.points} point(s).")

    # Tim increases points of each room participant on 2
    tim.increase(2)
    tony = Participant('Tony', room)

    print(f"\nTim have {tim.points} point(s).\nAlex have {alex.points} point(s).\nTony have {tony.points} point(s).")

    # Alex decreases points of each room participant on 4
    alex.decrease(4)

    print(f"\nTim have {tim.points} point(s).\nAlex have {alex.points} point(s).\nTony have {tony.points} point(s).")

    # Tony increases points of each room participant on 8
    tony.increase(8)
    print(f"\nTim have {tim.points} point(s).\nAlex have {alex.points} point(s).\nTony have {tony.points} point(s).")


if __name__ == '__main__':
    main()
