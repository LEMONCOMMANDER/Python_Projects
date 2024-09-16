This is a follow along with a free code camp video: https://www.youtube.com/watch?v=cHYq1MRoyI0

the goal is to learn pytest on a basic level to implement with selenium scripts. The scope of this video seems to focus on pytest,
but the skills will be trasnlatalbe. All important or large notes will direct to the read me, notes section below:


-------------------------------------------------- NOTES --------------------------------------------------
style: note #,  source (source file ): info
--------------------------------------------------
-------------------------------------------------- GENERAL NOTES
NOTE 1: pytest
-v is an extended view 
-s will enable/disable print statements


-------------------------------------------------- VIDEO NOTES
NOTE 2, my_functions_test.py: information on "assert" in pytest and errors. Basic structures of pytest syntax 
    video chapter - "Our First Tests" 

NOTE 3, class_based.py: created a new file to address video 2, class based testing at 19:28 ***
    uses class_based.py in "source" and circle_test.py in "tests" 

    Worth looking up how classes work in greater detail. the class Circle has 2 parameters, self and radius. 
    When defining the first instance, we called the variable name of that instance self.circle --> which explains some of the references
        in the code   

NOTE 4, fixture_based.py: focusing on fixtures - I am again going to copy all new files for this one 
    uses fixture_based.py in "source" and rectangle_test.py | video chapter "Fixtures" at 24:49

    "In testing, a fixture provides a defined, reliable and consistent context for the tests. 
        This could include environment (for example a database configured with known parameters) or content (such as a dataset).
        In pytest, they are functions you define that serve this purpose."
           
          --  https://docs.pytest.org/en/stable/explanation/fixtures.html#about-fixtures

    Fixtures can be scoped or global - global fixtures can be shared amongst all tests in a directory. To do this, a new doc called
    "conftest.py" is required - pytest will automatically detect fixtures in this document