class res_users(osv.osv):
    _inherit = "res.users"
    _order = 'partner_id asc'
    
res_users()

#    def default_get(self, cr, uid, fields, context=None):
#        data = super(project_issue, self).default_get(cr, uid, fields, context=context)
#        data['project_id'] = context.get('project_id', False)
#        return data
Get the field name in list:::
 if 'date_start' in a.keys():
                        start_date_activity = a['date_start']
XPath:::
	<xpath expr="//field[@name='website']" position="after">
               <field name="accreditation"/>
               <field name="year_of_establishemnt"/>
               <field name="avail_courses"/>
            </xpath>
            <xpath expr="//field[@name='title']" position="after">
               <field name="about_management"/>
            </xpath>
            <xpath expr="//field[@name='title']" position="replace">
            </xpath>
            <!--Hide sales and purchases in view_partner_form view-->
            <xpath expr="//page[@name='sales_purchases']" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//page[@name='accounting']" position="attributes">
                <attribute name="invisible">1</attribute>
            </xpath>
            <xpath expr="//field[@name='parent_id']"  position="after">
               <field name="title" placeholder = "Person Title" />
            </xpath>
            <xpath expr="//page[@name='internal_notes']"  position="after">
               <page name='college_dec' string="College Description">
                   <field name="college_dec" placeholder="Put a Description Here..."/>
               </page>
            </xpath>
			<!--Susai  -->
				<xpath expr="//notebook/page[@name='team']" position='after'>
                    <page string="Project Plan">
                        <field name="project_plan_ids">
                            <tree>
                                <field name="name" />
                                <field name="team_lead_id" />
                                <field name="date_start" />
                                <field name="date_end"  />
                            </tree>
                        </field>
                    </page>
                 </xpath>
                    <!--End  -->
			
			
			
			
class initiative_sequence(osv.osv):
    _name = "initiative.sequence"

    def onchange_project(self, cr, uid, ids, field, context=None):
        val = {}; allprojects = [];
        if field:
            projects = self.pool.get('project.project').browse(cr, uid, field)
            parent_project = self.pool.get('project.project').search(cr, uid, [('parent_project_id', 'ilike', projects.name)])
            for project in self.pool.get('project.project').browse(cr, uid, parent_project):
                values = {
                    'project_id':project.id,
                    'sequence':project.sequence or 0,
                }
                allprojects.append((0, 0, values))
            print allprojects
            if allprojects:
                val = {'child_ids':allprojects}
            else:
                val = {'child_ids':None}
                #raise osv.except_osv(_('Child Projects'), _("There is not child projects for %s project...!")%(projects.name))
        return {'value': val}

    _columns = {
        'project_id': fields.many2one('project.project', 'Project'),
        'record_id': fields.char('Record Id'),
        'child_ids': fields.one2many('initiative.sequence.line', 'initiative_id', 'Child Projects'),

    }
    def update_sequnce(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids):
            for project in record.child_ids:
                self.pool.get('project.project').write(cr, uid,[project.project_id.id], {'sequence': project.sequence})
        return
initiative_sequence()

class initiative_sequence_line(osv.osv):
    _name = 'initiative.sequence.line'

    _columns={
        'project_id': fields.many2one('project.project', 'Project'),
        'sequence': fields.integer('Sequence'),
        'initiative_id': fields.many2one('Initiative')
    }

initiative_sequence_line()



<record id="view_initiative_sequence_form" model="ir.ui.view">
            <field name="name">initiative.sequence.form</field>
            <field name="model">initiative.sequence</field>
            <field name="arch" type="xml">
                <form string="Initiative Sequence" create="false" edit="false">
                    <header><button name="update_sequnce" string="Update Sequence" type="object" icon="gtk-apply" /></header>
                	<group>
                        <field name="project_id" on_change="onchange_project(project_id)"/>
                        <field name="child_ids" nolabel="1" colspan="4">
                            <tree string="Child Projects" editable="bottom">
                                <field name="sequence"/>
                                <field name="project_id"/>
                            </tree>
                        </field>
                	</group>
                </form>
            </field>
        </record>
        <record id="action_initiative_sequence" model="ir.actions.act_window">
            <field name="name">Initiative Sequence</field>
            <field name="res_model">initiative.sequence</field>
            <field name="view_mode">form</field>
        </record>
        <menuitem action="action_initiative_sequence" name="Initiative Sequence" id="initiative_sequence_menu" parent="project.menu_project_management" sequence="7" />
		
		
		
		
		  activity_template = self.pool.get('activity.template').browse(cr, uid, ids, context)
#        for act_id in self.browse(cr, uid, ids, context):
#            print act_id
#        for act in activity_template:
#            print act.is_default
#        if is_default == True:
#            activity_ids=self.search_count(cr, uid, [('is_default', '=', uid)], context=context)
#            if activity_ids >0:
#                raise osv.except_osv(_('Alert'), _('You can choose only one template as a default'))
#        return True










def write(self, cr, uid, ids, vals, context=None):
        state_ids = {}
        state_ids = vals.get('state_ids',None)
        if state_ids:
            for states in state_ids:
                if not state_ids:
                    raise osv.except_osv(_('Alert'),_('Activity template stages can not be empty'))
#        if vals.get('is_default') == True:
#            activity_ids=self.search_count(cr, uid, [('is_default', '=', uid)], context=context)
#            if activity_ids ==1:
#                raise osv.except_osv(_('Alert'), _('You can choose only one template as a default'))
        return super(activity_template, self).write(cr, uid, ids, vals, context)
		
		
def onchange_is_default(self, cr, uid, ids, is_default, context=None):
        if is_default:
            for record in self.browse(cr, uid, self.search(cr, uid, [('is_default', '=', is_default)])):
                self.write(cr, uid, record.id, {'is_default':False})
        return True		
		
		
		
Gantt view inside the tree view:

<button name="%(action_project_task_wizard)d" string="Gantt"
							type="action" context="{'activity_ids':activity_ids}" />


<record id="view_project_task_gantt" model="ir.ui.view">
			<field name="name">project.task.gantt</field>
			<field name="model">project.task</field>
			<field name="arch" type="xml">
				<gantt create="false" delete="false" edit="false" date_stop="date_end"
					color="user_id" date_start="date_start" string="Activities"
					progress="progress" default_group_by="project_id">
				</gantt>
			</field>
		</record>


		<record id="action_project_task_wizard" model="ir.actions.act_window">
			<field name="name">Activities</field>
			<field name="type">ir.actions.act_window</field>
			<field name="view_id" ref="view_project_task_gantt" />
			<field name="res_model">project.task</field>
			<field name="view_type">form</field>
			<field name="view_mode">gantt</field>
			<field name="target">new</field>
		</record>
