This file specifies the parameters used in Black Rhino: Mika, their economic interpretation, and the way in which they are introduced and changed.

[] denotes an instance

[bank].interest_rate_loans                          interest rate per iteration on bank loans                                 updating
[bank].interest_rate_deposits                       interest rate per iteration on deposits                                   updating
[bank].target_leverage                              target leverate ratio of the bank                                         updating
[central_bank].interest_rate_cb_loans               interest rate per iteration on central bank loans                         updating
[firm].total_factor_productivity                    total factor productivity in Cobb-Douglas production function             updating
[firm].labour_elasticity                            labour elasticity in Cobb-Douglas production function                     updating
[firm].capital_elasticity                           capital elasticity in Cobb-Douglas production function                    updating
[household].labour                                  labour endowment per iteration                                            updating
[household].propensity_to_save                      percentage of wealth a household saves                                    updating
[environment].num_sweeps                            number of update steps in a simulation                                    updating
[environment].num_simulations                       number of simulations to be ran                                           updating
[environment].num_banks                             number of banks within the simulation                                     updating
[environment].num_firms                             number of firms within the simulation                                     updating
[environment].num_households                        number of households within the simulation                                updating
[environment].bank_directory                        directory containing config files for banks                               updating
[environment].firm_directory                        directory containing config files for firms                               updating
[environment].household_directory                   directory containing config files for households                          updating
[environment].central_bank_directory                directory containing config file for central bank                         updating
[environment].measurement_config                    location of measurement config file                                       updating
[environment].max_leverage_ratio                    maximum allowed leverage ratio of a bank                                  updating
[environment].required_reserves                     required deposit reserved to a central bank as a percentage               updating
[measurement].filename                              file name of the output csv file                                          updating
[measurement].output                                this is more tricky, to be added when going through measurement           updating