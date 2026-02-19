01. Classes and Objects: The Blueprint and the Building


• Class: Think of a class as a blueprint or a template. It defines what an objectwill be like – what data it will hold and what actions it can perform. It doesn’tcreate the object itself, just the instructions for creating it. It’s like anarchitectural plan for a house.



• Object (Instance): An object is a specific instance created from the classblueprint. If “Car” is the class, then your red Honda Civic is an object (aninstance) of the “Car” class. Each object has its own unique set of data. It’s likethe actual house built from the architectural plan.

02. The Constructor: Setting Things Up ( __init__ )


• The __init__ method is special. It’s called the constructor. It’s automatically run
whenever you create a new object from a class.


03. Inheritance: Building Upon Existing Classes


• Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes
and methods) from its parent class (or superclass). This allows you to create new
classes that are specialized versions of existing classes, without rewriting all the
code.


• super() : Inside a child class, super() lets you call methods from the parent
class. This is useful when you want to extend the parent’s behavior instead of
completely replacing it. It’s especially important when initializing the parent
class’s part of a child object.