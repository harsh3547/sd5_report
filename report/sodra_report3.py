import time,math
from datetime import datetime,timedelta
from openerp.report import report_sxw
from openerp.osv import osv
from openerp.tools.translate import _
#from aifc import data


class sd5_3_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(sd5_3_report, self).__init__(cr, uid, name, context=context)
        self.context=context
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
                                  'tarif':self._tarif,
                                  'hire':self.hire,
                                  'fire':self.fire,
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
        print "-------------string===",string
        return int(string)
    
    
    def _strings(self,string):
        return str(string)

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
        i=date / 3.0
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
    
    
    def _tarif(self,num):
        num=round(num,2)
        if num<10.0:return '0'+str(num)
        else:return num   
    
    def hire(self,period_id):
        cr=self.cr
        uid=self.uid
        employee_id=[]
        identifications=[]
        otherid=[]
        name=[]
        datas=[]
        field_A11=[]
        field_A12=[]
        total_A11=0.0
        total_A12=0.0
        sodra_id=self.context.get('active_id',False)
        sodra_obj=self.pool.get('sodra.report').browse(cr,uid,sodra_id)
        #print "----------------ids---",id,self
        object_period=self.pool.get("account.period").browse(cr,uid,period_id)
        for obj in object_period:
            period_start=obj.date_start
            period_stop=obj.date_stop
            object_contract=self.pool.get("hr.contract")
            valid_contract_ids=object_contract.search(cr,uid,['|','&',('date_end', '=', False),('date_start','<=',period_stop),'&','&',('date_end', '!=', False),('date_start','<=',period_stop),('date_end','>=',period_stop)],context=None)
            #print"----------def id_hire(self,id):------------------",valid_contract_ids
           
            for i in valid_contract_ids:
                employee_ids=object_contract.browse(cr,uid,i).employee_id.id
                #print"-----------------------------employee_ids",employee_ids
                #print"----------------------------iiiiiiiii",i
                employee_id.append(employee_ids)
            #print"--------------------------employee_id---",employee_id

            obj_payslip=self.pool.get('hr.payslip')
            valid_payslip=obj_payslip.search(cr,uid,[('state','=','draft'),('date_to','>=',period_start),('date_to','<=',period_stop),('employee_id','in',employee_id),('contract_id','in',valid_contract_ids)],context=None) or []
            #print "\n\n\n\n\n===============payslip========",valid_payslip
            no_of_pages=int(math.ceil(len(valid_payslip)/9.0)) if valid_payslip else 0

            code_A11=[i.code for i in sodra_obj.setting_id.field_A11]
            code_A12=[i.code for i in sodra_obj.setting_id.field_A12]
            #print "===field_A11===field_A12=====",field_A11,field_A12,code
            for j in valid_payslip:
                payslip=obj_payslip.browse(cr,uid,j)
                name.append(payslip.employee_id.name or ' ')
                otherid.append(payslip.employee_id.otherid or ' ')
                identifications.append(payslip.employee_id.identification_id or ' ')
                sumA11=0.0
                sumA12=0.0
                for line in payslip.line_ids:
                    if line.code in code_A11: sumA11 += line.total
                    if line.code in code_A12: sumA12 += line.total
                field_A11.append("%.2f"%sumA11)
                field_A12.append("%.2f"%sumA12)
                total_A11 += sumA11
                total_A12 += sumA12
            datas=[identifications,otherid,name,field_A11,field_A12,"%.2f"%total_A11,"%.2f"%total_A12]
            # valid_payslip is list of valid payslips, no_of_pages required to fit the payslips, datas = data of employee of the payslip
            print "-----------final result ----------",no_of_pages,valid_payslip,datas
        return [no_of_pages,valid_payslip,datas] 
    
    
    def fire(self,period_id):
        cr=self.cr
        uid=self.uid
        employee_id=[]
        identifications=[]
        otherid=[]
        name=[]
        start_date=[]
        fire_date=[]
        datas=[]
        field_A11=[]
        field_A12=[]
        total_A11=0.0
        total_A12=0.0
        sodra_id=self.context.get('active_id',False)
        sodra_obj=self.pool.get('sodra.report').browse(cr,uid,sodra_id)
        #print "----------------ids---",id,self
        object_period=self.pool.get("account.period").browse(cr,uid,period_id)
        for obj in object_period:
            period_start=obj.date_start
            period_stop=obj.date_stop
            object_contract=self.pool.get("hr.contract")
            valid_contract_ids=object_contract.search(cr,uid,[('date_end', '!=', False),('date_start','<=',period_stop),('date_end', '>=', period_start),('date_end','<=',period_stop)],context=None)
            #print"----------def id_hire(self,id):------------------",valid_contract_ids
           
            for i in valid_contract_ids:
                employee_ids=object_contract.browse(cr,uid,i).employee_id.id
                #print"-----------------------------employee_ids",employee_ids
                #print"----------------------------iiiiiiiii",i
                employee_id.append(employee_ids)
            #print"--------------------------employee_id---",employee_id

            obj_payslip=self.pool.get('hr.payslip')
            valid_payslip=obj_payslip.search(cr,uid,[('state','=','draft'),('date_to','>=',period_start),('date_to','<=',period_stop),('employee_id','in',employee_id),('contract_id','in',valid_contract_ids)],context=None) or []
            #print "\n\n\n\n\n===============payslip========",valid_payslip
            no_of_pages=int(math.ceil(len(valid_payslip)/4.0)) if valid_payslip else 0

            code_A11=[i.code for i in sodra_obj.setting_id.field_A11]
            code_A12=[i.code for i in sodra_obj.setting_id.field_A12]
            for j in valid_payslip:
                payslip=obj_payslip.browse(cr,uid,j)
                name.append(payslip.employee_id.name or ' ')
                otherid.append(payslip.employee_id.otherid or ' ')
                identifications.append(payslip.employee_id.identification_id or ' ')
                start_date.append(payslip.contract_id.date_start or ' ')
                fire_date.append(payslip.contract_id.date_end or ' ')
                sumA11=0.0
                sumA12=0.0
                for line in payslip.line_ids:
                    if line.code in code_A11: sumA11 += line.total
                    if line.code in code_A12: sumA12 += line.total
                field_A11.append("%.2f"%sumA11)
                field_A12.append("%.2f"%sumA12)
                total_A11 += sumA11
                total_A12 += sumA12
            datas=[identifications,otherid,name,start_date,fire_date,field_A11,field_A12,"%.2f"%total_A11,"%.2f"%total_A12]
            # valid_payslip is list of valid payslips, no_of_pages required to fit the payslips, datas = data of employee of the payslip
            print "--------final result---------",no_of_pages,valid_payslip,datas
        return [no_of_pages,valid_payslip,datas] 
    
        
                
   

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
