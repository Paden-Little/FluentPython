# Defining 'Pythonic'
A 'Pythonic' class is one which implements dunder methods that apply to its context. These dunder method -- in the case 
of *FrenchDeck*, \_\_getitem\_\_ and \_\_len\_\_ -- exposes built-in functionality within the Python language. Allowing 
the langauge to treat your custom objects as fundamental types. 
## Basic Dunders
 - *\_\_len\_\_*:
   - Exposes *len()* functionality (TestChapter1.py:5)
 - *\_\_getitem\_\_*:
   - Exposes *[]* operator 
     - The *[]* operator allows:
       - single item retrival (TestChapter1.py:12)
       - slicing (TestChapter1.py:22)
       - use of many *\_\_getitem\_\_* implementors like *random.choice()* (TestChapter1.py:30)
   - Makes *FrenchDeck* iterable (TestChapter1.py:39)
   - Makes *FrenchDeck* sortable (TestChapter1.py:46)
 - *\_\_repr\_\_*:
   - Instances of Vector shown in the console will call this method instead of *<Vector object at 0x10e100070>*
     - Good practice is to represent the object as if you were calling its constructor. (Vector.py:10)
     - *\_\_repr\_\_* should differ from *\_\_str\_\_*, which is called by *str()*, its return should be suitable for the end user
     - Whenever no *\_\_str\_\_* is availible, python with call *\_\_repr\_\_* as a fallback
 - *\_\_add\_\_*, *\_\_sub\_\_*, and *\_\_mul\_\_*
   - These dunders allow our custom types to make use of +, -, * operators. 
   - Its important to note that the expectation of these dunders is to return a new instance of the type without altering either of the provided types