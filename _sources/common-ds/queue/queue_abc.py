from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class QueueADT(ABC, Generic[T]):

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Enfile un nouvel objet dans la file"""
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """Défile le premier objet de la file"""
        pass

    @abstractmethod
    def first(self) -> T:
        """Retourne le premier élément de la file sans le défiler"""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Retourne ``True`` si la liste est vide et ``False`` sinon"""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Retourne le nombre d'éléments de la file"""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Retourne la représentation interne de la file"""
        pass


class QueueException(Exception):
    pass


class EmptyQueueError(QueueException):
    pass


class QueueOverflowError(QueueException):
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
