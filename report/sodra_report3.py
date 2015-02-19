import time
from datetime import datetime,timedelta
from openerp.report import report_sxw
from openerp.osv import osv
from openerp.tools.translate import _
#from aifc import data


class sd5_3_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(sd5_3_report, self).__init__(cr, uid, name, context=context)
        print context
        self.localcontext.update({'id':context.get('active_id'),
                                  'today':time.strftime("%Y%m%d"),
                                  'date':time.strftime("%Y%m%d"),
                                  'len':self._len,
                                  'int':self._int,
                                  'strings':self._strings,
                                  'cr':cr,
                                  'uid': uid,
                                  'get_user_address':self.get_user_address,
                                  'quarter':self.quarter,
                                  'employee_hire':self.employee_hire,
                                  'employee_fire':self.employee_fire,
                                  'id_hire':self.id_hire,
                                  'id_fire':self.id_fire,
                                  'hire_pages':self.hire_pages,
                                  'fire_pages':self.fire_pages,
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
    
    def _int(self,string):
        return int(string)
    
    
    def _strings(self,string):
        return str(string)
    
    '''def employee_datas(self,ids):
        cr=self.cr
        uid=self.uid
        obj=self.pool.get('hr.employee')
        id=obj.search(cr,uid,[],context=None)
        identifications=[]
        otherid=[]
        datas=[]
        for i in id:
            browse_obj=obj.browse(cr,uid,i)
            identification=browse_obj.identification_id
            other=browse_obj.otherid
            otherid.append(other)
            identifications.append(identification)
        datas=[identifications,otherid]
        return datas'''
    
    def employee_hire(self,ids):
        print "----------------ids",ids
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_start', '>=', sodra_date_start),('date_start','<=',sodra_date_stop)],context=None)
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        identifications=[]
        otherid=[]
        datas=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            employee_id.append(employee_ids)
        for j in employee_id:
            object_employee_browse=object_employee.browse(cr,uid,j)
            identification=object_employee_browse.identification_id
            other=object_employee_browse.otherid
            if other: 
                otherid.append(other)
            if identification:
                identifications.append(identification)
        datas=[identifications,otherid]
        return datas
    
    
    def id_hire(self,ids):
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_start', '>=', sodra_date_start),('date_start','<=',sodra_date_stop)],context=None)
        print"----------------------------",id
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            print"-----------------------------employee_ids",employee_ids
            print"----------------------------iiiiiiiii",i
            employee_id.append(employee_ids)
        print"-----------------------------",employee_id
        return employee_id 
    
    
    def hire_pages(self,ids):
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_start', '>=', sodra_date_start),('date_start','<=',sodra_date_stop)],context=None)
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            employee_id.append(employee_ids)
        idlen=len(employee_id)/9
        idrem=len(employee_id)%9
        if idrem > 0:
            idlen=idlen+1
        return idlen
    
    
    def employee_fire(self,ids):
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_end','>=', sodra_date_start),('date_end','<=',sodra_date_stop)],context=None)
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        identifications=[]
        otherid=[]
        datas=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            employee_id.append(employee_ids)
        for j in employee_id:
            object_employee_browse=object_employee.browse(cr,uid,j)
            identification=object_employee_browse.identification_id
            other=object_employee_browse.otherid
            if other: 
                otherid.append(other)
            if identification:
                identifications.append(identification)
        datas=[identifications,otherid]
        return datas
    
    def id_fire(self,ids):
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_end','>=', sodra_date_start),('date_end','<=',sodra_date_stop)],context=None)
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            employee_id.append(employee_ids)
        return employee_id
    
    def fire_pages(self,ids):
        cr=self.cr
        uid=self.uid
        object_sodra=self.pool.get("account.period").browse(cr,uid,ids)
        sodra_date_start=object_sodra.date_start
        sodra_date_stop=object_sodra.date_stop
        print"========================sodra_date_start",sodra_date_start
        print"========================sodra_date_stop",sodra_date_stop
        object_contract=self.pool.get("hr.contract")
        id=object_contract.search(cr,uid,[('date_end','>=', sodra_date_start),('date_end','<=',sodra_date_stop)],context=None)
        object_employee=self.pool.get('hr.employee')
        employee_id=[]
        for i in id:
            object_contract_browse=object_contract.browse(cr,uid,i).employee_id
            employee_ids=object_contract_browse.id
            employee_id.append(employee_ids)
        idlen=len(employee_id)/4
        idrem=len(employee_id)%4
        if idrem > 0:
            idlen=idlen+1
        return idlen
    
        
    def quarter(self,id):
        print "--------------id",id
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
                
    
    '''def employee_id(self,ids):
        cr=self.cr
        uid=self.uid
        obj=self.pool.get('hr.employee')
        id=obj.search(cr,uid,[],context=None)
        return id'''
    
'''  def id(self,ids):
        cr=self.cr
        uid=self.uid
        obj=self.pool.get('hr.employee')
        id=obj.search(cr,uid,[],context=None)
        idlen=len(id)/9
        idrem=len(id)%9
        if idrem > 0:
            idlen=idlen+1
        return idlen
    
    def SDP_id(self,ids):
        cr=self.cr
        uid=self.uid
        obj=self.pool.get('hr.employee')
        id=obj.search(cr,uid,[],context=None)
        idlen=len(id)/4
        idrem=len(id)%4
        if idrem > 0:
            idlen=idlen+1
        return idlen'''
        
    
   
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
