from src.updater import qe_casp_model
import numpy as np
"""
Simulation parameters


1.Investor funds' parameters
    identifier : identifiers of funds
    thetas : risk aversion parameters
    regions : domestic or foreign
    phi: Memory parameter determining how much weight is given to the last return observation  0 < phi < 1
    phi^p: Memory parameter determining how much weight is given to the last price observation  0 < phi^p < 1

    
2. Assets parameters
    identifier : identifiers of assets
    
    
Global parameters
    days : time steps
    tau = iteration steps in price finding function of market maker
    global capital: sum of investor funds' capital 
"""


"Fund parameters"
identifiers_funds = ["fund-1", "fund-2", "fund-3", "fund-4"]
#determine number of fund agents
number_funds = len(identifiers_funds)
risk_aversion = 2
thetas = (np.ones(number_funds) * risk_aversion).tolist()

regions = ["domestic", "foreign"]
global_capital = 1e9 # reverse engineer?

"Asset parameters"
identifiers_assets = ["domestic_low_risk", "domestic_high_risk", "foreign_high_risk", "foreign_low_risk", " domestic_cash", "foreign_cash"]
number_assets = len(identifiers_assets)
number_cash = len([i for i in identifiers_assets if "cash" in i])

"""Creating a list of nominal interest rate for rhos"""
rho = 0.05/250
bond_rhos = (np.ones(number_assets - number_cash ) * rho)
cash_rhos = np.ones(number_cash) * 0
rhos  = np.append(bond_rhos, cash_rhos ).tolist()  # rhos are nominal interest rate paid on the face value

"""Creating a list of default probabilities"""
omega = 0.0001
bond_omegas = (np.ones(number_assets - number_cash ) * omega )
cash_omegas = np.ones(number_cash) * 0
omegas  = np.append(bond_omegas, cash_omegas ).tolist()  # default probabilities omegas

"""Creating a list of face values"""
# How much is being raised by issuance
issuance = 1e6
bond_face_value = (np.ones(number_assets - number_cash ) * issuance)
cash_face_value = np.ones(number_cash) * 0
face_values = np.append(bond_face_value, cash_face_value).tolist()


supply = issuance
"""Creating a list of global_supplies"""
# Price is one, so quantity is the same as issuance
bond_supply = (np.ones(number_assets - number_cash ) * supply)
cash_supply = np.ones(number_cash) * 0
global_supply = np.append(bond_supply, cash_supply).tolist()


price_zero = 1.0
"""Creating a list of global_supplies"""
# Price is one, so quantity is the same as issuance
bond_price = (np.ones(number_assets - number_cash ) * price_zero)
cash_price = np.ones(number_cash) * 0
prices= np.append(bond_price, cash_price).tolist()



"""Creating a list of ms""" # Todo: using np array.tolist() as above
ms = [0.95, 0.99 , 0.95, 0.99 , 0 , 0 ]  #(1 - m) fraction of principal being repaid at every iteration step; e.g. (1 - 0.99) : 1% of principal is being repaid


"Method to call simulation"

qe_casp_model(identifiers_funds, thetas, regions, global_capital,
              identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices)