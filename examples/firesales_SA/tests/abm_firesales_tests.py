# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':

    import pdb  # python debugger, for debugging purposes only

    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    
    from src.environment import Environment
    from tests.TestAgent import TestAgent


    test_agent_object = TestAgent()  
    
    test_agent_object.print_info("This tests methods for agent class")

    test_agent_object.get_parameters_from_file(["configs/environment/", "test_firesales"])
