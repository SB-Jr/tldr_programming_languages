# Dart Basics
  
- Dart's main method is named `main()` or, if you need access to comand line arguments, `main(List<String> args)`.
- The `main()` method lives at the top level. In Dart, you can define code outside of classes. Variables, functions, getters, and setters can all live outside of classes.
- All identifiers are public by default. Dart doesn't have keywords for public, private, or protected.
- Dart uses two-character indentation by convention instead of four.
- Constructor for a class can be written without having a body. Dart follows a minimal way of writting methods.
- Remove the optional new keyword while creating instances.
- The `@override` annotation tells the analyzer that you are intentionally overriding a member. The analyzer raises an error if you failed to properly perform the override.
- Dart supports single or double quotes when specifying strings.
- Use string interpolation to put the value of an expression inside a string literal: `${expression}`. If the expression is an identifier, you can skip the braces: `$variableName`.
- Shorten one-line functions or methods using fat arrow `=>` notation.
eg:
<pre><code>
class A {
  int a;
  int b;
  int c;
  A(this.a, this.b, this.c);  //no body constructor
}

class B {

   @override
   String toString() => 'This is B';    //can use both '' or "" to denote string
}

void main() {  //using main outside any class definition
  var instA = A(1,2,4);  // instA is of type A here denoted using var
  print(instA);          //will output -> Instance of 'A'

  var instB = B();
  print(instB);          //will output -> "This is B"
}
</code></pre>
  
## Identifier Security
  
- To mark a Dart identifier as private to its library, start its name with an underscore `_`.<b>Library privacy generally means that the identifier is visible only inside the file (not just the class) that the identifier is defined in.</b>
- <b>Uninitialized variables (even numbers) have the value null.</b>
- By default, Dart provides implicit getters and setters for all public instance variables. You don't need to define your own getters or setters unless you want to enforce read-only or write-only variables, compute or verify a value, or update a value elsewhere.
- 