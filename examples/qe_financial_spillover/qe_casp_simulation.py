from src.updater import qe_casp_model

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
thetas = [2,2, 3, 3]
identifiers_funds = ["fund-1", "fund-2", "fund-3", "fund-4"]
regions = ["domestic", "foreign"]
global_capital = 1e9

"Asset parameters"
identifiers_assets = ["domestic_low_risk", "domestic_high_risk", "foreign_high_risk", "foreign_low_risk", " domestic_cash", "foreign_cash"]
ms = [0.95, 0.99 , 0.95, 0.99 , 0 , 0 ]  #(1 - m) fraction of principal being repaid at every iteration step; e.g. (1 - 0.99) : 1% of principal is being repaid
rhos = [0.05/250, 0.05/250, 0.05/250, 0.05/250 , 0 , 0 ] # rhos are nominal interest rate paid on the face value
omegas = [0.0001, 0.0001, 0.0001, 0.0001, 0, 0] # default probabilities omegas
face_values = [100000, 100000, 100000, 100000, 0, 0]


"Method to call simulation"

qe_casp_model(identifiers_funds, thetas, regions, global_capital,
              identifiers_assets, ms, rhos, omegas, face_values)