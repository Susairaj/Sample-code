Create and Write methods one2many field instead of one2many:::
	def create(self, cr, uid, vals, context=None):
        name=vals.get('name')
        responsibility_users=vals.get('responsibility_ids',None)
        date_start=vals.get('date_start')
        date_end=vals.get('date_end')
        project_id=vals.get('project_id')
#        Convert string date to date format
        act_start_date= datetime.strptime(date_start, "%Y-%m-%d").date()
        act_end_date= datetime.strptime(date_end, "%Y-%m-%d").date()
        if responsibility_users:
            list_users=None
            for res_user_id in responsibility_users:
                user_id=res_user_id[2].get('name')
                user_id=self.pool.get('res.users').search(cr, uid, [('id', '=',user_id)], context=context)
                user_obj=self.pool.get('res.users').browse(cr, uid, user_id, context)
                if user_obj:
                    if list_users == None:
                        list_users=str(user_obj.name)
                    else:
                        list_users=str(list_users)+','+ str(user_obj.name)
            vals.update({'rsp_user':list_users})
        if not responsibility_users:
            raise osv.except_osv(_('Validate Error'), _('Choose or create new responsibility user for %s.') % (name))
#        Get project start date and end date
        project_id=self.pool.get('project.project').search(cr, uid, [('id', '=',project_id)], context=context)
        project_obj=self.pool.get('project.project').browse(cr, uid, project_id, context)
#        Convert string date to date 
        if project_obj:
            project_date_end= datetime.strptime(project_obj.date, "%Y-%m-%d").date()
            project_date_start= datetime.strptime(project_obj.date_start, "%Y-%m-%d").date()
#            Validate activity date range
            if project_date_start > act_start_date:
                raise osv.except_osv(_('Validate Error'), _('Activity %s start date is less than project start date')% (name))
            if project_date_end < act_end_date:
                raise osv.except_osv(_('Validate Error'), _('Activity %s end date is greater than project end date')% (name))
        if act_start_date > act_end_date:
            raise osv.except_osv(_('Validate Error'), _('Activity %s End Date should be greater than Start Date.')% (name))
        return super(project_task, self).create(cr, uid, vals, context=None)
    
    
    def write(self, cr, uid, ids, vals, context=None):
        
        if not vals.get('message_last_post'):
            responsibility_users=vals.get('responsibility_ids',None)
            if responsibility_users:
                added_users=[]
                activity_user_id=[]
                list_users=None
                activity_obj=self.browse(cr, uid, ids, context)
                exitst_user_ids=activity_obj.responsibility_ids
                if exitst_user_ids:
                    res_list_user_ids=[]
                    for res_user_id in exitst_user_ids:
                        res_list_user_ids.append(res_user_id.name.id)
                for activity_res_user in responsibility_users:
                    if activity_res_user[2] != False:
                        activity_user_id.append(activity_res_user[2].get('name'))
                        added_users=list(set(activity_user_id) - set(res_list_user_ids))
                    else:
                        act_user_id=self.pool.get('activity.users').search(cr, uid, [('id', '=',activity_res_user[1])], context=context)
                        act_user_obj=self.pool.get('activity.users').browse(cr, uid, act_user_id, context)
                        user_id=self.pool.get('res.users').search(cr, uid, [('id', '=',act_user_obj.name.id)], context=context)
                        user_obj=self.pool.get('res.users').browse(cr, uid, user_id, context)
                        if user_obj:
                            if list_users == None:
                                list_users=str(user_obj.name)
                            else:
                                list_users=str(list_users)+','+ str(user_obj.name)
                if added_users:
                    for new_user_id in added_users:
                        act_user_id=self.pool.get('res.users').search(cr, uid, [('id', '=',new_user_id)], context=context)
                        user_obj=self.pool.get('res.users').browse(cr, uid, act_user_id, context)
                        if user_obj:
                            if list_users == None:
                                list_users=str(user_obj.name)
                            else:
                                list_users=str(list_users)+','+ str(user_obj.name)
                        vals.update({'rsp_user':list_users})
#        Browse project start date and end date
            project_task_obj=self.pool.get('project.task').browse(cr, uid, ids, context)
            project_id=self.pool.get('project.project').search(cr, uid, [('id', '=',project_task_obj.project_id.id)], context=context)
            project_obj=self.pool.get('project.project').browse(cr, uid, project_id, context)
#        Get currnet updated values
            date_start=vals.get('date_start',None)
            date_end=vals.get('date_end',None)
            if date_end != None and date_start != None:
#        Convert string date to date format
                act_start_date= datetime.strptime(date_start, "%Y-%m-%d").date()
                act_end_date= datetime.strptime(date_end, "%Y-%m-%d").date()
#        Validate activity date range
                if act_start_date > act_end_date:
                    raise osv.except_osv(_('Validate Error'), _('Activity end date should be greater than Start Date'))
            if project_obj:
#        Get Values from project object
                project_date_end=project_obj.date
                project_date_start=project_obj.date_start
                if date_start != None:
#        Convert string date to date format
                    act_start_date= datetime.strptime(date_start, "%Y-%m-%d").date()
                    project_date_start= datetime.strptime(project_date_start, "%Y-%m-%d").date()
                    if project_date_start > act_start_date:
                        raise osv.except_osv(_('Validate Error'), _('Activity start date is less than project start date'))
                if date_end != None:
#        Convert string date to date format
                    act_end_date= datetime.strptime(date_end, "%Y-%m-%d").date()
                    project_date_end= datetime.strptime(project_date_end, "%Y-%m-%d").date()
                    if project_date_end < act_end_date:
                        raise osv.except_osv(_('Validate Error'), _('Activity end date is greater than project end date'))
        return super(project_task, self).write(cr, uid, ids, vals, context=context)