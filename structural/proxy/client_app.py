from structural.proxy.impl import RealPerson, ProxyPerson


def main() -> None:
    """
    Client app
    """

    age = 10
    young_person = RealPerson('Ivan', age)
    young_responsible_person = ProxyPerson('Sergio', age)

    print("Young person do:")
    print(young_person.drive())
    print(young_person.drink())
    print(young_person.drink_and_drive())

    print("\nYoung responsible person do:")
    print(young_responsible_person.drive())
    print(young_responsible_person.drink())
    print(young_responsible_person.drink_and_drive())

    age = 20
    person = RealPerson('Andrii', age)
    responsible_person = ProxyPerson('Yurii', age)

    print("\nPerson do:")
    print(person.drive())
    print(person.drink())
    print(person.drink_and_drive())

    print("\nResponsible person do:")
    print(responsible_person.drive())
    print(responsible_person.drink())
    print(responsible_person.drink_and_drive())


if __name__ == '__main__':
    main()
