On change::
def onchange_classes(self, cr, uid, ids, class_ids, context=None):
        update_users = []; values = {}
        if class_ids[0][2]:
            class_ids = class_ids[0][2]
            for class_id in class_ids:
                users = self.pool.get('res.partner').browse(cr, uid,(self.pool.get('res.partner').search(cr, uid, [('class_id', '=',class_id)], context=context)))
                for record in users:
                    values = {'is_active' : True,'name' : record.name,'reg_no':record.reg_no, 'batch_id':record.batch_id.id, 'class_id':record.class_id.id}
                    update_users.append((0, 0, values))
        return  {'value':{'user_ids':update_users}}
		
To separate keys and values::
	stu_id={a:3,b:4}
	keys = stu_id.keys()
	values = stu_id.values()