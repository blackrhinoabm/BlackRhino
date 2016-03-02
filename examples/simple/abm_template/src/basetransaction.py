#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Transaction
#
# -------------------------------------------------------------------------


class BaseTransaction(object):
    """
    Class variables: __metaclass__
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_type_(self):
        return
    @abc.abstractmethod
    def set_type_(self, _type):
        """
        Class variables: type_
        Local variables: _type
        """
        if not isinstance(_type, str):
            raise TypeError
        else:
            self.type_ = _type
        return
    type_ = abc.abstractproperty(get_type_, set_type_)
    # type of transactions, e.g. "deposit"
    # trailing underscore to distinguish from python keyword

    @abc.abstractmethod
    def get_asset(self):
        return
    @abc.abstractmethod
    def set_asset(self, _asset):
        """
        Class variables: transaction_asset
        Local variables: _asset
        """
        if not isinstance(_asset, str):
            raise TypeError
        else:
            self.asset = _asset
        return
    asset = abc.abstractproperty(get_asset, set_asset)
    # type of asset, used for investment types

    @abc.abstractmethod
    def get_from_(self):
        return
    @abc.abstractmethod
    def set_from_(self, _from):
        """
        Class variables: from_
        Local variables: _from
        """
        self.transaction_from_ = _from
        return
    from_ = abc.abstractproperty(get_from_, set_from_)
    # agent being the originator of the transaction
    # trailing underscore to distinguish from python keyword

    @abc.abstractmethod
    def get_to(self):
        return
    @abc.abstractmethod
    def set_to(self, _to):
        """
        Class variables: to
        Local variables: _to
        """
        self.to = _to
        return
    to = abc.abstractproperty(get_to, set_to)
    # agent being the recipient of the transaction

    @abc.abstractmethod
    def get_amount(self):
        return
    @abc.abstractmethod
    def set_amount(self, _amount):
        """
        Class variables: amount
        Local variables: _amount
        """
        if not isinstance(_amount, float) or isinstance(_amount, int):
            raise TypeError
        else:
            self.amount = float(_amount)
        return
    amount = abc.abstractproperty(get_amount, set_amount)
    # amount of the transaction

    @abc.abstractmethod
    def get_interest(self):
        return
    @abc.abstractmethod
    def set_interest(self, _interest):
        """
        Class variables: interest
        Local variables: _interest
        """
        if not isinstance(_interest, float) or isinstance(_interest, int):
            raise TypeError
        else:
            self.interest = float(_interest)
        return
    interest = abc.abstractproperty(get_interest, set_interest)
    # interest rate paid to the originator each time step

    @abc.abstractmethod
    def get_maturity(self):
        return
    @abc.abstractmethod
    def set_maturity(self, _maturity):
        """
        Class variables: maturity
        Local variables: _maturity
        """
        if not isinstance(_maturity, float) or isinstance(_maturity, int):
            raise TypeError
        else:
            self.maturity = int(_maturity)
        return
    maturity = abc.abstractproperty(get_maturity, set_maturity)
    # time (in steps) to maturity

    @abc.abstractmethod
    def get_time_of_default(self):
        return
    @abc.abstractmethod
    def set_time_of_default(self, _time_of_default):
        """
        Class variables: time_of_default
        Local variables: _time_of_default
        """
        if not isinstance(_time_of_default, float) or isinstance(_time_of_default, int):
            raise TypeError
        else:
            self.time_of_default = int(_time_of_default)
        return
    time_of_default = abc.abstractproperty(get_time_of_default, set_time_of_default)
    # control variable checking for defaulted transactions

    @abc.abstractmethod
    def this_transaction(self, type_, asset, from_, to, amount, interest, maturity, time_of_default):
        self.type_ = type_
        # if transactionType == "I":
        self.asset = asset
        # the convention used is that amounts are positive
        if amount >= 0:
            self.from_ = from_
            self.to = to
        else:  # negative amounts reverse direction and delete sign
            self.from_ = to
            self.to = from_
            amount = abs(amount)
        self.amount = amount
        self.interest = interest
        self.maturity = maturity
        self.time_of_default = time_of_default
    # a standard function which sets the variables of the transaction to the given amounts

    @abc.abstractmethod
    def print_transaction(self):
        print "        <transaction type='" + self.type_ + "'>"
        if self.asset != "":
            print "        <transaction asset='" + self.asset + "'>"
        if hasattr(self.from_, "identifier"):
            print "            <property type='from' amount='" + str(self.from_.identifier) + "'></property>"
        else:
            print "            <property type='from' value='" + str(self.from_) + "'></property>"
        if hasattr(self.to, "identifier"):
            print "            <property type='to' value='" + str(self.to.identifier) + "'></property>"
        else:
            print "            <property type='to' value='" + str(self.to) + "'></property>"
        print "            <property type='amount' value='" + str(self.amount) + "'></property>"
        print "            <property type='interest' value='" + str(self.interest) + "'></property>"
        print "            <property type='maturity' value='" + str(self.maturity) + "'></property>"
        print "            <property type='time_of_default' value='" + str(self.time_of_default) + "'></property>"
        print "        </transaction>"
    # a standard function which prints the transaction and its properties

    @abc.abstractmethod
    def write_transaction(self):
        text = "        <transaction type='" + self.type_ + "'>\n"
        if self.asset != "":
            text += "        <transaction asset='" + self.asset + "'>\n"
        if hasattr(self.from_, "identifier"):
            text += "            <property type='from' value='" + str(self.from_.identifier) + "'></property>\n"
        else:
            text += "            <property type='from' value='" + str(self.from_) + "'></property>\n"
        if hasattr(self.to, "identifier"):
            text += "            <property type='to' value='" + str(self.to.identifier) + "'></property>\n"
        else:
            text += "            <property type='to' value='" + str(self.to) + "'></property>\n"
        text += "            <property type='amount' value='" + str(self.amount) + "'></property>\n"
        text += "            <property type='interest' value='" + str(self.interest) + "'></property>\n"
        text += "            <property type='maturity' value='" + str(self.maturity) + "'></property>\n"
        text += "            <property type='time_of_default' value='" + str(self.time_of_default) + "'></property>\n"
        text += "        </transaction>\n"

        return text
    # a standard function which returns a string with the transaction and its properties
