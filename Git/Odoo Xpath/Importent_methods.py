Calculate size of direcotry structure recursion method
----------------------------------------------------------------------------

def _get_size(self, cr, uid, dir_id):
        size = 0
        attach_obj = self.pool.get('ir.attachment')
        file_ids = attach_obj.search(cr, uid, [('parent_id', '=', dir_id)])
        for f in attach_obj.browse(cr, uid, file_ids):
            size += f.file_size or 0
        child_ids = self.search(cr, uid, [('parent_id', '=', dir_id)])
        for child_id in child_ids:
            size += self._get_size(cr, uid, child_id)
        return size
    
def _size_calc(self, cr, uid, ids, name, args, context=None):
	""" Finds size of the direcotry.
	@param name: Name of field.
	@param args none:
	@return: Dictionary of values.
	"""
	result = {}
	for dir in self.browse(cr, uid, ids, context=context):
		result[dir.id] = self._get_size(cr, uid, dir.id)
	return result
		
		
'size': fields.function(_size_calc, type='float', string='Total Size'),

Create function one object to another::

@api.model
    def create(self, vals):
        vals.update({'name':self.env['ir.sequence'].get('materials.receiving')})
        accepted_quantities = vals.get('material_ids')
        for accepted_qty in accepted_quantities:
            material_id= accepted_qty[2]['material_id']
            material_obj = self.env['material.material'].search([('id', '=', material_id )])
            material_qty=material_obj.available_units
            total= accepted_qty[2]['accepted_qty'] + material_qty
            self.env['material.material'].browse([material_id]).write({'available_units':total})
        return super(MaterialReceiving, self).create(vals)
		
	def write(self, cr, uid,ids, vals, context=None):
#		vals['num1'] = vals['num1'] + 10
		value = self.pool.get('student').search(cr,uid,[('name','like','susai')])
		for stu in self.pool.get('student').browse(cr, uid, value):
			vals['title'] = stu.name
			return super(test, self).write(cr, uid,ids, vals, context=None)
			
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        vals.update({'user_name': vals.get('name', None),'phone_no':vals.get('phone',None),
                     'mobile_no':vals.get('mobile',None),'email_id':vals.get('email',None),'user_role':vals.get('user',None)}),
        vals.update({'customer_name':vals.get('customer',False),'supplier_name':vals.get('supplier',False)})
        return super(res_partner, self).create(cr, uid, vals, context=None)
(first the changintg field vals.get(the other object field ,validation)(False is the check box)			
			
	def write(self, cr, uid, ids, values, context = None):
   res = super(MyChildClass, self).write(cr, uid, ids, values, context = context)
   if 'child_field' in values:
      for child_item in self.browse(cr, uid, ids, context = context):
          self.pool.get('my.parent.model').write(cr, uid, [child_item.parent_id.id], {'parent_field': values['child_field'],}, context = context) 

   return res

	def write(self, cr, uid, ids, vals, context=None):
        state1 = self.browse(cr, uid, ids).state
        state2 = vals.get('state',None)
        date_start = self.browse(cr, uid, ids).date_start
        date_end = self.browse(cr, uid, ids).date_end
        res = super(initiative_proposal, self).write(cr, uid,ids, vals, context=None)
        if state1 not in ['approval','decline'] and state2 == 'approval':
            if (not date_start) or (not date_end):
                raise osv.except_osv(_('Validate Error'), _('Start Date or End Date Missing'))
            if date_start > date_end:
                raise osv.except_osv(_('Validate Error'), _('Start Date is Greater than End Date'))    
            for stu in self.pool.get('initiative.proposal').browse(cr, uid, ids, context=None):
                vals['name']=str(stu.name)
                vals['team_lead_id']=stu.team_lead_id.id
                vals['date_start']=stu.date_start
                vals['date_end']=stu.date_end
                vals['caution_day']=stu.caution_day
                vals['department_id']=stu.department_id.id
                vals['initiative_type_id']=stu.initiative_type_id.id
                vals['initiative_category_id']=stu.initiative_category_id.id
                vals.pop('state')
                record=[]
                for objectives in stu.objective_ids:
                    record.append([6,False,[objectives.id]])
                vals['objective_ids']=record    
                self.pool.get('project.project').create(cr, uid, vals, context=None)
        if state1 == 'approval' and state2 == state1:
                vals.update({'name': vals.get('name', None)})
                self.pool.get('project.project').create(cr, uid, vals, context=None)
        return res
			
Create:			
			
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        vals['join_date'] = datetime.today()       
        return super(student, self).create(cr, uid, vals, context=None)
		
	def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
            vals.update({'user_name': str(vals['name']),'phone_no':str(vals['phone']),
                     'mobile_no':str(vals['mobile']),'email_id':str(vals['email']),'user_role':str(vals['user']),
                     'customer_name':str(vals['customer']),'supplier_name':str(vals['supplier'])}),
        return super(res_partner, self).create(cr, uid, vals, context=None)	

name_get,concatenate:
		
		
	def name_get(self, cr, uid, ids, context=None):
		if not ids:
			return []
			res = []
		for record in self.read(cr, uid, ids, ['student_name','name'], context=context):
			if record['name']:
			print record['name'][1]
			name = "%s (%s)" % (str(record['student_name']), str(record['name'][1]))
			res.append((record['id'],name ))
		return res
		
	witget="radio";
name_get:
	def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        res = []
        for record in self.read(cr, uid, ids, ['student_id'], context=context):
            if record.get('student_id', False):
                studen_id = "%s" % (str(record['student_id'][1]))
                res.append((record['id'],studen_id ))
        return resnote
		
on_change:

	def onchange_activity_stage(self, cr, uid, ids, activity_temp_state_id, context=None):
        val = {}
        if activity_temp_state_id:
            percentage = self.pool.get('activity.template.state').browse(cr, uid, activity_temp_state_id)
            per_completion = percentage.percentage_of_completion
            val = {
                   'per_completion': per_completion,
                   }
        return {'value': val}



	def onchange_student_name(self, cr, uid, ids, stu_id, context=None):
        val = {}
        if stu_id:
            mark_id = self.pool.get('student.course').browse(cr, uid, stu_id)
            val = {
                   'percentage': mark_id.percentage,
                   'grade':mark_id.grade,
                   }
        return {'value': val}
	
	def onchange_dob(self, cr, uid, ids, dob, context=None):
        val = {}
        if dob:
            val = { 'age' : datetime.date.today().year - datetime.datetime.strptime(dob, '%Y-%m-%d').date().year }
        return {'value': val}
		
		
records(0) to name::


  def _get_milestone_name(self, cr, uid, ids, fieldname, args, context=None):
        res = {};milestone_names =''
        for rec in self.browse(cr, uid, ids):
            for mileston_id in rec.mileston_ids:
                if milestone_names:    
                    milestone_names += ', ' + mileston_id.milestone_id.name
                else:
                    milestone_names = mileston_id.milestone_id.name
            res[rec.id] = milestone_names
        return res

	
	
On_change xml:

		on_change="onchange_student_name(student_id)"
		
		options="{'no_create':'1','no_edit':'1'}"
		
	

	
	burnur account:
		tpeac gziei aduld kylcs
		
		
function fields:


   def _get_total(self, cr, uid, ids, name, arg, context=None):
        res = dict.fromkeys(ids, False)
        if name:
            for rec in self.browse(cr, uid, ids):
                m=(rec.anatomy+rec.biochemistry+rec.microbiology+rec.community_medicine+rec.anesthesiology)
                res[rec.id] =m
        return res
    def _get_percentage(self, cr, uid, ids, name, arg, context=None):
        res = dict.fromkeys(ids, False)
        if name:
            for rec in self.browse(cr, uid, ids):
                m=(rec.total)/10
                res[rec.id] =m
        return res
    
    def _get_grade(self, cr, uid, ids, grade, arg, context=None):
        res = dict.fromkeys(ids, False)
        grade = False
        for rec in self.browse(cr, uid, ids):
            if (rec.percentage >= 90) and (rec.percentage <= 100):
                grade = "a_plus"
            elif (rec.percentage >= 60) and (rec.percentage < 90):
                grade = "a"
            elif (rec.percentage >= 40) and (rec.percentage < 60):
                grade = "b"
            elif (rec.percentage < 40):
                grade = "c"
            res[rec.id] = grade
        return res
		
		
get age::


    def _get_age(self, cr, uid, ids, dob, arg, context=None):
        res = dict.fromkeys(ids, False)
        today = date.today()
        if dob:
            for rec in self.browse(cr, uid, ids):
                dob = datetime.strptime(rec.dob, '%Y-%m-%d').date()
                delta = today - dob
                days = delta.days
                months = (delta.days/365) * 12
                year = today.year - dob.year
                if days>1:
                    res[rec.id] = "%s Day(s), %s Month(s)  , %s Year(s)" % (days, months, year)
                elif days<=0:
                    res[rec.id] = "You are not yet born"
                else:
                    res[rec.id] = "%s Day, %s Month , %s Year" % (days, months, year)
        return res
    
    def _get_age1(self, cr, uid, ids, dob, arg, context=None):
        res = dict.fromkeys(ids, False)
        today = date.today()
        if dob:
            for rec in self.browse(cr, uid, ids):
                dob = datetime.strptime(rec.dob, '%Y-%m-%d').date()
                res[rec.id] = today.year - dob.year
        return res

function field take the one class field to other class::
	def _get_total(self, cr, uid, ids, name, args, context=None):
        res = dict.fromkeys(ids, False)
        total=0
        for rec in self.browse(cr, uid, ids):
            for ttl in rec.discount_ids:
                count_ob = ttl.amount
                if count_ob:
                    total=total+(count_ob)
        res[rec.id] = total
        return res
##################		
attrs="{'readonly':[('is_system_admin_group','=',False),('is_executive_group','=',False),('is_lead_active_user','!=',True),('is_assigned_to','!=',True)]}"

    def _is_assigned_to(self, cr, uid, ids, fieldname, args, context=None):
        res = {}
        ''' Checking whether current user is Team Member or not '''            
        is_user_group = False
        user = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'project', 'group_project_user')
        if user:
            val = self.pool.get('res.users').read(cr, uid, [uid], ['groups_id'], context=context)[0]['groups_id']
            for record in self.browse(cr, uid, ids, context=context):
                if record.assigned_to.id == uid:
                        res[record.id] = True
                else:
                    res[record.id] = False
        return res
    
        'is_assigned_to': fields.function(_is_assigned_to, type="boolean", string='Assigned to user'),

###################################		
	def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        user_id = []
        member = context.get('members', False)
        res = super(project_task, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        if member:
            for record in member[0][2]:
                user_id.append(record)
            doc = etree.XML(res['arch'])
            for field in res['fields']:
                if field == 'assigned_to':
                    res['fields'][field]['domain'] = [('id','in',user_id)]
        return res
    
    
    def _get_total(self, cr, uid, ids, name, args, context=None):
        res = {}; total = 0 ; 
        for rp in self.browse(cr, uid, ids):
            for am in rp.discount_ids:
                total += am.amount
            res[rp.id] = total
        return res
	def default_get(self, cr, uid, fields, context=None):
        data = super(project_issue, self).default_get(cr, uid, fields, context=context)
        task_id = context.get('project_id', None)
        if task_id:
            task = self.pool.get('project.task').browse(cr, uid, task_id)
            project = self.pool.get('project.project').browse(cr, uid, task_id)
            if task.name:
                data['activity'] = task.name
                data['project_id'] = project.id
        return data
Related method::
			'total_ids':fields.related('total_id','total',relation='discount',type='many2one',string='Total'),
		current class many2one field,the other class field name that you need ,other class object name,type text or char
			then string.


Create the msg in inbox put in create method::

post_vars = {'subject': "Message subject",
             'body': "Message body",
             'partner_ids': [(4, 3)],} # Where "4" adds the ID to the list 
                                       # of followers and "3" is the partner ID 
thread_pool = self.pool.get('mail.thread')
thread_pool.message_post(
        cr, uid, False,
        type="notification",
        subtype="mt_comment",
        context=context,
        **post_vars)		


Apply domain filter for the many2one field:::

@api.onchange('place')
def onchange_place(self):
    res = {}
    if self.place:
        res['domain'] = {'asset_catg_id': [('place_id', '=', self.place.id)]}
    return res
Load One2many fields value using default_get::

@api.model
    def default_get(self, fields_name):
        receiving_type = [];
        data = super(MaterialReceiving, self).default_get(fields_name)
        for record in self.env['receiving.attachment.type'].search([]):
            if record.id != self.env['receiving.attachment'].search([('id', '=', record.id )]).id:
                receiving_type.append((0, 0,{'receiving_attach_type_id': record.id}))
            else:
                receiving_type.append((0, 0,{'receiving_attach_type_id': record.id}))
            data['receiving_attachment_ids'] = receiving_type
        return data
    
    @api.model
    def default_get(self, fields_name):
        res = super(MaterialReceiving, self).default_get(fields_name)
        attachment_types = self.env['receiving.attachment.type'].search([])
        receiving_attachment = self.env['receiving.attachment']
        data = []
        for attachment_type in attachment_types:
            attachment = receiving_attachment.create({
                'receiving_attach_type_id': attachment_type.id,
            })
            data.append(attachment.id)
        res['receiving_attachment_ids'] = [(6, False, data)]
        return res	
		
Send Notifications::
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