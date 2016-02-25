DESCRIPTION OF TESTS

    # Tests for Bank
    test.bank__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/banks
        the identifier is printed and can be checked against the file
    test.bank__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/banks can be changed
        and prints the original and changed ("new_ident") identifiers
    test.bank__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/banks
        and prints them out, these can be checked against the file
    test.bank__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'rd': 0.44, 'rl': 0.55, 'active': 1}
    test.bank__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/banks
        and prints them out, these can be checked against the file
    test.bank__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test.bank__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_bank helper function
    test.bank__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/banks
    test.bank__check_consistency([environment_directory, test_config_file, log_directory])
        Tests whether the function for checking whether assets are equal to liabilities
        performs correctly, it should give True first for the standard bank and then False
        after adding a one sided transaction
    test.bank__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard bank in the helper class
    test.bank__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard bank
        in the helper class
    test.bank__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test.bank__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.bank__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.bank__initialize_standard_bank([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard bank works
        and prints the standard bank for visual confirmation

    # Tests for Firm
    test.firm__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/firms
        the identifier is printed and can be checked against the file
    test.firm__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/firms can be changed
        and prints the original and changed ("new_ident") identifiers
    test.firm__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/firms
        and prints them out, these can be checked against the file
    test.firm__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'productivity': 1.55, 'active': 1}
    test.firm__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/firms
        and prints them out, these can be checked against the file
    test.firm__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test.firm__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_firm helper function
    test.firm__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/firms
    test.firm__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard firm in the helper class
    test.firm__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard firm
        in the helper class
    test.firm__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test.firm__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.firm__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.firm__initialize_standard_firm([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard firm works
        and prints the standard firm for visual confirmation

    # Tests for Household
    test.household__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/households
        the identifier is printed and can be checked against the file
    test.household__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/households can be changed
        and prints the original and changed ("new_ident") identifiers
    test.household__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/households
        and prints them out, these can be checked against the file
    test.household__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'ps': 1.55, 'active': 1, 'labour': 8}
    test.household__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/households
        and prints them out, these can be checked against the file
    test.household__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test.household__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_household helper function
    test.household__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/households
    test.household__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard household in the helper class
    test.household__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard household
        in the helper class
    test.household__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test.household__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.household__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after 
        adding a worthless item and finally after calling the function
    test.household__initialize_standard_firm([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard household works
        and prints the standard household for visual confirmation

    # Tests for Environment
    test.environment__add_static_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether one can add a static parameter, should print the standard set of static
        parameters and then the same set with a 'test' parameter added with value 0.66
    test.environment__add_variable_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether one can add a variable parameter, should print the standard set of variable
        parameters and then the same set with a 'test' parameter added with value range 0.66-0.77
    test.environment__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the identifier of the environment, and prints it out
        should be the same as in the config file in tests/environments/
    test.environment__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can change the identifier of the environment, and prints the
        original identifier, changes it to XYZ and prints the identifier again
    test.environment__get_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get static parameters from the environment, and prints
        them out, they should be in line with the config file in tests/environments/
    test.environment__set_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can set static parameters in the environment, first prints
        the original static parameters, changes them to {'test': 0.55}, and prints them again
    test.environment__get_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get variable parameters from the environment, and prints
        them out, they should be in line with the config file in tests/environments/
    test.environment__set_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can set variable parameters in the environment, first prints
        the original variable parameters, changes them to {'test': 0.55-0.66}, and prints them again
    test.environment__str(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether __str__ function works properly, the printout can be checked against
        the config file in tests/environments/
    test.environment__print_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the parameters correctly, this prints the parameters
        read from the config file in tests/environments/
    test.environment__write_environment_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can write the environment config file, it is written to the folder
        from which the function is originally called
    test.environment__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can read an xml config file (/tests/environments/), and prints out
        the environment so it can be checked against the config file
    test.environment__initialize(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the environment is properly initialized, and prints out the environment
        so it can be checked against the config file in tests/environments/
    test.environment__initialize_banks_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether banks are properly initialized by the environment from config files saved in
        tests/agents/banks/, prints the number of banks expected and read and then prints the banks
    test.environment__initialize_firms_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether firms are properly initialized by the environment from config files saved in
        tests/agents/firms/, prints the number of firms expected and read and then prints the firms
    test.environment__initialize_households_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether households are properly initialized by the environment from config files saved in
        tests/agents/households/, prints the number of households expected and read and then prints the households
