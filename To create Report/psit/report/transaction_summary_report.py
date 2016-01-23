import time
from openerp.osv import osv
from openerp.report import report_sxw

class transaction_summary_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context): 
         if context is None:
            context = {}
         super(transaction_summary_report, self).__init__(cr, uid, name, context=context)
         self.localcontext.update({
        })
   
class report_fabsheetqweb(osv.AbstractModel):
    _name = "report.psit.transaction_summary_report_qweb"
    _inherit = "report.abstract_report"
    _template = "psit.transaction_summary_report_qweb"
    _wrapped_report_class = transaction_summary_report