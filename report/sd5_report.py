import time
from openerp.report import report_sxw
from osv import osv
from openerp.tools.translate import _


class sd5_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        print '********************************* report called sd5'
        print cr,uid,name,context
        super(sd5_report, self).__init__(cr, uid, name, context=context)
        
        self.write_ids(cr, uid,context)
        
        self.localcontext.update({
                                  'time':time,
                                  'cr':cr,
                                  'uid': uid,
                                  'get_user_address':self._get_user_address
                                  })
        
        
    
    def write_ids(self,cr,uid,context=None):
        # set company id for company many2one field
        company_id=self.pool.get('res.users').browse(cr,uid,uid).company_id.id
        employee_records=context.get('active_ids',False)
        for i in employee_records:
            self.pool.get('hr.contract').write(cr,uid,i,{'company':company_id})
            
        contracts=self.pool.get('hr.contract').search(cr,uid,[])
        user_id=self.pool.get('sodra.config').search(cr,uid,[])
        if len(user_id)!=0:
            for i in contracts:
                self.pool.get('hr.contract').write(cr,uid,i,{'sodra':user_id[0]})
        else:
            raise osv.except_osv(_('ERROR !'), _('Please set Sodra Report Settings'))    
        
    
    def _get_user_address(self):
        cr=self.cr
        uid=self.uid
        #print "user id printing the report ",uid
        name=self.pool.get('res.users').browse(cr,uid,uid).name
        user_partner=self.pool.get('res.partner').search(cr,uid,[('name','=',name)])
        #print 'kkkkkkkkkkkkkkkkkkkkk',user_partner
        res_obj=self.pool.get('res.partner').browse(cr,uid,user_partner[0])
        #print '9898696969869888888888888   res_obj',res_obj
        address=(res_obj.name or '')+' '+(res_obj.phone or '')+' '+(res_obj.email or '')
        return address
        

        
report_sxw.report_sxw('report.sd5_report_mod','hr.contract','addons/sd5_report/report/sd5_report.mako',
    parser=sd5_report)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
