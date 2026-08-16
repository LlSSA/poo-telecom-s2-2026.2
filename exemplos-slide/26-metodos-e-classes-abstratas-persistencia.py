from abc import ABC, abstractmethod
import shelve
from shelve import DbfilenameShelf

class Serializable(ABC):
    @abstractmethod
    def save(self, db_: DbfilenameShelf):
        pass
    @abstractmethod
    def load(self, id_:str, \
             db_:DbfilenameShelf):
        pass

class Person(Serializable):
    def __init__(self, id_:str, name_: str):
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
        if isinstance(id_, str):
            self.__id = id_
        else:
            raise ValueError('id must be an integer.')
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if isinstance(name_, str):
            self.__name = name_
        else:
            raise ValueError('name must be a string.')
    def save(self, db_: DbfilenameShelf):
        if isinstance(db_, DbfilenameShelf):
            db_[self.id] = self
        else:
            raise ValueError('db must be a shelve db')
        def load(self, id_: str, db_: DbfilenameShelf):
            if isinstance(db_, DbfilenameShelf):
                if isinstance(id_, str):
                    obj = db_[id_]
                    self.id = obj.__id
                    self.name = obj.__name
                else:
                    raise ValueError('db must be a shelve db.')


    if __name__=='__main__':

        p1 = Person('p1', 'Joseph')
        p2 = Person('p2', 'Mary')
        persons = [p1, p2]

        persons_ids = [p2.id, p1.id]

        db = shelve.open('person.db')
        print('Stored objects')
        for p in persons:
        p.save(db)
        68 print(p)
        db.close()

        db = shelve.open('person.db')
        print('Recovered objects')
        i = 0
        for k in persons_ids:
            persons[i].load(k, db)
            print(persons[i])
            i += 1
        db.close()