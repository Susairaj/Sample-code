@api.model
    def default_get(self, fields_list):
        res = super(SaleReplacementLine, self).default_get(self)
        """ Validating total percentage amount as 100 """
        percentage = self._context.get('percentage',False) 
        lines = self._context.get('lines',False)
        print self.percentage
        if lines == 0:
            res['percentage'] = 100
        else:
            res['percentage'] = percentage
        return res
###############################################################
To Create new record in other object:::
(0,0,{'':object.field,'':object.field})
To Update new record in other object::
(0,6,{})
To split the record:::
.split(':')[0]
.split(':')[1]

#############################################################
Create , Default_get,corn job(scheduler)-----@api.model
Write ----@api.multi

################################################################
To Notify the Action::: to the current user

alert_msg = 'Your message has been sent successfully. Your have overridden '+str(cre_bal_now)+' credits.'
            res = {
            'type': 'ir.actions.client',
            'tag': 'action_warn',
            'name': 'Failure',
            'params': {
               'title': 'Notification',
               'text': alert_msg,
               'sticky': True
                }
            }
            return res
##################################################