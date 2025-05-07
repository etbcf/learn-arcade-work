1. What are the three main advantages of object-oriented programming?

One, we can group multiple variables together in a single record. Two, we can associate
functions with that group of data. Three, we can use something called inheritance which
allows us to take a base set of code and extend it, without needing to rewrite it from scratch.

2. What keyword is used to define a new class?

We use the **class** keyword.

3. All class names should start with an upper-case or lower-case letter?

Unlike variables, all class names should start with a capital letter. While you can use a
lower-case variable, you never should. Following this pattern of lower-case for variables
and upper-case for classes makes it easy to tell which is which.

4. Where do the comments for a class go? What kind of comments do you use? Why is there a standard?

They go right after the class definiton.
We normally put them into triple-quote comment syntax. They are called Docstrings.

The cool feature about creating comments this way, is the text can be pulled out
automatically to form a website for your API documentation. It is a consistent way and have the following benefits:

- Make code easier to read and maintain;
- Allow tools like Sphinx, pydoc, or IDEs to generate documentation automatically;
- Help teams or future developers understand what each class or method is for without reading every line of code.

5. What is the difference between a function and a method?

**Functions**
- A function is a block of reusable code that performs a specific task;
- It is not bound to an object or class;
- It is declared using the **def** keyword and it's called independently.

**Methods**
- Methods are functions in a class;
- Methods are automatically called and they are set like this **__init__, __repr__, or __str__** inside of a class;

6. What three different terms can be used to refer to data that is tied to a a class?

- Instance variables;
- Attributes;
- Fields.

7. What is a magic method?

Magic method, are methods that are automatically called.

8. What is a dunder method?

A dunder method is a name to refer to the double undercores that makes up a magic method.

9. All class methods should have start with the same parameter. What is that parameter?

That parameter is **self**.

10. What is the name of the method in a class where we define our attributes?

It is the **constructor**.

11. When defining a class attribute, what needs to go right before it?

The **self** parameter.

12. What is a constructor?

A constructor in object-oriented programming is a special method that is automatically called
when you create a new instance of a class.

13. What is the difference between a class and an object?

Let's say we have a Person and Samantha, the Person would be the class and Samantha the object.

14. What are the common mistakes when creating instances (objects) of a class?

The first common mistake when creating an object is to forget the parentheses:

```
# ERROR - Forgot the parentheses after Address
home_address = Address
```
Another very common mistake when working with classes is to forget to specify which instance
of the class you want to work with.

15. How can we make sure our attributes are assigned when the object is created?

We can add a parameter to our constructor, so that it requires us to pass in a name for the object.

16. What is the point of adding “typing” to a class?

It allows a programmer to use a tool like mypy and catch errors earlier in the development process.

17. What is a data class?

Think of a dataclass like a pre-built mold for making cookies. Normally, you'd have to shape each 
cookie by hand (writing your own __init__, __repr__, etc.), but with a dataclass, you just define
what ingredients (fields) go in, and Python handles shaping them into cookies
(creating the boilerplate methods) for you.

18. What are static variables?

Variables that don’t change for each instance of a class, are called class variables or static variables.

You refer to a static variable by using the class name Cat rather than any of the instance names like cat1.
