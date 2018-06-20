from src.model import qe_casp_model
import numpy as np
"""
Simulation parameters

1.Investor funds' parameters
    identifier : identifiers of funds
    lambdas : risk aversion parameters
    regions : domestic or foreign
    
    For expectations:
    tethas : default propability correction parameter  
    phi: Memory parameter determining how much weight is given to the last return observation  0 < phi < 1
    phi^p: Memory parameter determining how much weight is given to the last price observation  0 < phi^p < 1
    phi^x: Memory parameter determining how much weight is given to the last exchange rate observation  0 < phi^p < 1
    std_noise: the expected default probability has a fund-varying idiosyncratic noise component for the evaluation of news 
    
2. Assets parameters
    identifier : identifiers of assets
    
    
Global parameters
    days : time steps
    tau = iteration steps in price finding function of market maker
    global capital: sum of investor funds' capital 
    backward_simulated_time: used to simulate historical bond prices and returns
    xchange = foreign_price/domestic_price 
    
"""
"Simulation parameters"
days = 2
backward_simulated_time = 20

#  Domestic Price
p_domestic = 1.0
p_foreign = 12.0

x_domestic_to_foreign =  float(p_foreign)/float(p_domestic)
x_foreign_to_domestic =  float(p_domestic)/float(p_foreign)
#exchange_rate from the perspective of the domestic guy: x_f/x_d
#exchange rates are saved in dictionaries

exchange_rate = {"x_domestic_to_foreign": [x_domestic_to_foreign] }  #  x^d   *!*( x^f / x^d )*!* = x^f

"Fund parameters"
identifiers_funds = ["fund-1", "fund-2", "fund-3", "fund-4"]
#determine number of fund agents
number_funds = len(identifiers_funds)
risk_aversion = 2
correction_parameter = 0.01 # 1 percent
phi = 0.5
phi_p = 0.5
phi_x = 0.5
lambdas = (np.ones(number_funds) * risk_aversion).tolist()
phis = (np.ones(number_funds) * phi).tolist()
phis_p = (np.ones(number_funds) * phi_p).tolist()
phis_x = (np.ones(number_funds) * phi_x).tolist()

thetas = (np.ones(number_funds) * correction_parameter).tolist()
std_noises = [0.001, 0.002 , 0.001 , 0.004 ]  # Todo: using np array.tolist() as above

regions = ["domestic", "foreign"]

"Asset parameters"
identifiers_assets = ["domestic_low_risk", "domestic_high_risk", "foreign_high_risk", "foreign_low_risk", "domestic_cash", "foreign_cash"]
number_assets = len(identifiers_assets)
number_cash = len([i for i in identifiers_assets if "cash" in i])

"""Creating a list of nominal interest rate for rhos"""
rho = 0.04/250
bond_rhos = (np.ones(number_assets - number_cash ) * rho)
cash_rhos = np.ones(number_cash) * 0
rhos  = np.append(bond_rhos, cash_rhos ).tolist()  # rhos are nominal interest rate paid on the face value

"""Creating a list of default probabilities"""
omega = 10e-7
bond_omegas = (np.ones(number_assets - number_cash ) * omega )
cash_omegas = np.ones(number_cash) * 0
omegas  = np.append(bond_omegas, cash_omegas ).tolist()  # default probabilities omegas

"""Creating a list of face values"""
# How much is being raised by issuance
issuance = 1e6
bond_face_value = (np.ones(number_assets - number_cash ) * issuance)
cash_face_value = np.ones(number_cash) * 0
face_values = np.append(bond_face_value, cash_face_value).tolist()


supply_bond = issuance
supply_cash = 0.1 * issuance
"""Creating a list of global_supplies"""
# Price is one, so quantity is the same as issuance
bond_supply = (np.ones(number_assets - number_cash ) * supply_bond)
cash_supply = np.ones(number_cash) * supply_cash
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

qe_casp_model(days, identifiers_funds, lambdas, thetas, phis, phis_p, phis_x, regions, std_noises,
              identifiers_assets, ms, rhos, omegas, face_values, global_supply, prices, backward_simulated_time, exchange_rate   )