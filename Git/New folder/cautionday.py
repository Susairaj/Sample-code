   def onchange_initiative_template(self, cr, uid, ids, project_template_id, context=None):
        stages = []
        activity_ids = []
        caution_day=2
        if project_template_id:
            template_obj = self.pool.get('project.template').browse(cr, uid, project_template_id)
            if template_obj:
                caution_day=template_obj.caution_day
                """ @purpose: to load stages """
                for stage in template_obj.stage_ids:
                    stages.append(stage.stage_id.id)
                """ @purpose: to load activity """
                for activity in template_obj.activity_ids:
                    activity_ids.append((0,0,{'name': activity.name,'is_lead_active_user':True,'is_system_admin_group':1,'caution_day':2}))
                
        return {'domain':{'stage_id':[('id','in',stages)]}, 'value': {'activity_ids': activity_ids,'caution_day':caution_day}}