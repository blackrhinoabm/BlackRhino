#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This script contains the Agent class which is later called in the Environment
# script.

import logging

from src.shock import Shock
from src.runner import Runner

from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Bank
#
# ============================================================================


class Agent(BaseAgent):
    #
    #
    # VARIABLES
    #
    identifier = ""  # identifier of the specific agent
    state_variables = {}
    parameters = {}

    ''' Accounts is not used in our example, but it's in the BaseAgent
    parent class'''
    accounts = []

    #
    #
    # CODE
    #
    #

    #
    #
    # all the methods inherited from the abstract class BaseAgent
    # that we need to include so the agent class gets instantiated
    # we can use them to modify the program easier (e.g. set_num_sweeps)
    #
    #

    def __getattr__(self, attr):
        super(Agent, self).__getattr__(attr)


    def __str__(self):
        # return super(Agent, self).__str__()

        ret_str = "  <agent identifier='" + self.identifier + "'>\n "

        for entry in self.parameters:
            value = self.parameters[entry]
            ret_str = ret_str + " <parameter type='parameters' name=" + entry + "' value='" + str(value) + "'></parameter>\n"

        for entry in self.state_variables:
            value = self.state_variables[entry]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
                ret_str = ret_str + "    <parameter type='state_variables' name='" + entry + "' value='" + str(value) + "'></parameter>\n"
            else:
                raise TypeError
        ret_str = ret_str + "</agent>\n"
        return ret_str

    def get_parameters(self):
        return self.parameters

    def append_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def set_parameters(self, values):
        super(Agent, self).append_parameters(values)

    def append_state_variables(self, values):
        super(Agent, self).append_state_variables(values)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _variables):
        super(Agent, self).set_state_variables(_variables)

    def check_consistency(self, assets, liabilities):
        super(Agent, self).check_consistency(assets,liabilities)

    def clear_accounts(self):
        super(Agent, self).clear_accounts()

    def get_account(self, _type):
        super(Agent, self).get_account(_type)

    def purge_accounts(self, environment):
        super(Agent, self).purge_accounts(environment)

    def get_account_num_transactions(self, _type):
        super(Agent, self).get_account_num_transactions(_type)

    def get_transactions_from_file(self, filename, environment):
        super(Agent, self).get_transactions_from_file(filename, environment)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        super(Agent, self).set_identifier(value)

    def update_maturity(self):
        super(Agent, self).update_maturity()

    # -----------------------------------------------------------------------
    # __init__  used to automatically instantiate an agent as an object when
    # the agent class is called
    # ------------------------------------------------------------------------

    def __init__(self):
        self.identifier = ""  # identifier of the specific agent
        self.state_variables = {}
        self.parameters = {}

        # local state variables used in computation of asset sales
        self.state_variables['shock_for_agent'] = 0.0
        self.state_variables['total_asset_sales'] = 0.0
        self.state_variables['direct_impact'] = 0 
        
        self.state_variables["valuation_losses"] = 0.0
        self.state_variables["equity_losses"] = 0.0
        self.state_variables["equity_losses_from_system_deleveraging"] = 0.0
        self.state_variables["asset_losses_from_system_deleveraging"] = 0.0

        self.state_variables["debt_paid_by_cash"] = 0.0 
        self.pre_shock_equity = 0
        self.state_variables["total_assets"] = 0


        self.temp = 0
        self.sale_of_k_assets = {}


        self.state_variables['systemicness']= 0
        self.results_df = 0

        self.new_weights = {}
        self.balance_sheet_valuation = {}


    def get_parameters_from_file(self, agent_filename, environment):
        from xml.etree import ElementTree

        try:
            xmlText = open(agent_filename).read()
            element = ElementTree.XML(xmlText)
            # we get the identifier
            self.identifier = element.attrib['identifier']

            # and then we're only interested in <parameter> fields
            element = element.findall('parameter')

            # loop over all <parameter> entries in the xml file
            for subelement in element:

                if subelement.attrib['type'] == 'parameters':
                    name = str(subelement.attrib['name'])
                    value = float(subelement.attrib['value'])
                    self.parameters[name] = value

                if subelement.attrib['type'] == 'state_variables':
                    name = str(subelement.attrib['name'])
                    value = float(subelement.attrib['value'])
                    self.state_variables[name] = value

            self.new_weights = self.parameters       
        except:
            logging.error("    ERROR: %s could not be parsed", agent_filename)


    # -------------------------------------------------------------------------
    #
    # ---------------------------------------------------------------------
    def change_leverage(self, param):
        # if self.identifier == "SBSA":  #check SBSA
        #     print(self.state_variables['debt'])
        #     print(self.state_variables['equity'])
        #     print(self.parameters['leverage'])
        #     print(self.state_variables['debt']/self.state_variables['equity'])
        #Before is correct
 
        self.parameters['leverage']= self.parameters['leverage'] * param 
        self.state_variables['debt'] = self.state_variables['equity'] * self.parameters['leverage']

        
        # if self.identifier == "SBSA":  #check SBSA
        #     print('leverage' , self.state_variables['debt'] / self.state_variables['equity'] , self.parameters['leverage'])

    def initialize_total_assets(self):
        self.pre_shock_equity = self.state_variables['equity']
        self.state_variables['total_assets']  = self.state_variables['debt'] + self.state_variables['equity']

    def initialize_cash_reserves(self):
        self.state_variables['cash_reserves'] = self.state_variables['total_assets'] * self.parameters['m_1']

    def update_balance_sheet(self):
        self.state_variables['total_assets'] = self.state_variables['debt'] + self.state_variables['equity']
        self.parameters = self.new_weights
 
    def check_accounts(self):
        if self.state_variables['total_assets'] == self.state_variables['equity'] + self.state_variables['debt']:
            print("yes, great - the accounting worked for %s" %self.identifier)
        else:
            print('no.. damn!')

    def initialize_shock(self, environment):
        self.state_variables['shock_for_agent'] = 0.0

        for shock in environment.shocks:
            for k in set(self.parameters) & set(shock.asset_returns):

                self.state_variables['shock_for_agent'] +=  self.parameters[k] * shock.asset_returns[k]

                'Uncomment this code to print which asset class and which shock'
                # if self.identifier == "SBSA":
                #         if shock.asset_returns[k]!= 0.0:
                #             print(shock.asset_returns[k], k, "shooock!")

        self.state_variables['direct_impact'] = self.state_variables['shock_for_agent'] * self.state_variables['total_assets']

        #quick accounting test for step1: I print to screen the asset class that is being shocked
        #Like this I can verify the configuration (no time to write testing file)
        # if self.identifier == "SBSA":
        #     print("ACCOUNTING FOR ONE BANK")
        #     print("The shock for ", self.identifier, "TOTAL ASSET is:", self.state_variables['shock_for_agent'], "so", self.state_variables['shock_for_agent'] * 100 , "per cent")

    #Calculate direct losses (shock proportional to asset share times total assets)
    def calc_equity_and_valuation_losses(self):
        self.state_variables["equity_losses"] = self.state_variables['shock_for_agent'] * self.state_variables['total_assets']
        self.state_variables["valuation_losses"] =  self.state_variables["equity_losses"] * self.parameters['leverage'] 
 
    def check_losses_against_capital_bufffer(self, environment, current_step):
        #Get the current amount of cash reserves
        
        if self.state_variables['cash_reserves'] == 0:
            self.state_variables['debt_paid_by_cash'] = 0

            return 0

        else:
            print(self.state_variables['cash_reserves'] , "cash reserves")
            new_equity = self.state_variables["equity"] - abs(self.state_variables["equity_losses"]) 
            print('new_equity', new_equity, self.identifier)
            new_debt = new_equity * self.parameters['leverage']
            print(self.state_variables['debt']  , "debt" , self.identifier)
            print(new_debt, "new debt", self.identifier)

            difference = self.state_variables['debt']  - new_debt  
            print(difference , "difference", self.identifier)
         
            if (self.state_variables['cash_reserves'] - difference) > 0:              
                    buffer = (self.state_variables['cash_reserves'] - difference)
                    print(buffer, "BUFFER", "Cash reserves are enough!!!, no fire-sale for", self.identifier)
                    return buffer

            if (self.state_variables['cash_reserves'] - difference) <= 0 and self.state_variables['cash_reserves'] >0:
                    print(self.state_variables['cash_reserves'], difference)
                    print("Cash reserves are NOT enough!!!, Fire-sale for", self.identifier)
                    paid_by_cash = self.state_variables['cash_reserves']
                    
                    self.state_variables["debt_paid_by_cash"] = paid_by_cash  
                    return 0 

            if (self.state_variables['cash_reserves'] - difference) < 0:
                    return 0 
 
    def new_cash_weight(self, total_assets):
        new_weight = self.state_variables['cash_reserves'] / total_assets
        old_weight = self.parameters['m_1']  
        #print new_weight, "new_weight", "old weight:" , old_weight
        difference = old_weight - new_weight 

        local_sum = 0
        for p in self.parameters:
            if not any(c in p for c in ( "leverage")):
                if p != 'm_1':
                    local_sum+=1  
        add_to_other_weights = (difference/local_sum)

        return new_weight, add_to_other_weights


    def update_asset_weights(self, new_weight, add_to_other_weights, environment, current_step):
        for p in self.new_weights:
            if not any(c in p for c in ( "leverage")):
                if p == 'm_1':
                    self.new_weights[p] = new_weight
                else:
                    self.new_weights[p]  = self.new_weights[p]  +  add_to_other_weights

    def calc_new_equity_and_debt(self):
        new_equity = self.state_variables["equity"] - abs(self.state_variables["equity_losses"])
        new_debt = new_equity * self.parameters['leverage']
        
        self.state_variables['debt'] =  new_debt
        self.state_variables['equity'] =  new_equity


    def calc_total_asset_sales(self, environment, current_step, new_assets, paid_by_cash):

        # for shock in environment.shocks:
        #     self.state_variables['total_asset_sales'] = 0.0
        #     local_sum = 0.0   # not elegant, but safe, just to keep track of summing

        #     for k in self.parameters.keys():
        #         try:
        #             local_sum += self.parameters[k] * shock.asset_returns[k]
        #         except:
        #             pass
        self.state_variables['total_asset_sales'] = self.state_variables["valuation_losses"]  + paid_by_cash
        # "Check by accounting:"
        # if self.identifier == "SBSA":
        #     print "***AGENT.PY***The total asset sales for ", self.identifier, "are:", self.state_variables['total_asset_sales']

#                for k in set(self.state_variables) & set(shock.asset_returns):
                    #print self.state_variables['total_asset_sales'],  self.state_variables[k], shock.asset_returns[k]
#                    self.state_variables['total_asset_sales'] = self.state_variables['total_asset_sales'] + self.state_variables[k] * shock.asset_returns[k]
#                self.state_variables['total_asset_sales'] = self.state_variables['total_assets'] * self.state_variables['total_asset_sales'] * self.state_variables['leverage']
    
    def calc_systemicness(self, environment, current_step, AV):        
        if AV!= 0:
            self.state_variables['systemicness'] = self.state_variables["equity_losses_from_system_deleveraging"] / AV
        else: 
            self.state_variables['systemicness'] = 0
        
 

    def calc_asset_losses_from_system_deleveraging(self, environment, current_step):
        asset_losses_from_other_bank_selling = (self.state_variables['shock_for_agent'] * self.state_variables['total_assets'] * self.parameters['leverage'] )
        self.state_variables["asset_losses_from_system_deleveraging"] = asset_losses_from_other_bank_selling   
        return asset_losses_from_other_bank_selling



    def calc_equity_losses_from_system_deleveraging(self, environment, current_step):
        losses_from_other_bank_selling = (self.state_variables['shock_for_agent'] * self.state_variables['total_assets']) 
        self.state_variables["equity_losses_from_system_deleveraging"] = losses_from_other_bank_selling   
        return losses_from_other_bank_selling
    # def add_parameters_dealer(self, updater):
    #
    #     if any(c in self.identifier for c in ("SBSA", "ABSA", "NEDBANK", "DB", "JpM", "HSBC", "FNB", "CITYBANK", "INVESTEC")):
    #         self.parameters['dealer']= 1.0
    #         for k in self.parameters:
    #             if k == 'm_14':
    #                 self.state_variables['inventory_risky_asset']  =  self.parameters[k] * self.state_variables['total_assets']
    #                 self.state_variables['inventory_risky_asset_quantity'] = self.state_variables['inventory_risky_asset'] / updater.prices['risky_asset']
    #                 return self.state_variables['inventory_risky_asset']
    #     else:
    #         self.parameters['dealer']=0

    def append_results_to_dataframe(self, current_step):
        import pandas as pd

        results_state_variables = []
        results_state_varnames =[]

        results_parameters = []
        results_parnames =[]
        temp =0

        for i in self.state_variables:
            results_state_varnames.append(i + " " + self.identifier)
            results_state_variables.append(self.state_variables[i])

        df1 = pd.DataFrame(columns=results_state_varnames)
        df1 = df1.append(pd.Series(results_state_variables, index=results_state_varnames), ignore_index=True)

        for i in self.parameters:
            results_parnames.append(i + " " + self.identifier)
            results_parameters.append(self.parameters[i])

        "We do the same for parameters"
        df3 = pd.DataFrame(columns=results_parnames)
        df3 = df3.append(pd.Series(results_parameters, index=results_parnames), ignore_index=True)

        df2 = pd.DataFrame({'current_step':[current_step]})

        self.results_df = pd.concat([df2, df1], axis=1)
        logging.info('Agent.py; function: Appended agents state_variables results to %s dataframe' %self.identifier )

        "To add parameters uncomment and use instead of line\
        above. But DON't forget to change method\
        def update_results_to_dataframe below\
        and uncomment "
        self.results_df = pd.concat([df2, df1, df3], axis=1)
        logging.info('Agent.py; function: Appended agents parameter and state_variables results to %s dataframe' %self.identifier )
        return self.results_df


    def update_results_to_dataframe(self, current_step):
        import pandas as pd

        if current_step >0:
            temp = []
            timer = []
            results_state_variables = []

            timer = current_step
            temp.append(timer)

            for state_variable in self.state_variables:
                temp.append(self.state_variables[state_variable])

            "To add parameters uncomment, but also change method\
            def  append_results_to_dataframe in above!!\
            uncomment "
            for p in self.parameters:
                temp.append(self.parameters[p])
            x = list(self.results_df.columns.values)

            dftemp = pd.DataFrame([temp], columns=x)
            self.results_df = pd.concat([self.results_df, dftemp], ignore_index=True)
