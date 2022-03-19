# Fl-Python-Typing
Shadows for Python's typing modules, so that statically typed scripts can be run
within FL Studio's Python environment without import errors.

# Setup

1. Copy the cloning URL as if you are going to `git clone` the project
2. Instead of running `git clone <url>`, cd into your project's directory and
   run `git submodule add <url>`
3. Run a `git commit` to commit the submodule
4. Add the typing module to Python's path by adding `import fl_typing` to the
   start of your `device_.py` files
5. You should be able to import and use static typing features in FL Studio
   without any issues.

# Note

These modules aren't exact replicas of the Python standard library originals -
they do absolutely nothing during runtime, and thus can't be used to access
module functions during runtime, except in cases where those functions do
nothing anyway.
