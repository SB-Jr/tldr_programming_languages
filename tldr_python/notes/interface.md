# Interfaces

Python has 2 ways of implementing interface:

- Informal Interface

- Formal Interface

## Informal Interface

In certain circumstances, you may not need the strict rules of a formal 
Python interface. Python’s dynamic nature allows you to implement an **informal interface**. An informal Python interface is a class that defines methods that can be overridden, but there’s no strict enforcement.

eg:

```python
class InformalInterface:
    def method1(a: int, b: str) -> str:
        pass
    def method2(a: str, b:str, c: str) -> str:
        pass
```

Here the above interface is basically a class and we are conveying the structure through argument hinting. Here when the SubClass implements this informal interface, it will basically extend it and this informal interface acts like a normal inheritance in python.

```python
class InheritedClass(InformalInterface):
    def method1(a: int, b: str) -> str:
        '''some implementation'''
```

Here `InheritedClass` is a concrete class which basically just extends our interface. So when we test the `issubclass` method on this 2 classes, it returns True.

```bash
>>> issubclass(InheritedClass, InformalInterface)
True
```

Thus informal Interface is basically Inheritance.

**Note: This is not the expected behavior when implementing an interface. If the implementing class doesn't implement all the interface then we should have a check mechanism to check this. In inheritance, if the subclass is not overriding a parent class method, the parent class method is invoked, and this should not happen when implementing an interface.** 

**Note: Interface cannot be instantiated but here there is no mechanism to stop us from instantiating the `InformalInterface` class.**

## Formal Interface

Ideally when implementing an interface we dont want the `issubclass` to return True when implementing class doesn't define all the methods of the interface.

To create a formal interface we need to use ABCs (Abstract Base Classes).

An ABC is simple as an interface or base classes define as an abstract 
class in nature and the abstract class contains some methods as 
abstract. Next, if any classes or objects implement or drive from these 
base classes, then theses bases classes forced to implements all those 
methods.

eg:

```python
from abc import ABC
from abc import abstractclassmethod

class FormalInterface(ABC):
    @abstractclassmethod
    def some_method():
        pass
```

Here we have used annotations to convey which methods has to be compulsorily implemented by a class if it inherits from this base class.

Here as the `FormalInterface` is inheriting from `ABC`, it can't be instantiated and any Class inheriting from `FormalInterface` cant be instantiated until it overrides the `some_method()` function in its definition.
