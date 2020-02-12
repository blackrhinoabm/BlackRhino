---
layout: page
title: New models
subtitle: How to contribute to Black Rhino.
---

This section provides a tutorial of how you can add new models to Black Rhino.

### Test your code

One of the most critical steps in developing extensions and modifications to black_rhino is writing tests. Typically, a researcher will try to avoid this "unecessary" step in the code development as no "new" results are being produced. New modifications to the code will only be accepted, however, if they are properly tested to ensure the integrity of the code. There are two types of tests: (extended) unit tests, and simulation tests. While unit tests ensure the proper functioning of a small piece of code, simulation tests are larger tests that simulate extreme economic conditions. The behavior and economic interpretation of the observables and hence the economic transmission channels of the model can be understood in these extreme situations.

Writing a number of unit tests serves two purposes and its relevance cannot be underestimated. First of all, only proper unit testing can ensure that the code does exactly what it is supposed to do. It will save you a lot of time later on if you write your test at the same time you write a modification and extension to black_rhino. Unit tests should be written frequently for smaller parts of codes and once these parts are individually tested, also for larger parts. The other important reason for using unit tests is that they guarantee that a routine (a method or a larger part of code) do exactly the same when they are refactorized. This becomes relevant if you refactorize for instance the interbank lending routines for higher speed (this is the innermost loop, where the simulation spends most of the time).

black_rhino has a separate program called ./black_rhino_tests.py that is used to execute individual tests. Useful example data is provided in the directory tests/. In tests/ a number of test files for different parts of the code (classes) is already provided. Of course, there could always be more tests and with future revisions of black_rhino further tests will be provided.
