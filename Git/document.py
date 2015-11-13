# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
import zipfile ,base64 

class document_document(osv.osv):
    _name = "document.document"
    
    def default_get(self, cr, uid, fields, context=None):
        data = super(document_document, self).default_get(cr, uid, fields, context=context)
        task_id = context.get('active_id', False)
        values = []
        if task_id:
            task = self.pool.get('project.task').browse(cr, uid, task_id)
            for record in task.attachment_ids:
                values.append((0, 0, {'file_id': record.id,'file_name':record.datas_fname}))
            data['document_ids'] = values
        return data
    
    def download_zip(self, cr, uid, ids, context=None):
        if context.get('active_model', False):
            active_id = context.get('active_id', False)
            model = context.get('active_model')
            filename = self.pool.get(model).browse(cr, uid, active_id).name
            # Create zip file
            z = zipfile.ZipFile('/opt/odoo/zipedfiles/%s' % filename, 'w')
            any_file = False
            for line in self.browse(cr, uid, ids):
                for doc in line.document_ids:
                    if doc.is_attachment:
                        name = doc.file_id.datas_fname
                        z.writestr(name, (doc.file_id.datas).decode('base64'))
                        any_file = True
            # flush and close
            z.close()
            
            if any_file:
                with open(filename, "rb") as f:
                    bytes = f.read()
                    datas = base64.b64encode(bytes)
                attachment_data = {
                    'name': filename + '.zip',
                    'datas_fname': filename + '.zip',
                    'datas': datas,
                    'res_model': model,
                    'file_type': 'application/zip',
                    'res_id': active_id,
                }
                document = self.pool.get('ir.attachment').create(cr, uid, attachment_data, context=context)
                return document 

    
    _columns = {
        'document_ids':fields.one2many('document.line','document_id','Documents'),
    }
    
document_document()

class document_line(osv.osv):
    _name = "document.line"
    
    _columns = {
        'document_id':fields.many2one('document.document', 'Docs ID'),
        'is_attachment':fields.boolean('Select'),
        'file_id':fields.many2one('ir.attachment', 'Attachment Name', readonly=True),
        'file_name':fields.char('File Name'),
    }
    
document_line()

