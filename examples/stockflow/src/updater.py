#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-


# -------------------------------------------------------------------------
#  class Updater
# -------------------------------------------------------------------------


class Updater():
    #
    #
    # METHODS
    #
    def get_identifier(self):
        return self.identifier

    # -------------------------------------------------------------------------
    # __init__
    # -------------------------------------------------------------------------
    def __init__(self, environment):
        self.environment = environment

        self.system_equity = 0
        self.system_assets = 0
        

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # do_update
    # -------------------------------------------------------------------------
    def do_update(self, environment, current_step):

        """The Update Step is broken down into two steps; i.e.
        first round effects and second round feedback effects.
        For now, we only have first round effects"""


        if current_step < 1:

            self.do_firstround_effects(environment, current_step)

        else:

            self.do_secondround_effects(environment, current_step)


    def do_firstround_effects(self, environment, current_step):
        print "1.**** UPDATER.PY*** FIRST ROUND EFFECTS:INITIALIZE ASSETS"

        for agent in environment.agents:

            agent.initialize_assets(environment, current_step)

            if any(c in agent.identifier for c in ("HF", "Hedge", "Hedgefund", "Hedge Fund")):
                agent.profit_hf(environment)
                print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income


            if any(c in agent.identifier for c in ("MMF", "Money Market")):
                agent.profit_mmf(environment)
                print "******* The", agent.identifier, " has profit in t=", current_step+1, "of", agent.net_income

            # self.system_equity += agent.state_variables['equity']
            # self.system_assets += agent.state_variables['total_assets']






    #
    def do_secondround_effects(self, environment, current_step):
        pass

        """For now, we don't have
        second round effects yet.
        It could be something like:
        We update the balance sheets from the first
        round effects.

        for agent in environment.agents:
            agent.update_balance_sheet()

        and then Update the shock vector
        print "2.**** UPDATER.PY*** SECOND ROUND EFFECTS:"
        """
    # -----------------------------------------------------------------------
