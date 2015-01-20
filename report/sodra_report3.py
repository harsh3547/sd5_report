import time
from datetime import datetime,timedelta
from openerp.report import report_sxw
from openerp.osv import osv
from openerp.tools.translate import _


class sd5_3_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(sd5_3_report, self).__init__(cr, uid, name, context=context)
        print context
        self.localcontext.update({'id':context.get('active_id'),
                                  'today':time.strftime("%m-%d-%y"),
                                  'len':self._len,
                                  'cr':cr,
                                  'uid': uid,
                                  'get_user_address':self.get_user_address,
                                  'quarter':self.quarter
                                  })
    def get_user_address(self,id):
        cr=self.cr
        uid=self.uid
        #print "user id printing the report ",uid
        obj=self.pool.get('sodra.report.setting').browse(cr,uid,id)
        address=''
        if obj:
            address=(obj.street or '')+' '+(obj.street2 or '')+' '+(obj.city or '')+' '+(obj.state_id.name or '')+' '+(obj.zip or '')
        return str(address)
    
    def _len(self,string):
        return len(string)
    
    def quarter(self,id):
        cr=self.cr
        uid=self.uid
        obj=self.pool.get('account.period').browse(cr,uid,id)
        date=obj.date_start
        print date
        date=date.split('-')
        print date
        date=date[1]
        print date
        print type(date)
        date=int(date)
        i=date / 3
        if i<=1:
            q=1
        elif(i>1 and i<=2):
            q=2
        elif(i>2 and i<=3):
            q=3
        else:
            q=4    
        print q
        return q
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
