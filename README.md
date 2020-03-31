<img src="https://cogeorg.github.io/images/black_rhino_logo.jpg" height="64px"/>


[comment]: <> (One paragraph overview of the project, TODO add link to blog?)
**Black Rhino** is an open source easy-to-use-and-adapt 
economic/financial network multi-agent simulation (MAS) 
that serves two purposes. First, it can be used as a 
practical tool to simulate and analyse a model economic 
/ banking system. This is particularly handy for central 
banks and policy makers, as black_rhino fills a 
gap in the policy-toolbox. Second, it is a python module 
that can be easily adapted, changed, and modified for 
research purposes. It is intended to reduce the amount 
of work necessary to write an economic or financial MAS
 and hence allows researchers to focus on the economic 
 questions instead of worrying about code design patterns 
 and basic functionality. As such it may be particularly 
 useful for both experienced researchers as well as 
 graduate and PhD students.

[comment]: <> (Explain how to use the tool)
__Getting started__

First, you **install** Black Rhino using the following command in your command shell:

`   git clone https://github.com/cogeorg/black_rhino`

Alternatively, you can use github desktop to clone the repository on your system.
Once you have done so, you need to clone abm_template as well (submodule). Enter the following command 
in you command shell: 

`   git submodule update --init --recursive`

After that you are ready to start using Black Rhino.

__Using black_rhino__

First of all, you have to distinguish between a Python version based on Windows and a version based on Linux. Depending on your system you have to un/comment on statement in the main black_rhino start file. In order to execute black_rhino for Window you have to use
args=['./black_rhino.py',  "tests/environments/", "test_all_methods",  "tests/log/"]
while when using Linux the "args = sys.argv" has to be used. The respective other statement should be made inactive by marking it as a comment.

Usage:  
./black_rhino.py $environment_directory/ $environment_identifier $log_directory/  
Example:  
./black_rhino.py tests/environments/ test_all_methods tests/log/  

Even though black_rhino is intended to be easy to use and adapt, this does not make it entirely easy to use the first time. This section outlines the basic usage, a later section elaborates on the program's internal logic.

The environment file is the file that determines in which economic environment the simulation takes place. It is located in the environment_directory/ and denoted by the environment_identifier (e.g. test10) and without the .xml extension. All the parameters that are specific to the macroeconomy and the regulatory environment are stored here. Also, a number of parameters that are common to all banks (or firms, households, and the central bank) are collected in the environment file.

The first type of output that black_rhino generates are measurements and can be found in the measurement_directory/ specified in the config file for the environment. The contents of the measurement file are specified within the config file for measurement and also within the Measurement class itself. These are comma-separated files. The data have to be transformed into result files that can be plotted e.g. using gnuplot. I usually use R to read the histograms and create mean, std deviation, etc. and then gnuplot for the plotting itself. But of course you can also use R for plotting.

The other type of output is a log file, created in log_directory/ (typically log/) that is named $identifier.log and contains information about the run. The logfile is useful in many circumstances, as it will report a number of errors that could occur (e.g. through misusage or because a certain exception was triggered in the run) and also give information how long a run takes (which is very useful, as you can start a run with one simulation only and then extrapolate how long 1000 simulations would take).

Note that more details about specific files within black_rhino can be found within the files themselves as docstrings and code comments, as well as within the examples/ where you can see .docx documentation files.

__Contributing__
You can contribute to the repository by adding new models. This works as follows. 

__Disclaimer__

This software is intended for educational and research
purposes. Despite best efforts, 
we cannot fully rule out the possibility of errors and bugs. 
A number of tests are provided together with the software 
that aim to minimize this risk, but the use of black_rhino
 is entirely at your own risk.

Please note: black_rhino is published under the 
GNU GPL v3. If you are unsure about 
the implications, check the website of the Free Software Foundations.




The optimization behavior of agents is based on the Solow growth model, and described in principle in http://www.pitt.edu/~mgahagan/Solow.htm

Bank is only an intermediary in the exchange the labour for ownership of capital (when household sells labour they get a deposit financed by the loan given to the firm, when the firm sells goods they get a deposit financed by the loan given to the household, these are netted at the end of each simulation step; conversely the imbalance between trade of labour and goods is netted and represents the ownership of firm’s capital by household). We can’t start with zero capital for technical reasons (Cobb-Douglas production function gives zero for zero capital), so the config file has starting capital ownership of 30 monetary units (and corresponding loan/deposit structure of 30 monetary units). The household is endowed every step of the simulation with 24 units of labour. We fix the price of the good produced in the economy (perishable) to 10 units, the price of the labour is found through Walrasian auction based on Cobb-Douglas production function, maximisation of profits for firms, and utility for households given by ln(units_consumed)+ln(25-labour_sold). The details of the math involved will be found immediately below. This cycle runs the number of times specified and works as the original Solow model, so that is there is growth in capital accumulated, but it’s slowing down with time. The derivation of the supply and demand functions follow, which are instrumental to the way the model works. The price of goods (p) is fixed to 10, the price of labour (w) is found through Walrasian auction, there is a capital stock (c), and at equilibrium household sells some amount of labour (l), and the firm in turns produces some amount of goods (y) and sells them at price p. The household maximises utility given as:

U=ln⁡(y)+ln⁡(25-l)

Taking into account the production function (Cobb-Douglas):

y=α*l^β*c^γ

Maximum utility is given by:

(d/dl)ln⁡(α*l^β*c^γ)+ln⁡(25-l)=0

Which finds the demand function of the household as:

l=(25*w-c)/(2*w)

Firm maximises profits: π=yp-wl, or:

max(α*l^β*c^γ p-wl)

Which gives the firm’s supply of labour function as:

l=(w/(α*β*c^γ*p))^(1/(β-1))

After firms acquire labour as explain below they produce given the C-D production function, and attempt to sell all their stock (as the good is perishable, and the price is fixed). The household attempts to buy goods for the percentage of their wealth given by their propensity to consume (1 – propensity to save). As can be readily seen this step depends entirely on the step above, where labour was sold.

There is a very crude financial market too. Given that there is no maturity mismatch in this model (transactions have no maturity in the model), and that loans and deposits are the same in the model, there is no chance for an interbank lending market to arise. However, we have investments in assets specified within the config file, in which the banks may invest. Bank chooses the amount of investments to make based on the amount of deposits they have, given the leverage ratio of (investments+loans)/(deposits). The bank then invests in a portfolio of n assets giving the investment in these assets equal weights. These are financed by a central bank loan. The central bank gives loans as necessary without any restrictions in this model. This financial aspect can be easily removed or enhanced depending on the user's needs.

The above roughly specifies the update algorithm that describes how the system evolves from one state to another. This update algorithm is part of the class Updater and constitutes the main part of the model Dynamics. To simplify debugging, the updater is not called directly from __main__(), there rather is a class Runner which contains a runner.do_run() that is executed in a loop within __main__().

The runner does three things. First, it takes care of the actual update step by calling updater.do_update(). Second, it checks whether there is a Shock in the current update step. If so, class Shock can execute a shock (shocks can easily be expanded). And third, the runner takes care of the Measurements, implemented in class Measurement. At each update step, there will be a measurement of all the state variables, stored in a histogram that is written to the hard disk at the end of the run. For reference, measurement config file typically looks like this:

```xml
<measurement identifier='test_output'>
    <parameter type='filename' value='TestMeasurement.csv'></parameter>
    <parameter type='output' column='1' header='Step' value='current_step'></parameter>
    <parameter type='output' column='2' header='Deposits' value='household_deposits' ></parameter>
</measurement>
```

This structure ensures that the code is easier to debug and adapt. Details about the interface of each class can be found within the actual .py files.


__Test Your Code__

One of the most critical steps in developing extensions and modifications to black_rhino is writing tests. Typically, a researcher will try to avoid this "unecessary" step in the code development as no "new" results are being produced. New modifications to the code will only be accepted, however, if they are properly tested to ensure the integrity of the code. There are two types of tests: (extended) unit tests, and simulation tests. While unit tests ensure the proper functioning of a small piece of code, simulation tests are larger tests that simulate extreme economic conditions. The behavior and economic interpretation of the observables and hence the economic transmission channels of the model can be understood in these extreme situations.

Writing a number of unit tests serves two purposes and its relevance cannot be underestimated. First of all, only proper unit testing can ensure that the code does exactly what it is supposed to do. It will save you a lot of time later on if you write your test at the same time you write a modification and extension to black_rhino. Unit tests should be written frequently for smaller parts of codes and once these parts are individually tested, also for larger parts. The other important reason for using unit tests is that they guarantee that a routine (a method or a larger part of code) do exactly the same when they are refactorized. This becomes relevant if you refactorize for instance the interbank lending routines for higher speed (this is the innermost loop, where the simulation spends most of the time).

black_rhino has a separate program called ./black_rhino_tests.py that is used to execute individual tests. Useful example data is provided in the directory tests/. In tests/ a number of test files for different parts of the code (classes) is already provided. Of course, there could always be more tests and with future revisions of black_rhino further tests will be provided.
