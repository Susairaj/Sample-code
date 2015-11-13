def onchange_initiative_template(self, cr, uid, ids, project_template_id, members, context=None):
        stage_ids = []
        activity_ids = []; user_id =[]; active_member = []
        caution_day = 2
        stage_stage_obj = self.pool.get('stage.stage')
        if project_template_id:
            template_obj = self.pool.get('project.template').browse(cr, uid, project_template_id)
            if template_obj:
                caution_day = template_obj.caution_day
                """ @purpose: to load stages """
                for stage in template_obj.stage_ids:
                    if stage.stage_id.id:
                        stage_ids.append(stage.stage_id.id)
                """ @purpose: to load activity """
                for member in members[0][2]:
                     user_data = self.pool.get('res.users').browse(cr, uid, member)
                     user_id.append(user_data.id)
                     print user_id
                for activity in template_obj.activity_ids:
                    activity_ids.append((0, 0, {'name': activity.name, 'is_lead_active_user': True,
                                                'is_system_admin_group': 1, 'caution_day': 2, 'members': [[6, 0, user_id]]}))
            return {'domain': {'stage_id': [('id', 'in', stage_ids)]},
                    'value': {'activity_ids': activity_ids, 'caution_day': caution_day, 'stage_id': False,
                              'per_completion': None}}
        else:
            for stage in stage_stage_obj.browse(cr, uid, stage_stage_obj.search(cr, uid, [])):
                stage_ids.append(stage.id)
            return {'domain': {'stage_id': [('id', 'in', stage_ids)]},
                    'value': {'activity_ids': activity_ids, 'caution_day': caution_day, 'stage_id': False,
                              'per_completion': None}}
        return True

    