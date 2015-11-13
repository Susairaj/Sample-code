def onchange_team_members(self, cr, uid, ids, team_lead_id, team_support_ids, members, context=None):
        if members and members[0][2]:
            temp_members = members[0][2]
        else:
            temp_members = []
        if team_support_ids and team_support_ids[0][2]:
            for i in team_support_ids[0][2]:
                if i not in temp_members:
                    temp_members.append(i)
        if (team_lead_id) and (team_lead_id not in temp_members):
            temp_members.append(team_lead_id)
        return {'value': {'members': [(6, 0, temp_members)]}}
		
		
		
		
 <field name="team_lead_id" widget="selection" placeholder="N/A" attrs="{'readonly':[('is_system_admin_group','=',False),('is_executive_group','=',False)]} " on_change="onchange_team_members(team_lead_id, team_support_ids, members)" context="{'project_id': active_id}" string="Team Lead" />
					<newline />
					<!-- <field name="team_support_ids" widget="many2many_tags" placeholder="N/A" attrs="{'readonly':[('is_system_admin_group','=',False),('is_lead_active_user','=',False)]}" on_change="onchange_team_support(team_support_ids,members)" context="{'project_id': active_id}" /> -->
					<field name="team_support_ids" widget="many2many_tags" placeholder="N/A" attrs="{'readonly':[('is_system_admin_group','=',False),('is_lead_active_user','=',False)]}" on_change="onchange_team_members(team_lead_id, team_support_ids, members)" context="{'project_id': active_id}" />
					<newline />
def onchange_team_members(self, cr, uid, ids, team_lead_id, team_support_ids, members, context=None):
#        if members and members[0][2]:
#            temp_members = members[0][2]
#        else:
#            temp_members = []
#        if team_support_ids and team_support_ids[0][2]:
#            for i in team_support_ids[0][2]:
#                if i not in temp_members:
#                    temp_members.append(int(i))
#        if (team_lead_id) and (team_lead_id not in temp_members):
#            temp_members.append(int(team_lead_id))
#        return {'value': {'members': [(6, 0, temp_members)]}}


#    def onchange_team_support(self, cr, uid, ids, team_support_ids, members, context=None):
#        val = {}
#        existing_members=[]
#        if members[0][2]!=[]:
#            existing_members=members[0][2]
#            val = {
#                    'members': existing_members
#                    }
#        if team_support_ids[0][2]!=[]:
#            team_members=team_support_ids[0][2]
#            if members[0][2]!=[]:
#                for team in team_support_ids:
#                    if team not in team_members:
#                        for i in existing_members:
#                            team_members.append(i)
#                            val = {
#                                 'members': list(set(team_members))
#                              }
#                    else:
#                        raise osv.except_osv(_('Alert'), _('Team lead already exist in Team member list.'))
#                        val={
#                             'members': existing_members
#                             }         
#            else:
#                    val={
#                     'members': list(set(team_members))
#                     }   
#       
#        return {'value': val}





