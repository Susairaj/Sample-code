# -*- coding: utf-8 -*-

from openerp import api, fields, models
from datetime import datetime


class SubContractorReport(models.Model):
    _name = "sub.contractor.report"
    _description = "Sub Contractor Report"

    @api.multi
    def print_report(self, context=None, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('psit.sub_contractor_summary_report_qweb')
        return {
            'context': context,
            'data': data,
            'type': 'ir.actions.report.xml',
            'report_name': report.report_name,
            'report_type': report.report_type+"_close",
            'report_file': report.report_file,
        }
    
    blocks_id = fields.Many2one('blocks.blocks', string='Block')
    location_id = fields.Many2one('locations.locations', string='Location')
    contractor_material_id = fields.Many2one('contractor.contractor', string='Contractor Type', required=True)
    date_from = fields.Date(string='Start Date', default=datetime.now(), required=True)
    date_to = fields.Date(string='End Date', default=datetime.today(), required=True)
    
    contractor_mat_ids = fields.One2many('sub.contractor', 'contractor_id', 'Sub Contractor Summary Report')


class SubContractor(models.Model):
    _name = "sub.contractor"
    _description = 'Sub Contractor Details'
    
    material_id = fields.Many2one('material.configuration', 'Name')
    unique_id = fields.Char('ID', related='material_id.unique_id')
    unit_id = fields.Many2one('materials.units', 'Unit')
    quantity_issued = fields.Float('Total Quantity Issued')
    quantity_returned = fields.Float('Total Quantity Returned')
    net_quantity_issues = fields.Float('Net Quantity Issues')
    remarks = fields.Char('Remarks')
    contractor_id = fields.Many2one('sub.contractor.report', 'Contractor')