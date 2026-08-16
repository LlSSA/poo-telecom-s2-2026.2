class Person:
    def __init__(self, id_: int, name_: str):
        self.id = id_
        self.name = name_
    def __str__(self):
        return 'id: {}, name: {}' \
            .format(self.id, self.name)
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id_):
        if isinstance(id_, int):
            self.__id = id_
        else:
            raise ValueError('id must be an integer.')

    @property
    def name(self):
        return self.__qualname__
    @name.setter
    def name(self, name_):
        if isinstance(name_, str):
            self.__name = name_
        else:
            raise ValueError('name must be a string.')

if __name__ == '__main__':
    import shelve
    db = shelve.open('person.db')
    p1 = Person(1, 'Joseph')
    p2 = Person(2, 'Mary')
    print('Written objects')
    for p in (p1, p2):
        db[p.name] = p
        print(p)
    db.close()
    db = shelve.open('person.db')
    p3 = db['Mary']
    p4 = db['Joseph']
    print('Recovered objects')
    for p in (p3, p4):
        print(p)
    db.close()
        