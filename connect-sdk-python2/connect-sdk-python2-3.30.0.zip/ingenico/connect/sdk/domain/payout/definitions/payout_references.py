# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PayoutReferences(DataObject):

    __invoice_number = None
    __merchant_order_id = None
    __merchant_reference = None

    @property
    def invoice_number(self):
        """
        | Your invoice number (on printed invoice) that is also returned in our report files
        
        Type: str
        """
        return self.__invoice_number

    @invoice_number.setter
    def invoice_number(self, value):
        self.__invoice_number = value

    @property
    def merchant_order_id(self):
        """
        | Order Identifier generated by the merchant
        | Note: This does not need to have a unique value for each transaction
        
        Type: long
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def merchant_reference(self):
        """
        | Note that the maximum length of this field for transactions processed on the GlobalCollect platform is 30. Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    def to_dictionary(self):
        dictionary = super(PayoutReferences, self).to_dictionary()
        if self.invoice_number is not None:
            dictionary['invoiceNumber'] = self.invoice_number
        if self.merchant_order_id is not None:
            dictionary['merchantOrderId'] = self.merchant_order_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        return dictionary

    def from_dictionary(self, dictionary):
        super(PayoutReferences, self).from_dictionary(dictionary)
        if 'invoiceNumber' in dictionary:
            self.invoice_number = dictionary['invoiceNumber']
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        return self
