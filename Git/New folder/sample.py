    def onchange_team_support(self, cr, uid, ids, team_support_ids, members, context=None):
        val = {}
        if members[0][2]!=[]:
                existing_members=members[0][2]
                val = {
                        'members': existing_members
                }
            
        if team_support_ids[0][2]!=[]:
            team_members=team_support_ids[0][2]
            if existing_members[0] not in team_members: 
                team_members.append(existing_members[0])
            for new_team_members in team_members:
                    val = {
                   'members': team_members,
                   }
    
        return {'value': val} 
		
		on_change="onchange_team_support(team_support_ids,members)"