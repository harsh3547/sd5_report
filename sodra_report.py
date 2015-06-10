# -*- coding: utf-8 -*-
from openerp.osv import fields, osv,orm
from datetime import date
class sodra_report(osv.osv):
    
    _name = 'sodra.report'
    _description = "sodra report"
    _defaults = {
                 'date': date.today().strftime('%Y-%m-%d'),
                 }
    def create(self,cr,uid,vals,context):
        sequence = self.pool.get('ir.sequence').get(cr,uid,'sodra.report2')
        print "=======================sequqnce",sequence
        vals.update({'sequence':sequence})
        return super(sodra_report,self).create(cr,uid,vals,context)
        
    _columns  = {
                 'name':fields.char(string="Name",size =50,required = True),
                 'setting_id':fields.many2one('sodra.report.setting','Company'),
                 'user_id':fields.many2one("res.users","Users"),
                 'date':fields.date('Date'),
                 'sequence':fields.char('Sequence'),
                 'period_id':fields.many2one('account.period','Period'),
                 'field_1':fields.boolean('Patikslintas pranešimas'),
                 'field_20_1':fields.boolean('priedas SAM3SD(P20.1)'),
                 'field_21_1':fields.boolean('priedas SAM3SDP(P21.1)'),

                 }
    
class sodra_report_setting(osv.osv):
    _name = 'sodra.report.setting'
    _description = "sodra report"
    _defaults = {
                 
                 }
    
    _columns  = {
                 
                 'company_id':fields.many2one('res.company','Company'),
                 'name':fields.related('company_id','name',type='char',string="name"),
                 'company_registry':fields.related('company_id','company_registry',type='char',string="Company Registry"),
                 'sodra_no':fields.related('company_id','sodra_no',type='char',string="Sodra No"),
                 'phone':fields.related('company_id','phone',type='char',string="Phone"),
                 'street':fields.related('company_id','street',type='char',string="Address"),
                 'street2':fields.related('company_id','street2',type='char', string="streeet2"),
                 'city':fields.related('company_id','city',type='char', string="city"),
                 'state_id':fields.related('company_id','state_id',type='many2one', string="State",relation="res.country.state"),
                 'zip':fields.related('company_id','zip',type='char', string="zip"),
                 'field_8':fields.text(string='Adresatas',size=68),
                 'tarif_id':fields.float('Tarif'),
                 'field_A11':fields.many2many('hr.salary.rule', 'hr_sodra_one_salary_rule_rel','setting_id','rule_id',string='field A11'),
                 'field_A12':fields.many2many('hr.salary.rule', 'hr_sodra_two_salary_rule_rel','setting_id','rule_id',string='field A12'),
                 }
    
class res_company(osv.osv):
    _inherit = "res.company"
    _description = 'Companies'
    _columns = {
                 'sodra_no':fields.char(string="Sodra No.",size =50),
    
                 }
    