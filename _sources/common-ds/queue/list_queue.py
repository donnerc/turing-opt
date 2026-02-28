from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class QueueADT(ABC, Generic[T]):

    @abstractmethod
    def enqueue(self, item: T) -> None:
        '''Enfile un nouvel objet dans la file'''
        pass
    
    
    @abstractmethod
    def dequeue(self) -> T:
        '''Défile le premier objet de la file'''
        pass
    
    
    @abstractmethod
    def first(self) -> T:
        '''Retourne le premier élément de la file sans le défiler'''
        pass
    

    @abstractmethod
    def is_empty(self) -> bool:
        '''Retourne ``True`` si la liste est vide et ``False`` sinon'''
        pass


    @abstractmethod
    def __len__(self) -> int:
        '''Retourne le nombre d'éléments de la file'''
        pass


    @abstractmethod
    def __repr__(self) -> str:
        '''Retourne la représentation interne de la file'''
        pass

class QueueException(Exception):
    pass

class EmptyQueueError(QueueException):
    pass


class ListQueue(QueueADT, Generic[T]):
    '''
    Implements a queue ADT by storing the elements in a list

    >>> queue: ListQueue[int] = ListQueue()
    >>> queue.enqueue(3)
    >>> queue.enqueue(5)
    >>> queue
    [3, 5]
    >>> len(queue)
    2
    >>> queue.first()
    3
    >>> queue.dequeue()
    3
    >>> queue
    [5]
    >>> queue.dequeue()
    5
    >>> queue
    []
    >>> queue.dequeue()
    Traceback (most recent call last):
    ...
    EmptyQueueError: dequeue from empty queue
    '''

    def __init__(self) -> None:
        self._items = []

    def enqueue(self, item: T) -> None:
        '''Enfile un nouvel objet dans la file'''
        self._items.append(item)
    
    
    def dequeue(self) -> T:
        '''Défile le premier objet de la file'''
        if self.is_empty():
            raise EmptyQueueError("dequeue from empty queue")
        else:
            return self._items.pop(0)


    def first(self) -> T:
        '''Retourne le premier élément de la file sans le défiler'''
        if self.is_empty():
            raise EmptyQueueError("illegal first element in empty queue")
        else:
            return self._items[0]
    

    def is_empty(self) -> bool:
        '''Retourne ``True`` si la liste est vide et ``False`` sinon'''
        return len(self) == 0


    def __len__(self) -> int:
        '''Retourne le nombre d'éléments de la file'''
        return len(self._items)


    def __repr__(self) -> str:
        '''Retourne la représentation interne de la file'''
        return repr(self._items)


if __name__ == '__main__':
    import doctest
    doctest.testmod()