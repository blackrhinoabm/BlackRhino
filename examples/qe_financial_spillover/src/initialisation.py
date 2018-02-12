from fund import Fund
from asset import Asset
from functions import *
from functions.distribute import *

import random

def init_funds(identifiers_funds, thetas, regions, global_capital):
    #Instantiate investor funds using the number of identifiers as range
    fund_list = []
    # Loop over number of funds
    for ident, theta  in zip(identifiers_funds, thetas):
        # Instantiate fund object
        fund = Fund(ident, theta)
         # Save in list
        fund_list.append(fund)

    fund_regions = distribute_funds_equally(len(identifiers_funds), regions)

    # Attach region to funds
    for fund, region_label in zip(fund_list, fund_regions):
        fund.parameters['region'] = region_label

    # # Allocate fund size
    # fund_sizes = distribute_funds_equally(len(identifiers_funds), [global_capital / len(identifiers_funds)])
    # for fund, size in zip(fund_list, fund_sizes):
    #     fund.state_variables['capital'] = size

    return fund_list

def init_assets(regions, identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices):
    # Instantiate investor funds using the number of identifiers as range
    asset_dict = {}
      # Loop over regions
    for region in regions:
        temp = {
            region : {}
                }
        asset_dict.update(temp)

    domestic = []
    foreign = []

    for ident,  m, rho, omega, face_value, global_supply, price  in zip(identifiers_assets,  ms, rhos, omegas, face_values,global_supply, prices):
        # Instantiate fund object
        asset = Asset(ident, m, rho, omega, face_value, global_supply, price )

        # Save in dict - hard coded; not elegant and problematic if there are more assets
        if "domestic" in ident:
            domestic.append(asset)
        if "foreign" in ident:
            foreign.append(asset)

    for key, value in  asset_dict.iteritems():
        if "domestic" in key:
            asset_dict[key] = domestic
        if "foreign" in key:
            asset_dict[key] = foreign
    return  asset_dict

def init_returns(assets):
    for key, list in assets.iteritems():
        for asset in list:
            return_ = asset.parameters['rho']
            asset.returns.append(return_)

def init_portfolio_transactions(identifiers_funds, funds, asset_dict):
    for fund in funds:
        weights = fund.calc_optimal_pf(asset_dict)

    # for key, list in asset_dict.iteritems():
    #     for asset in list:
    #         asset.parameters['global_quantity']

    # fund_sizes = distribute_funds_equally(len(identifiers_funds), [global_capital / len(identifiers_funds)])
    #
    # print fund_sizes
    # for fund, size in zip(fund_list, fund_sizes):
    #     fund.state_variables['capital'] = size

    valuation_domestic = 0
    valuation_foreign  = 0

    # valuation_b = amount_b * environment.variable_parameters['price_of_b']
    # self.add_transaction("B", "assets", "firm-abroad", self.identifier, amount_b, 0, 0, -1, environment)
    #
    # # Code to see transactions and keeping track of index, value pairs
    # # for num, line in enumerate(self.accounts):
    # #     print("{}: {}".format(num, line))
    #
    # valuation_a = amount_a * environment.variable_parameters['price_of_a']
    # self.add_transaction("A", "assets", "firm-domestic",self.identifier, amount_a, 0, 0, -1, environment)
    # #
    #
    # """Be careful with the from_ agent here: environment.agents[2].identifier. Government is the third
    # item in environment.agents list"""
    # amount = round((self.get_account("investment_shares") - valuation_b - valuation_a)/environment.variable_parameters['price_of_bond'], 4)
    # self.add_transaction("Risk_free", "assets", environment.agents[2].identifier ,self.identifier, amount, 0, 0, -1, environment)
    #



