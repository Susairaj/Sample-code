from openerp import models, fields,api
from datetime import datetime, timedelta

class sale_order(models.Model):
    _inherit ='sale.order'
    
#    this function is overwritton
    def _amount_all_wrapper(self, cr, uid, ids, field_name, arg, context=None):
        """ Wrapper because of direct method passing as parameter for function fields """
        return self._amount_all(cr, uid, ids, field_name, arg, context=context)

    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
#        print self.order_line.discount
        for order in self.browse(cr, uid, ids, context=context):
            res[order.id] = {
                'amount_untaxed': 0.0,
                'amount_tax': 0.0,
                'amount_total': 0.0,
            }
            val = val1 = 0.0
            cur = order.pricelist_id.currency_id
            for line in order.order_line:
                val1 += line.price_subtotal
                val += self._amount_line_tax(cr, uid, line, context=context)
            res[order.id]['amount_tax'] = cur_obj.round(cr, uid, cur, val)
            amount = cur_obj.round(cr, uid, cur, val1)
            res[order.id]['amount_untaxed'] = amount
            res[order.id]['amount_total'] = amount - order.discount + order.expedite + order.shipping - order.shipping_discount
        return res
    
    
    
    customer_po = fields.Char('Customer Po',required=True)
    lead_time = fields.Many2one('edoption.lead.time','Lead Time')
    est_ship_date = fields.Date('Est. Ship Date')
#    payment_term = fields.Many2one('account.payment.term','Terms')
    handling_id = fields.Many2one('edoption.expedite.type','Order Type')
    package_type_id = fields.Many2one('packaging.type','Package Type')
#    carrier_id = fields.Many2one('delivery.carrier','Ship Method')
    agent_id = fields.Many2one('sale.agent','Sales Rep')
    commission_id = fields.Many2one('commission','Sales Rep Code')
    specrep_id = fields.Many2one('sale.agent','Spec Rep')
    speccode_id = fields.Many2one('commission','Spec Rep Code')
    shipping_id = fields.Many2one('res.partner','Customer')
    partner_invoice_id = fields.Many2one('res.partner','Invoice Address')
    partner_shipping_id = fields.Many2one('res.partner','Shipping Address')
    customer_notes = fields.Text('Customer Notes')
    product_type = fields.Many2one('product.types', 'Product Type')
    unit_type = fields.Selection([('decimal_inch','Decimal Inch'),('metric','Metric')],'Unit Type')
    pending_date= fields.Datetime('Changes Pending Date',readonly=True)
    date_confirm = fields.Datetime('Confirmation Date',readonly=True)
    ask_date = fields.Datetime('Acknowledged Date',readonly=True)
    approve_date = fields.Datetime('Approval Date',readonly=True)
    ship_date = fields.Datetime('Actual Shipped Date',readonly=True)
    info_note = fields.Text('Internal Notes')
    special_instrudtion = fields.Text('Special Instruction')
    discount_type = fields.Many2one('discount.type','Discount Type')
    discount_percent = fields.Float('Discount(%)')
    discount = fields.Float('Discount Amount')
    expedite = fields.Float('Expedite')
    shipping = fields.Float('Shipping Cost')
    shipping_discount = fields.Float('Shipping Discount')
    is_back_order = fields.Boolean('Is Back Order')
    is_slip_generated = fields.Boolean('Is Packing Slip Printed')
    handling_type = fields.Selection([('rush','Rush Order'),('select','Select Order'),('normal','Normal Order')],'Handling Type')
    expedite_fee = fields.Selection([('50','50% Fee'),('30','30% Fee'),('10','10% Fee')],'Expedite Fee')
    customer_priority = fields.Integer('Customer Priority')
    rep_origin_id =  fields.Many2one('sale.order','Original Order')
    repl_note = fields.Text('Notes')
    replacement_ids = fields.One2many('replacement.code','sale_order_id')
    insert_finish = fields.Char('Insert Notes')
    parapan_color = fields.Many2one('product.product','Color')
    door_edge_radius = fields.Many2one('edge.radius','Door Edge Radius')
    profile = fields.Many2one('element.profile', 'Profile Type')
    insert = fields.Many2one('product.product', 'Insert Type')
    finish = fields.Many2one('edoption.finish','Profile Finish')
    bpg_color = fields.Many2one('product.product','Color')
    bpg_thickness = fields.Many2one('bpg.thickness','Thickness')
    insert_edge_detail = fields.Many2one('edge.detail','Edge Detail')
    bpg_finish = fields.Selection([('gloss','Gloss'),('matte','Matte')],'Glass Finish')
    basesystem_support_option = fields.Selection([('feet','Feet'),('casters','Casters'),('cap','Caps Only'),('no_caps','No Caps')],'Support Options')
    deco_panel_type = fields.Selection([('single_sided','Single Sided'),('double_sided','Double Sided')],'DecoPanel Type')
    middle_insert = fields.Many2one('product.product','Middle Insert Type')
    ledcolor_temperature = fields.Many2one('product.product','Led Color Temperature')
    front_insert = fields.Many2one('product.product','Front Insert Type')
    back_insert = fields.Many2one('product.product','Back Insert Type')
    insert_only = fields.Many2one('product.product','Insert')
    
    @api.onchange('partner_id')
    def onchange_customer(self):
        if self.partner_id:
            obj = self.env['res.partner'].browse(self.partner_id.id)
            self.partner_invoice_id = None
            self.partner_shipping_id = None
            for record in obj:
                self.lead_time = record.sale_delay.id
                self.payment_term =record.property_supplier_payment_term.id
                self.carrier_id = record.property_delivery_carrier
                self.shipping_id = record.id
                self.customer_notes = record.comment
                for child in record.child_ids:
                    if child.type == 'invoice':
                        self.partner_invoice_id = child.id
                    if child.type == 'delivery':
                        self.partner_shipping_id = child.id  
                
    @api.onchange('lead_time')
    def onchange_lead_time(self):
        if self.lead_time:
            sale_dela_obj = self.env['edoption.lead.time'].browse(self.lead_time.id)
            for rec in sale_dela_obj:
                self.est_ship_date = (datetime.now() + timedelta(rec.lead_time)).strftime("%Y-%m-%d")
        else:
            self.est_ship_date=None

    @api.onchange('agent_id')
    def onchange_sales_rep(self):
        if self.agent_id:
            sale_agent_obj = self.env['sale.agent'].browse(self.agent_id.id)
            for rec in sale_agent_obj:
                self.commission_id = rec.commission
        else:
            self.est_ship_date=None

    @api.onchange('handling_id')
    def find_expedite_percentage(self):
        if self.handling_id:
            handling_id_value = self.handling_id.value
            amount_untaxed = self.amount_untaxed
            self.expedite = handling_id_value * amount_untaxed

    @api.onchange('discount_type')
    def onchange_discount_type(self):
        if self.discount_type:
            self.discount_percent = self.discount_type.default_discount
            if self.discount_type.default_discount == 0:
                self.discount = 0
            else:
                self.discount = (self.amount_untaxed * self.discount_percent)/100
    
    @api.onchange('discount_percent')
    def onchange_discount_percent(self):
        if self.discount_percent:
#            self.discount = (self.amount_untaxed * self.discount_percent)/100
            self.write({'discount' : (self.amount_untaxed * self.discount_percent)/100 })
#    @api.one
#    @api.depends('order_line.unit_price','order_line.tax_id','order_line.discount','order_line.product_uom_qty')
#    def find_total(self):
#        self.amount_total = self.amount_untaxed - self.discount + self.expedite + self.shipping - self.shipping_discount
#        print "the method is called "
#        print self.amount_total

class replacement_code(models.Model):
    _name = 'replacement.code'
    name = fields.Many2one('replacement.reasoncode','Replacement Code')
    whos_fault = fields.Many2one('replacement.faults','Whos Fault')
    amount = fields.Float('Amount')
    total_amount = fields.Float('Total Amount',compute='find_total')
    sale_order_id = fields.Many2one('sale.order')
    
    @api.depends('amount')
    def find_total(self):
        for record in self:
            record.total_amount = (float(record.sale_order_id.amount_untaxed) * float(record.amount))/100
        return True

class sale_order_line(models.Model):
    _inherit ='sale.order.line'
    
#    def _amount_line(self, cr, uid, ids, field_name, arg, context=None):
#        tax_obj = self.pool.get('account.tax')
#        cur_obj = self.pool.get('res.currency')
#        res = {}
#        if context is None:
#            context = {}
#        for line in self.browse(cr, uid, ids, context=context):
#            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
#            taxes = tax_obj.compute_all(cr, uid, line.tax_id, price, line.product_uom_qty, line.product_id, line.order_id.partner_id)
#            cur = line.order_id.pricelist_id.currency_id
#            res[line.id] = cur_obj.round(cr, uid, cur, taxes['total'])
#        return res
    
    customer_part_no = fields.Char('CPN')
    dummy_width = fields.Float('Width', required=True)
    dummy_height = fields.Float('Height', required=True)
    quant = fields.Integer('Quantity', compute='onchange_product_uom_qty',store = True)
    unit_width = fields.Char('Unit Type')
    is_manul_price = fields.Boolean('Manual Price?')
    is_discount = fields.Boolean('Discountable?')
    fab_image = fields.Binary('Fab Sheet Image')
    glass_fab_image = fields.Binary('Glass Fab Sheet Image')
    notes = fields.Text('Notes')
    
#    Added quant field and this function since quantity should be integer field. if you are able to change the format  in xml tags itself than this field and the function can be removed 
    @api.depends('product_uom_qty')
    def onchange_product_uom_qty(self):
        for record in self:
            if record.product_uom_qty:
                record.quant = record.product_uom_qty
