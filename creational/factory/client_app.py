from creational.factory.factories.person_factory import PersonFactory


def main() -> None:
    """
    Client app
    """
    persons = list()
    pf = PersonFactory()
    persons.append(pf.create_person("Oleh"))
    persons.append(pf.create_person("Serhiy"))
    persons.append(pf.create_person("Yurii"))
    persons.append(pf.create_person("Taras"))
    persons.append(pf.create_person("Andrii"))

    for person in persons:
        print(person)


if __name__ == '__main__':
    main()
