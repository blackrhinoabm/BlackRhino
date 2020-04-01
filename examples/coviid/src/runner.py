from examples.coviid.src.agent import Agent
from src.measurement import Measurement
from src.updater import Updater
from examples.coviid.src.abm_template.baserunner import BaseRunner


class Runner():
    def __init__(self, environment):
        self.initialize(environment)

    def initialize(self, environment):
        self.identifier = environment.identifier
        self.num_sweeps = int(environment.static_parameters['num_sweeps'])
        self.updater = Updater(environment)

    def store_grid(environment):
        grid = []
        for r in range(environment.rows):
            grid_row = []
            for a in environment.agents[r]:
                if a.status == 'i1':
                    grid_row.append(2)
                elif a.status == 'i2':
                    grid_row.append(3)
                elif a.status == 'r':
                    grid_row.append(1)
                else:
                    grid_row.append(0)
            grid.append(grid_row)
        return grid

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        return super(Runner, self).set_identifier(value)

    def get_num_sweeps(self):
        return self.num_sweeps

    def set_num_sweeps(self, value):
        super(Runner, self).set_num_sweeps(value)

    def do_run(self, environment):
        # loop over all time steps and do the updating
        # For each update step
        measurement = Measurement(environment, self)
        measurement.open_file()

        for i in range(self.num_sweeps): #sweeps is time periods
            self.current_step = i
            self.updater.do_update(environment)
            measurement.write_to_file()

        print("***\nThis run had {}s sweeps and {}s simulations".format(self.num_sweeps, environment.static_parameters['num_simulations']))
        print("Check the output file that was written as csv in the measurements folder\n***")

        measurement.close_file()
