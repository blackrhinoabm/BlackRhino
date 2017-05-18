



# -------------------------------------------------------------------------
#
#  class TestAgent
#
# -------------------------------------------------------------------------


class TestAgent():


    def print_info(self, text):

        print(text) 

        print 'XxxxxxXXxxxxXXXXxx'


    def get_parameters_from_file(self, args):

        import os
    	from src.environment import Environment 
        from src.agent import Agent	

        text = 'Calling test_agent_object.get_parameters_from_file(["configs/environment/", "test_firesales"]) to check whether the parameters for the agents are read correctly'

        self.print_info(text)

        #
        # Initialize Environment and give arguments
        #

        # we need to give environment config
        environment_directory = str(args[0])
        identifier = args[1]

        # calling the Environment Class  
        environment = Environment(environment_directory, identifier)

        # # get the agent_directory from the environment
        agent_directory = environment.agent_directory        
        # # and loop over all agents in the directorys
        listings = os.listdir(agent_directory)

        for file in listings:

            if 'agent1.xml' in file:
            # #
            # # TESTING
            # #

        # # test whether the parameters are read properly
                text = "Initiating agent object..\n"
                self.print_info(text)

                agent = Agent()
                environment.agents.append(agent)
                print agent

                text = "Reading in parameters by calling method..\n"
                self.print_info(text)

                agent_filename = agent_directory + file
                agent.get_parameters_from_file(agent_filename, environment)
                print agent











       



     

    # ----------------------------

