---
layout: post
title: The Solow model
subtitle: An agent-based version of the famous Solow growth model
---

This post provides an example of the Solow growth model in the Black Rhino package. It will first cover the Solow model itself and how it is implemented in Black Rhino. Then, it will cover how to use Black Rhino to actually run the model and analyse the results.

## The model

The [Solow (1956)](https://www.jstor.org/stable/pdf/1884513.pdf) growth model is a model of long-run economic growth. It explains long run economic growth as a function of capital accumulation, labour, and productivity. This is an agent-based version of that model. It contains one firm agent and one household agent. These are presentative of the broader firm and household sector. There is also a Bank agent, but it is only there as an intermediary to exchange the labour for ownership of capital (when household sells labour they get a deposit financed by the loan given to the firm, when the firm sells goods they get a deposit financed by the loan given to the household, these are netted at the end of each simulation step; conversely the imbalance between trade of labour and goods is netted and represents the ownership of firm’s capital by household).



The price of the labour is found through Walrasian auction based on Cobb-Douglas production function, maximisation of profits for firms, and utility for households given by $$ln(units_consumed)+ln(25-labour_sold)$$. The details of the math involved will be found immediately below, the technical side of the simulator will be found in the sections further down. This cycle runs the number of times specified and works as the original Solow model, so that is there is growth in capital accumulated, but it’s slowing down with time. The derivation of the supply and demand functions follow, which are instrumental to the way the model works. The price of goods (p) is fixed to 10, the price of labour (w) is found through Walrasian auction, there is a capital stock (c), and at equilibrium household sells some amount of labour (l), and the firm in turns produces some amount of goods (y) and sells them at price p. The household maximises utility given as:

The model contains a single equation that explains long-run economic output $$Y$$ as a function of capital accumulation $$K$$, labour $$L$$, and productivity.

$$ \alpha + 2$$

The model is set within the framework of neoclassical economics. It is essentially a

It attempts to explain long-run economic growth by looking at capital accumulation, labor or population growth, and increases in productivity, commonly referred to as technological progress. At its core is a neoclassical (aggregate) production function, often specified to be of Cobb–Douglas type, which enables the model "to make contact with microeconomics".[1]:26 The model was developed independently by Robert Solow and Trevor Swan in 1956,[2][3][note 1] and superseded the Keynesian Harrod–Domar model.

## Configuring the model

In the Black Rhino framework, parameters are stored in xml files. Using this notebook, you can set change them. First, you need to import the elementree from the xml Python module.

```python
import xml.etree.ElementTree as ET
```

Then, the parameters for the model need to be defined. We can’t start with zero capital because the Cobb-Douglas production function gives zero for zero capital. Therefore, the model is initialized with capital ownership of 30 monetary units (and corresponding loan/deposit structure of 30 monetary units). The household is endowed every step of the simulation with 24 units of labour. We fix the price of the good produced in the economy (perishable) to 10 units.


Below you will find the parameter inputs for this model.  

```python
parameter_values = (('num_sweeps', '30'),
                    ('num_simulations', '1'),
                    ('num_banks', '1'),
                    ('num_firms', '1'),
                    ('num_households', '1'),
                    ('bank_directory', 'agents/banks/'),
                    ('firm_directory', 'agents/firms/'),
                    ('household_directory', 'agents/households'),
                    ('measurement_config', 'measurements/test_output.xml')
                   )
```

To translate this to an xml document, which the framework can read, we first need create an ET element.

```python
environment = ET.Element('environment')
```

And create parameter elements and give them the values seen below to add to the tree object.


```python
parameters = []
for x in range(len(parameter_values)):
    parameters.append(ET.SubElement(environment, 'parameter'))

for idx, p in enumerate(parameters):
    p.set('type', 'static')
    p.set('name', parameter_values[idx][0])
    p.set('value', parameter_values[idx][1])
```

This object can now be transformed to a string and written to an xml file using the code below.

```python
xml_params = ET.tostring(environment, encoding="unicode")
myfile = open("environments/solow_parameters.xml", "w")
myfile.write(xml_params)
myfile.close()
```

Now, the parameter xml file has been generated and the model can be run. Before, running the model, you need to import a couple of extra modules. These are the Python logging module, the Black Rhino environment class, and the Black Rhino runner class.

```python
import logging
import os
from src.environment import Environment
from src.runner import Runner
```

Then, before running the model, the logger needs to be initialized.

```python
log_directory = "log/"
identifier = "test_all_methods"
environment_directory = "environments/"
if not os.path.exists('log'):
    os.makedirs('log')
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                    filename=log_directory + identifier + ".log", level=logging.INFO)
logging.info('START logging for run: %s',  environment_directory + identifier + ".xml")
```

First, the environment will be initialized. It contains the model parameters and variables. The environment also contains a list of agents. In the Solow model, the environment contains one bank, one firm, and one household. Finally, it also contains initialized transactions for these agents.

```python
environment = Environment(environment_directory, identifier)
```

Next up, the runner object is created. As the name suggests, the runner object handles the running of the model. But that is not all, it also initializes the updater.

```python
runner = Runner(environment)
```

Now you can actually run the model. Since the agent-based model is simulated using Monte Carlo methods. This means that the model will be run multiple times (num_simulations). For every simulation run, the environment and runner will be (re-)initialized. Then, the runner will run the Solow model. During the run, the runner will write data about capital to a csv file specified within the Measurement class and print out all the transactions happening and the books of firm and household at the end of each sweep.


```python
for i in range(int(environment.num_simulations)):
    logging.info('  STARTED with run %s',  str(i))
    environment.initialize(environment_directory,  identifier)
    runner.initialize(environment)

    runner.do_run(environment)
    logging.info('  DONE')
```

So, now the model has been run, you will be able to analyse its outputs. If you are running the Ipython notebook to run the model. The following command will set the notebook to depict the output inside the notebook.


```python
%matplotlib inline
```

Furthermore, you should import the modules to create graphs (matplotlib) and data frames (pandas).


```python
import pandas as pd
import matplotlib.pyplot as plt
```

Running the model has generated a csv file that contains its output. We can use pandas to read the csv.


```python
solow_data = pd.read_csv('measurements/TestMeasurement.csv', index_col=0)
```

The datafame looks as follows:


```python
solow_data.head(3)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Deposits</th>
    </tr>
    <tr>
      <th>Step</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>60.105832</td>
    </tr>
    <tr>
      <th>2</th>
      <td>101.668774</td>
    </tr>
    <tr>
      <th>3</th>
      <td>152.021609</td>
    </tr>
  </tbody>
</table>
</div>


The Solow growth model is expected to produce an increase in total wealth that slows over time. In this version of the model, this means that there is deposit growth until the equilibrium is reached. This is exactly what we observe.


```python
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,6))

ax.plot(solow_data.index, solow_data)
ax.set_xlabel('Time', fontsize='14')
ax.set_ylabel('Capital', fontsize='14')

fig.savefig('solow_capital.png')
```

![png](../img/output_29_0.png)

This was an example of how to run one configuration of this model. The Black Rhino examples/solow folder contains three seperate notebooks for each of the elements of configuring the model, running the model, and analysing the results. For more advanced use, we recommend using these notebooks to run the model.
