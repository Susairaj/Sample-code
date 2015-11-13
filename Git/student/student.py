'''
Created on Jan 10, 2015

@author: Bosco
'''
from openerp.osv import fields, osv
from bsddb.dbtables import _columns

class student(osv.osv):
    
    
    _name="student"
    _discription="Sample student"
    _columns = {
        'name':fields.char('StudentName', required=True),
        'gender':fields.selection([('male','Male'),('female','Female')],'Gender'),
        'dob':fields.date('DOB'),
        'address':fields.text('Address'),
        'studentdepartment_id':fields.one2many('studentdepartment','student_id','Department')
    }
student()
class studentmark(osv.osv):
    
    
    
    _name="studentmark"
    _discription="Sample"
    
    def _percentage(self,cr,uid,ids,fieldnames,arg,context=None):
        res = {}
        for rec in self.browse(cr,uid,ids,context=context):
            res[rec.id] = (rec.tamil+rec.english+rec.accountancy+rec.fuzzy+rec.intgral_calculas )/5
        return res
    _columns = {
                'student_id':fields.many2one('student','StudentName',required=True),
                'tamil':fields.integer('Tamil'),
                'english':fields.integer('English'),
                'accountancy':fields.integer('Accondency'),
                'fuzzy':fields.integer('Fuzzy'),
                'intgral_calculas':fields.integer('Integral_calculas'),
                'Percentage':fields.function(_percentage,type='integer',store=True),
                
                
                }
studentmark()
class studentdepartment(osv.osv):
    _name="studentdepartment"
    _discription="Sample"
    _columns ={
              'department':fields.selection([('english','English Department'),
('maths','Mathematics Department'),('cs','Computer science Department'),
('electronic','Electronic Department'),('tamil','Tamil Department')],'Department',required=True),
              'student_id':fields.many2one('student','StudentName')
              }
studentdepartment()
    