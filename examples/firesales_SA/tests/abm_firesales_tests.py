# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':

    import pdb  # python debugger, for debugging purposes only

    import sys


    from inspect import getsourcefile
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(getsourcefile(lambda:0)) ) ) )
    
    from src.environment import Environment
    from TestAgent import TestAgent


    test_agent_object = TestAgent()  
    
    #test_agent_object.print_info("This tests methods for agent class")

    test_agent_object.get_parameters_from_file(["configs/environment/", "test_firesales"])



