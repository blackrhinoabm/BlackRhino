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
    test.environment__get_agent_by_id(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the function fetches the agent by an ID (string). If it works correctly, it
        should print an agent with "bank_test_config_id" identifier. This depends on the agent of this
        identifier being in the /agents/ directory, from which the agents are initialized.
    test.environment__read_transactions_for_banks(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the bank files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the banks with
        the transactions as specified in the config files within /agents/banks/.
    test.environment__read_transactions_for_firms(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the firm files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the firms with
        the transactions as specified in the config files within /agents/firms/.
    test.environment__read_transactions_for_households(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the household files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the households with
        the transactions as specified in the config files within /agents/banks/.
    test.environment__check_global_transaction_balance(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the check for global balance for a transaction type

    # Tests for Transaction
    test.transaction__init(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the initialization of a transaction works, and prints the ID of the
        initialized transaction, the assignment of which is all initialize does on Transaction.
    test.transaction__del(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can delete the transaction, prints whether it exists, deletes it, and
        then prints whether it exists again.
    test.transaction__get_type_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the type of the transaction and prints it (test_type).
    test.transaction__set_type_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the type of the transaction and prints it (test_type),
        then changes it (new_type) and prints it again.
    test.transaction__get_asset(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the asset of the transaction and prints it (test_asset).
    test.transaction__set_asset(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the asset of the transaction and prints it (test_asset),
        then changes it (new_asset) and prints it again.
    test.transaction__get_from_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the from of the transaction and prints it (test_from).
    test.transaction__set_from_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the from of the transaction and prints it (test_from),
        then changes it (new_from) and prints it again.
    test.transaction__get_to(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the to of the transaction and prints it (test_to).
    test.transaction__set_to(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the to of the transaction and prints it (test_to),
        then changes it (new_to) and prints it again.
    test.transaction__get_amount(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the amount of the transaction and prints it (15).
    test.transaction__set_amount(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the amount of the transaction and prints it (15),
        then changes it (25) and prints it again.
    test.transaction__get_interest(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the interest of the transaction and prints it (0.01).
    test.transaction__set_interest(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the interest of the transaction and prints it (0.01),
        then changes it (0.02) and prints it again.
    test.transaction__get_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the maturity of the transaction and prints it (1).
    test.transaction__set_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the maturity of the transaction and prints it (1),
        then changes it (2) and prints it again.
    test.transaction__get_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the time_of_default of the transaction and prints it (1).
    test.transaction__set_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the time_of_default of the transaction and prints it (1),
        then changes it (2) and prints it again.
    test.transaction__this_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can add values to the transaction all at once, and then prints the
        transaction, the attributes should be (type, asset, from, to, 1, 2, 3, 4) respectively.
    test.transaction__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can add a transaction to the books of agents automatically. Creates a
        transaction with attributes (type, asset, test_household, test_firm, 1, 2, 3, 4) and adds
        it to the books of the two agents automatically, after which it prints the books of these
        two agents.
    test.transaction__remove_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can remove a transaction from the books of agents automatically. At first
        it does the same as transaction__add_transaction but then it removes the transaction from
        the books of the two agents and prints these agents again.
    test.transaction__print_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test.transaction__str(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test.transaction__write_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test.transaction__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can clear accounts of a bank properly, so it reflects the removal on the
        other party involved in the transaction as well. The test prints the accounts of banks
        and households, then clears the accounts of bank_test_config_id bank, printing the
        accounts of the aforementioned again, showing the appropriate transactions gone.
    test.transaction__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether purging accounts works properly. Prints the books of test_household and
        test_firm which have a transaction with amount = 0. Then the accounts globally are purged
        and the two abovementioned agents are printed again, correctly not showing the transaction
        with amount = 0.