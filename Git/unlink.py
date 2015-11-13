if stu:
                for ini in self.pool.get('project.project').browse(cr, uid, ids, context=None):
                    if ini.id == stu.id:
                        if old_state in ['decline'] and new_state == 'approval':
        #                    super(initiative_proposal, self).unlink(cr, uid, stu.id, context)
#                            super(project_project, self).unlink(cr, uid, ini.id, context)
                            return self.pool.get('project.project').unlink(cr, uid, ini.id, context=context)
#                            self.env['project.project'].unlink(cr, uid, ini.id, context)