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
	
Upload many2many field::

def load_acces_rights(self, cr, uid, ids, context=None):

        access = [];list_menu_ids=[]; values = {}
        parent_menu_id = self.pool.get('ir.ui.menu').search(cr,uid,[('name', '=', 'KnowSpace'),('parent_id', '=', None)],context=context)
        menu_obj = self.pool.get('ir.ui.menu').browse(cr, uid, parent_menu_id)
        if menu_obj:
            list_menu_ids.append(menu_obj.id)
            menu_ids = self.pool.get('ir.ui.menu').search(cr,uid,[('parent_id', '=', menu_obj.id)],context=context)
            for menu_id in menu_ids:
                list_menu_ids.append(menu_id)
                sub_menu_ids = self.pool.get('ir.ui.menu').search(cr,uid,[('parent_id', '=', menu_id)],context=context)
                sub_menu_obj =  self.pool.get('ir.ui.menu').browse(cr, uid, sub_menu_ids)
                if sub_menu_obj:
                    for sub_menu_id in sub_menu_obj:
                        print sub_menu_id.sequence
                        list_menu_ids.append((4,sub_menu_id.id))
        values.update({'menu_access': [(6, 0, list_menu_ids)]})