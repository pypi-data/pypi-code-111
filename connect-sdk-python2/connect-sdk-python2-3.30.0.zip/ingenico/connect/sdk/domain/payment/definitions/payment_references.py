# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class PaymentReferences(DataObject):

    __merchant_order_id = None
    __merchant_reference = None
    __payment_reference = None
    __provider_id = None
    __provider_reference = None
    __reference_orig_payment = None

    @property
    def merchant_order_id(self):
        """
        | Your order ID for this transaction that is also returned in our report files
        
        Type: long
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def merchant_reference(self):
        """
        | Your unique reference of the transaction that is also returned in our report files. This is almost always used for your reconciliation of our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    @property
    def payment_reference(self):
        """
        | Payment Reference generated by WebCollect
        
        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value):
        self.__payment_reference = value

    @property
    def provider_id(self):
        """
        | Provides an additional means of reconciliation for Gateway merchants
        
        Type: str
        """
        return self.__provider_id

    @provider_id.setter
    def provider_id(self, value):
        self.__provider_id = value

    @property
    def provider_reference(self):
        """
        | Provides an additional means of reconciliation for Gateway merchants
        
        Type: str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value):
        self.__provider_reference = value

    @property
    def reference_orig_payment(self):
        """
        | When you did not supply a merchantReference for your payment, you need to fill this property with the reference of the original payment when you want to refund it
        
        Type: str
        """
        return self.__reference_orig_payment

    @reference_orig_payment.setter
    def reference_orig_payment(self, value):
        self.__reference_orig_payment = value

    def to_dictionary(self):
        dictionary = super(PaymentReferences, self).to_dictionary()
        if self.merchant_order_id is not None:
            dictionary['merchantOrderId'] = self.merchant_order_id
        if self.merchant_reference is not None:
            dictionary['merchantReference'] = self.merchant_reference
        if self.payment_reference is not None:
            dictionary['paymentReference'] = self.payment_reference
        if self.provider_id is not None:
            dictionary['providerId'] = self.provider_id
        if self.provider_reference is not None:
            dictionary['providerReference'] = self.provider_reference
        if self.reference_orig_payment is not None:
            dictionary['referenceOrigPayment'] = self.reference_orig_payment
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentReferences, self).from_dictionary(dictionary)
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'providerId' in dictionary:
            self.provider_id = dictionary['providerId']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        if 'referenceOrigPayment' in dictionary:
            self.reference_orig_payment = dictionary['referenceOrigPayment']
        return self
