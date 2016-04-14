<xpath expr="//label[@for='street']" position="before">
	<field name="batch_id" widget="selection" 
	attrs="{'invisible':[('is_type', 'not in', 'student')],'required':[('is_type', 'in', 'student')]}" />
</xpath>
<xpath expr="//field[@name='gender']" position="before">
	<field name="class_id"  domain="[('batch_id','=', batch_id)]" attrs="{'invisible':['|', ('is_type', 'not in', 'student'),('batch_id', '=', False)],'required':[('is_type', 'in', 'student')]}" />
</xpath>
Disable create button using xpath::
<record>
        ...
        <field name="arch" type="xml">
            <xpath expr='//form[@string="Product"]' position='attributes'>
                <attribute name="create">false</attribute>
            </xpath>
        </field> ,
    </record>
	
Filter today,this week, this month::
<filter string="Today" domain="[('create_date','>=', ((context_today()).strftime('%Y-%m-%d'))), ('create_date','&lt;=', ((context_today()).strftime('%Y-%m-%d')))]"/>
<filter string="This Week" domain="[('create_date','&gt;=', ((context_today()).strftime('%%Y-%%m-%%d'))),
 ('create_date','&lt;=', ((context_today()+datetime.timedelta(days=6)).strftime('%%Y-%%m-%%d')))]"/>
<filter string="This Month" domain="[('create_date','&lt;=',(context_today()+relativedelta(day=31)).strftime('%%Y-%%m-%%d')),
('create_date','&gt;=',(context_today()-relativedelta(day=1)).strftime('%%Y-%%m-%%d'))]"/>

How to use options::one2many field
<field name="partner_id" options="{'limit': 10, 'create': false, 'create_edit': false}"/>

Change the line color using xpath::
<xpath expr="//tree[@string='Attachments']" position="attributes">
					<attribute name="colors">orange:state=='request_review';green:type == 'binary'; blue:type =='url'</attribute>
				</xpath>