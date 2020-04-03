from examples.coviid.src.abm_template.basemeasurement import BaseMeasurement


class Measurement(BaseMeasurement):
    identifier = ""
    # this we need to tell python measurment is passing in objects
    environment = type('', (), {})()
    runner = type('', (), {})()
    filename = ""
    config = {}
    file = None
    csv_writer = None

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        super(Measurement, self).set_identifier(identifier)

    def get_config(self):
        return self.config

    def set_config(self, config):
        super(Measurement, self).set_config(config)

    def get_environment(self):
        return self.environment

    def set_environment(self, environment):
        super(Measurement, self).set_environment(environment)

    def get_runner(self):
        return self.runner

    def set_runner(self, runner):
        super(Measurement, self).set_runner(runner)

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        super(Measurement, self).set_filename(filename)

    def get_file(self):
        return self.file

    def set_file(self, file):
        super(Measurement, self).set_file(file)

    def get_csv_writer(self):
        return self.csv_writer

    def set_csv_writer(self, csv_writer):
        super(Measurement, self).set_csv_writer(csv_writer)

    def __init__(self, environment, runner):
        super(Measurement, self).__init__(environment, runner)

    def open_file(self):
        super(Measurement, self).open_file()

    def write_to_file(self):
        super(Measurement, self).write_to_file()

    def close_file(self):
        super(Measurement, self).close_file()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # Read the xml config file specifying the config file
    # which is a list of lists
    # We need to specify the filename
    # We also need to specify each output:
    # - type: 'output'
    # - column: integer specifying which column will be used for this
    # - header: string written as header in the csv file in the column
    # - value: string or number, identifier for the wrapper function
    # specifying what the wrapper function returns
    # Thus:
    # {column_number: [header, output, wrapper_id],...:[...]]
    # [int: [string, string, string],...:[...]]
    #
    # Now we pass this on to the Measurement class through an xml file
    # which should look like this
    #
    # <measurement identifier='output_identifier'>
    #     <parameter type='filename' value='TestMeasurement.csv'></parameter>
    #     <parameter type='output' column='1' header='Step' value='current_step'></parameter>
    #     <parameter type='output' column='2' header='Deposits' value='column2_head' ></parameter>
    # </measurement>
    #
    # -------------------------------------------------------------------------
    def read_xml_config_file(self, config_file_name):
        super(Measurement, self).read_xml_config_file(config_file_name)
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # wrapper(self, id)
    # Wrapper for functions returning the desired values to be written
    # -------------------------------------------------------------------------

    def wrapper(self, ident):
        if ident == "current_step":
            return self.runner.current_step + 1

        if ident == "a1_opinion_after_current_step":
            for agent in self.environment.agents:
                if agent.identifier == 'agent_one':
                    return agent.opinion

        if ident == "a2_opinion_after_current_step":
            for agent in self.environment.agents:
                if agent.identifier == 'agent_two':
                    return agent.opinion

        if ident == "a3_opinion_after_current_step":
            for agent in self.environment.agents:
                if agent.identifier == 'agent_three':
                    return agent.opinion
