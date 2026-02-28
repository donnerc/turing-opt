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

class QueueOverflowError(QueueException):
    pass





class ArrayQueue(QueueADT, Generic[T]):
    '''

    Implements a static array based queue

    >>> q = ArrayQueue(max_size=5)
    >>> q.enqueue(3)
    >>> q.enqueue(5)
    >>> q
    ArrayQueue(max_size=5, items=[3, 5])
    >>> len(q)
    2
    >>> for item in [7, 9, 11]: q.enqueue(item)
    >>> q
    ArrayQueue(max_size=5, items=[3, 5, 7, 9, 11])
    >>> q.enqueue(13)
    Traceback (most recent call last):
    ...
    QueueOverflowError: Cannot enqueue into full queue
    >>> q.first()
    3
    >>> q.dequeue()
    3
    >>> len(q)
    4
    >>> q
    ArrayQueue(max_size=5, items=[5, 7, 9, 11])
    >>> for _ in range(4): q.dequeue()
    5
    7
    9
    11
    >>> q
    ArrayQueue(max_size=5, items=[])
    >>> q.dequeue()
    Traceback (most recent call last):
    ...
    EmptyQueueError: Cannot dequeue from empty queue
    >>> q.first()
    Traceback (most recent call last):
    ...
    EmptyQueueError: Cannot get first element from empty queue
    >>> for n in range(2): q.enqueue(n)
    >>> q
    ArrayQueue(max_size=5, items=[0, 1])
    >>> q.is_empty()
    False
    >>> for _ in range(2): q.dequeue()
    0
    1
    >>> q
    ArrayQueue(max_size=5, items=[])
    >>> q.is_empty()
    True
    '''

    def __init__(self, max_size: int, items=None) -> None:
        self._items = items or [None] * max_size
        self._rear = 0
        self._front = 0
        self._size = 0
        self._max_size = max_size

    def __len__(self) -> int:
        return self._size
    
    def _shift_right(self, current_value):
        return (current_value + 1) % self._max_size

    def _add_item(self, item: T) -> None:
        self._items[self._rear] = item
        self._rear = self._shift_right(self._rear)
        self._size += 1
        
    
    def enqueue(self, item: T) -> None:
        if self._size < self._max_size:
            self._add_item(item)
        else:
            raise QueueOverflowError("Cannot enqueue into full queue")
        
    def dequeue(self) -> T:
        if self._size > 0:
            front_item = self._items[self._front]
            self._front = self._shift_right(self._front)
            self._size -= 1
            return front_item
        else:
            raise EmptyQueueError("Cannot dequeue from empty queue")
        
        
    def to_list(self) -> list[T]:
        if self._size == 0:
            return []
        elif self._front < self._rear:
            return self._items[self._front:self._rear]
        else:
            return self._items[:self._rear] + self._items[self._front:]
        
    def __repr__(self):
        items = self.to_list()
        return f'{self.__class__.__name__}(max_size={self._max_size}, items={items})'
    
    def first(self):
        if self._size > 0:
            return self._items[self._front]
        else:
            raise EmptyQueueError("Cannot get first element from empty queue")
            
    def is_empty(self) -> bool:
        return self._size == 0
            
class DynamicArrayQueue(ArrayQueue):
    '''
    >>> q = DynamicArrayQueue(max_size=3)
    >>> q._grow()
    >>> q
    DynamicArrayQueue(max_size=6, items=[])
    >>> q = DynamicArrayQueue(max_size=3)
    >>> for x in [2, 4, 6]: q.enqueue(x)
    >>> q._max_size == 3
    True
    >>> q.enqueue(10)
    >>> q
    DynamicArrayQueue(max_size=6, items=[2, 4, 6, 10])
    '''
    #def __init__(self, max_size: int, items=None) -> None:
    #    super().__init__(max_size, items)

    def _grow(self):
        new_max_size = self._max_size * 2

        new_items = [None] * new_max_size

        # copy element from old array to new array
        for new_index in range(self._size):
            old_index = (self._front + new_index) % self._max_size
            new_items[new_index] = self._items[old_index]

        self._items = new_items

        self._front = 0
        self._rear = self._size

        self._max_size = new_max_size

    def enqueue(self, item: T) -> None:
        if self._size < self._max_size:
            self._add_item(item)
        else:
            self._grow()
            self.enqueue(item)

if __name__ == '__main__':
    import doctest
    doctest.testmod()