from creational.factory.person import Person


class PersonFactory:
    """
     Simple Factory is used to create a specific type of product (object).
     """
    id_iterator = 0

    @staticmethod
    def create_person(name: str) -> Person:
        person = Person(PersonFactory.id_iterator, name)
        PersonFactory.id_iterator += 1
        return person
