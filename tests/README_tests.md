DESCRIPTION OF TESTS

    # Tests for Bank
    test_bank.bank__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/banks
        the identifier is printed and can be checked against the file
    test_bank.bank__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/banks can be changed
        and prints the original and changed ("new_ident") identifiers
    test_bank.bank__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/banks
        and prints them out, these can be checked against the file
    test_bank.bank__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'rd': 0.44, 'rl': 0.55, 'active': 1}
    test_bank.bank__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/banks
        and prints them out, these can be checked against the file
    test_bank.bank__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test_bank.bank__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_bank helper function
    test_bank.bank__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/banks
    test_bank.bank__check_consistency([environment_directory, test_config_file, log_directory])
        Tests whether the function for checking whether assets are equal to liabilities
        performs correctly, it should give True first for the standard bank and then False
        after adding a one sided transaction
    test_bank.bank__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard bank in the helper class
    test_bank.bank__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard bank
        in the helper class
    test_bank.bank__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test_bank.bank__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of items and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_bank.bank__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_bank.bank__initialize_standard_bank([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard bank works
        and prints the standard bank for visual confirmation

    # Tests for Firm
    test_firm.firm__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/firms
        the identifier is printed and can be checked against the file
    test_firm.firm__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/firms can be changed
        and prints the original and changed ("new_ident") identifiers
    test_firm.firm__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/firms
        and prints them out, these can be checked against the file
    test_firm.firm__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'productivity': 1.55, 'active': 1}
    test_firm.firm__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/firms
        and prints them out, these can be checked against the file
    test_firm.firm__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test_firm.firm__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_firm helper function
    test_firm.firm__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/firms
    test_firm.firm__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard firm in the helper class
    test_firm.firm__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard firm
        in the helper class
    test_firm.firm__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test_firm.firm__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_firm.firm__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_firm.firm__initialize_standard_firm([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard firm works
        and prints the standard firm for visual confirmation

    # Tests for Household
    test_household.household__get_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the correct identifier has been read from the config file in tests/agents/households
        the identifier is printed and can be checked against the file
    test_household.household__set_identifier([environment_directory, test_config_file, log_directory])
        Tests whether the identifier read from the config file in tests/agents/households can be changed
        and prints the original and changed ("new_ident") identifiers
    test_household.household__get_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have been read from the file in tests/agents/households
        and prints them out, these can be checked against the file
    test_household.household__set_parameters([environment_directory, test_config_file, log_directory])
        Tests whether parameters have read from config can be overridden
        and prints the new values {'ps': 1.55, 'active': 1, 'labour': 8}
    test_household.household__get_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have been read from the file in tests/agents/households
        and prints them out, these can be checked against the file
    test_household.household__set_state_variables([environment_directory, test_config_file, log_directory])
        Tests whether state variables have read from config can be overridden
        and prints the new values {'test': 0.66}
    test_household.household__str([environment_directory, test_config_file, log_directory])
        Tests whether __str__ function works properly, the printout can be checked against
        the config in initialize_standard_household helper function
    test_household.household__get_parameters_from_file([environment_directory, test_config_file, log_directory])
        Tests whether the config file is read correctly, prints the identifier from
        the config file, which can be checked against the file in tests/agents/households
    test_household.household__get_account([environment_directory, test_config_file, log_directory])
        Tests whether get_account works properly, printing the values of various
        balance sheet items, which can be checked against standard household in the helper class
    test_household.household__get_account_num_transactions([environment_directory, test_config_file, log_directory])
        Tests whether get_account_num_transactions works, printing how many transactions
        of different types are in the balance sheet, to be checked against the standard household
        in the helper class
    test_household.household__add_transaction([environment_directory, test_config_file, log_directory])
        Tests whether a transaction can be added, and prints the balance sheet
        before and after adding the transaction, allowing for the comparison
    test_household.household__clear_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are cleared after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_household.household__purge_accounts([environment_directory, test_config_file, log_directory])
        Tests whether accounts are purged after using the appropriate function, and prints
        the number of itams and their value in the balance sheet at the beginning, after
        adding a worthless item and finally after calling the function
    test_household.household__initialize_standard_firm([environment_directory, test_config_file, log_directory])
        Tests whether the helper function for initializing a standard household works
        and prints the standard household for visual confirmation

    # Tests for Environment
    test_environment.environment__add_static_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether one can add a static parameter, should print the standard set of static
        parameters and then the same set with a 'test' parameter added with value 0.66
    test_environment.environment__add_variable_parameter(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether one can add a variable parameter, should print the standard set of variable
        parameters and then the same set with a 'test' parameter added with value range 0.66-0.77
    test_environment.environment__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the identifier of the environment, and prints it out
        should be the same as in the config file in tests/environments/
    test_environment.environment__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can change the identifier of the environment, and prints the
        original identifier, changes it to XYZ and prints the identifier again
    test_environment.environment__get_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get static parameters from the environment, and prints
        them out, they should be in line with the config file in tests/environments/
    test_environment.environment__set_static_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can set static parameters in the environment, first prints
        the original static parameters, changes them to {'test': 0.55}, and prints them again
    test_environment.environment__get_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get variable parameters from the environment, and prints
        them out, they should be in line with the config file in tests/environments/
    test_environment.environment__set_variable_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can set variable parameters in the environment, first prints
        the original variable parameters, changes them to {'test': 0.55-0.66}, and prints them again
    test_environment.environment__str(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether __str__ function works properly, the printout can be checked against
        the config file in tests/environments/
    test_environment.environment__print_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the parameters correctly, this prints the parameters
        read from the config file in tests/environments/
    test_environment.environment__write_environment_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can write the environment config file, it is written to the folder
        from which the function is originally called
    test_environment.environment__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can read an xml config file (/tests/environments/), and prints out
        the environment so it can be checked against the config file
    test_environment.environment__initialize(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the environment is properly initialized, and prints out the environment
        so it can be checked against the config file in tests/environments/
    test_environment.environment__initialize_banks_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether banks are properly initialized by the environment from config files saved in
        tests/agents/banks/, prints the number of banks expected and read and then prints the banks
    test_environment.environment__initialize_firms_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether firms are properly initialized by the environment from config files saved in
        tests/agents/firms/, prints the number of firms expected and read and then prints the firms
    test_environment.environment__initialize_households_from_files(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether households are properly initialized by the environment from config files saved in
        tests/agents/households/, prints the number of households expected and read and then prints the households
    test_environment.environment__get_agent_by_id(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the function fetches the agent by an ID (string). If it works correctly, it
        should print an agent with "bank_test_config_id" identifier. This depends on the agent of this
        identifier being in the /agents/ directory, from which the agents are initialized.
    test_environment.environment__read_transactions_for_banks(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the bank files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the banks with
        the transactions as specified in the config files within /agents/banks/.
    test_environment.environment__read_transactions_for_firms(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the firm files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the firms with
        the transactions as specified in the config files within /agents/firms/.
    test_environment.environment__read_transactions_for_households(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests wehther the transactions in the household files are read correctly. It first clears all the
        accounts and prints empty books, and then reads the accounts and should print the households with
        the transactions as specified in the config files within /agents/banks/.
    test_environment.environment__check_agent_homogeneity(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the check for agent homogeneity works for banks (parameter "banks"), first
        we create two standard banks and check if they are homogeneous (should return True), then
        change some parameter and check again (should return False)

    # Tests for Transaction
    test_transaction.transaction__init(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the initialization of a transaction works, and prints the ID of the
        initialized transaction, the assignment of which is all initialize does on Transaction.
    test_transaction.transaction__del(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can delete the transaction, prints whether it exists, deletes it, and
        then prints whether it exists again.
    test_transaction.transaction__get_type_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the type of the transaction and prints it (test_type).
    test_transaction.transaction__set_type_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the type of the transaction and prints it (test_type),
        then changes it (new_type) and prints it again.
    test_transaction.transaction__get_asset(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the asset of the transaction and prints it (test_asset).
    test_transaction.transaction__set_asset(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the asset of the transaction and prints it (test_asset),
        then changes it (new_asset) and prints it again.
    test_transaction.transaction__get_from_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the from of the transaction and prints it (test_from).
    test_transaction.transaction__set_from_(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the from of the transaction and prints it (test_from),
        then changes it (new_from) and prints it again.
    test_transaction.transaction__get_to(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the to of the transaction and prints it (test_to).
    test_transaction.transaction__set_to(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the to of the transaction and prints it (test_to),
        then changes it (new_to) and prints it again.
    test_transaction.transaction__get_amount(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the amount of the transaction and prints it (15).
    test_transaction.transaction__set_amount(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the amount of the transaction and prints it (15),
        then changes it (25) and prints it again.
    test_transaction.transaction__get_interest(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the interest of the transaction and prints it (0.01).
    test_transaction.transaction__set_interest(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the interest of the transaction and prints it (0.01),
        then changes it (0.02) and prints it again.
    test_transaction.transaction__get_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the maturity of the transaction and prints it (1).
    test_transaction.transaction__set_maturity(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the maturity of the transaction and prints it (1),
        then changes it (2) and prints it again.
    test_transaction.transaction__get_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the time_of_default of the transaction and prints it (1).
    test_transaction.transaction__set_time_of_default(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get and set the time_of_default of the transaction and prints it (1),
        then changes it (2) and prints it again.
    test_transaction.transaction__this_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can add values to the transaction all at once, and then prints the
        transaction, the attributes should be (type, asset, from, to, 1, 2, 3, 4) respectively.
    test_transaction.transaction__add_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can add a transaction to the books of agents automatically. Creates a
        transaction with attributes (type, asset, test_household, test_firm, 1, 2, 3, 4) and adds
        it to the books of the two agents automatically, after which it prints the books of these
        two agents.
    test_transaction.transaction__remove_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can remove a transaction from the books of agents automatically. At first
        it does the same as transaction__add_transaction but then it removes the transaction from
        the books of the two agents and prints these agents again.
    test_transaction.transaction__print_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test_transaction.transaction__str(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test_transaction.transaction__write_transaction(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the transaction properly. Prints the transaction from
        transaction__add_transaction in a nice xml format.
    test_transaction.transaction__clear_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can clear accounts of a bank properly, so it reflects the removal on the
        other party involved in the transaction as well. The test prints the accounts of banks
        and households, then clears the accounts of bank_test_config_id bank, printing the
        accounts of the aforementioned again, showing the appropriate transactions gone.
    test_transaction.transaction__purge_accounts(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether purging accounts works properly. Prints the books of test_household and
        test_firm which have a transaction with amount = 0. Then the accounts globally are purged
        and the two abovementioned agents are printed again, correctly not showing the transaction
        with amount = 0.

    # Tests for Helper
    test_helper.helper__initialize_standard_bank(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether initializing standard bank works properly. Initializes standard bank and then
        prints it to the screen. The standard bank should have three transactions on the books.
    test_helper.helper__initialize_standard_firm(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether initializing standard firm works properly. Initializes standard firm and then
        prints it to the screen. The standard firm should have three transactions on the books.
    test_helper.helper__initialize_standard_household(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether initializing standard household works properly. Initializes standard household and then
        prints it to the screen. The standard household should have three transactions on the books.
    test_helper.helper__cobb_douglas(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether C-D production function works. Calculates production for given
        parameters, should calculate production to be 2.93
    test_helper.helper__leontief(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether Leontief production function works. Calculates production for given
        parameters, should calculate production to be 2.5
    test_helper.helper__ces(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether CES production function works. Calculates production for given
        parameters, should calculate production to be 2.43
    test_helper.helper__translog(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether translog production function works. Calculates production for given
        parameters, should calculate production to be 13.74

    # Tests for Market
    test_market.market__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the identifier of the market, and prints it out
        should be printing "market_id"
    test_market.market__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the identifier as mentioned above can be changed
        and prints the original ("market_id") and changed ("new_market_id") identifiers
    test_market.market__get_tolerance(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the tolerance of the market, and prints it out
        should be printing 0.01
    test_market.market__set_tolerance(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the tolerance as mentioned above can be changed
        and prints the original (0.01) and changed (0.55) tolerances
    test_market.market__get_resolution(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the resolution of the market, and prints it out
        should be printing 0.01
    test_market.market__set_resolution(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the resolution as mentioned above can be changed
        and prints the original (0.01) and changed (0.55) resolutions
    test_market.market__get_amplification(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the amplification of the market, and prints it out
        should be printing 1.1
    test_market.market__set_amplification(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the amplification as mentioned above can be changed
        and prints the original (1.1) and changed (0.55) amplifications
    test_market.market__tatonnement(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether tatonnement finds appropriate price or labour. Should give roughly 50.666
    test_market.market__rationing(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether rationing finds appropriate pairs and transactions. Should return
        transactions amounting to 7, from agents 1 and 2 to agents 3 and 4. The final pairs
        may be different each run but the above conditions should be met.
    test_market.market__rationing_proportional(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether proportional rationing finds appropriate pairs and transactions. Should return
        transactions amounting to 7, from agents 1 and 2 to agents 3 and 4. Agent 1 should be selling
        2.91 while Agent 2 should be selling 4.08. The final pairs may be different each run
        but the above conditions should be met.
    test_market.market__rationing_proportional(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether abstract rationing finds appropriate pairs and transactions. First it looks
        at prioritising pairs with similar names. There it should return 'aaaaaa' > 'aaaabb' = 3
        'bbbbbb' > 'aabbbb' = 4, then it looks at prioritising pairs with dissimilar names and should
        return 'aaaaaa' > 'aabbbb' = 4 & 'bbbbbb' > 'aaaabb' = 3, finally again at the first version
        but not allowing 'aaaaaa' to trade with 'aaaabb', and should return 'aaaaaa' > 'aabbbb' = 4
        'bbbbbb' > 'aaaabb' = 3.

    # Tests for Measurement
    test_measurement.measurement__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the identifier of the measurement, and prints it out
        should be printing whatever is in the config file in /tests/ ("test_output")
    test_measurement.measurement__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the identifier as mentioned above can be changed
        and prints the original ("test_output") and changed ("new_measurement_id") identifiers
    test_measurement.measurement__get_config(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the config of the measurement, and prints it out
        should be printing whatever is in the xml config file in /tests/
    test_measurement.measurement__set_config(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the config as mentioned above can be changed
        and prints the original (as above) and changed ({'test': ['config']}) configs
    test_measurement.measurement__get_environment(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the environment of the measurement, and prints it out
        should be printing whatever is environment config specified
    test_measurement.measurement__set_environment(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the environment as mentioned above can be changed
        and prints the original (as above) and changed (we change it to Runner object) configs
    test_measurement.measurement__get_runner(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the runner of the measurement, and prints it out
        should be printing a src.runner.Runner object
    test_measurement.measurement__set_runner(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the runner as mentioned above can be changed
        and prints the original (as above) and changed (we change it to Environment object) configs
    test_measurement.measurement__get_filename(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the filename of the measurement, and prints it out
        should be printing whatever is in the measurement config in /tests/
    test_measurement.measurement__set_filename(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the filename as mentioned above can be changed
        and prints the original (as above) and changed (TestFilename.csv) filenames
    test_measurement.measurement__get_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the file of the measurement, and prints it out
        should be printing None in this instance, see the test below also
    test_measurement.measurement__set_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the file as mentioned above can be changed
        and prints the original (as above) and changed (open file object) filenames
    test_measurement.measurement__get_csv_writer(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the csv_writer of the measurement, and prints it out
        should be printing None in this instance, see the test below also
    test_measurement.measurement__set_csv_writer(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the csv_writer as mentioned above can be changed
        and prints the original (as above) and changed (_csv.writer object) filenames
    test_measurement.measurement__init(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can initialise the Measurement class instance properly
        and prints so initialised instance to the screen
    test_measurement.measurement__open_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can open a file in the measurement class and prints out
        the open file object
    test_measurement.measurement__write_to_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can write to the file opened above and it prints out the objects
        and their size before and after writing to the file
    test_measurement.measurement__close_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can close the file which we've been opening and writing to
        and prints whether the file is closed before and after closing it (should be False > True)
    test_measurement.measurement__read_xml_config_file(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can read the xml config file for the measurement saved in /tests/
        and writes the identifier, so it can be checked against the id in the config file

    # Tests for Runner # TODO: Tina

    # Tests for Updater
    test_updater.updater__get_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the identifier of the updater, and prints the current
        identifier, that is "test_model_id"
    test_updater.updater__set_identifier(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can change the previously set identifier and prints the previous
        identifier as above and a new identifier after the change ("new_model_id")
    test_updater.updater__get_model_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the model parameters of the updater, and prints the current
        model parameters, that is {"test": "model parameters"}
    test_updater.updater__set_model_parameters(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can change the previously set model_parameters and prints the previous
        model_parameters as above and a new model_parameters after the change
        i.e. {"new": "model parameters"}
    test_updater.updater__get_interactions(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can get the interactions of the updater, and prints the current
        interactions, that is None
    test_updater.updater__set_interactions(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can change the previously set interactions and prints the previous
        interactions as above and a new interactions after the change
        ["new", "interactions"]
    test_updater.updater__str(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can print the Updater, and prints an xml style string with
        the config of updater, in this case should only have identifier = "testing str"
    test_updater.updater__init(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can initialise the updater properly. As initialising the updater
        sets the appropriate environment this should print the environment
    test_updater.updater__accrue_interests(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can accrue interests. Should print a deposits transaction of the
        test household with value 10.0 and interest rate of 5%, accrue the interest, and
        then pprint the test household with deposits now at 10.5
    test_updater.updater__endow_labour(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can endow labour to the sweep_labour parameter, and prints the
        sweep_labour before endowment (0) and after endowment (see config file)
    test_updater.updater__sell_labour(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether selling endowed labour works well, prints the household with its
        accounts, then sells labour and prints it again. You should notice new labour and
        deposits transactions corresponding to the sell message above it.
    test_updater.updater__consume_rationed(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether consuming the produced goods works. Prints the household which is
        the same as at the end of the above test, then performs the consumptions, you should
        see the message, and then the printout of the household again, wich should have additional
        goods and loans transactions corresponding to the message
    test_updater.updater__net_loans_deposits(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can net loans and deposits. This should print out the household
        as it is at the end of the above test, performs netting the loans and deposits, and
        prints the household again. All the loans and deposits should now be in one transaction
        with value corresponding to sum of the previous loans and deposits.
    test_updater.updater__net_labour_goods(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether we can net labour and goods. This should print out the household
        as it is at the end of the above test, performs netting the labour and deposits, and
        prints the household again. All the labour and goods should now be in one transaction
        with value corresponding to sum of the previous labour and goods. Notice that goods and
        deposits have different prices (see messages in the tests above), and this is used
        in the netting.
    test_updater.updater__do_update(["tests/environments/", "test_all_methods", "tests/log/"])
        Tests whether the do_update loop works. Prints the household at the start of the
        update and then at the end. This should be equivalent to the 4 tests above.
