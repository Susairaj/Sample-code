<xpath expr="//label[@for='street']" position="before">
	<field name="batch_id" widget="selection" 
	attrs="{'invisible':[('is_type', 'not in', 'student')],'required':[('is_type', 'in', 'student')]}" />
</xpath>
<xpath expr="//field[@name='gender']" position="before">
	<field name="class_id"  domain="[('batch_id','=', batch_id)]" attrs="{'invisible':['|', ('is_type', 'not in', 'student'),('batch_id', '=', False)],'required':[('is_type', 'in', 'student')]}" />
</xpath>