# coding=utf-8
from openerp.osv import osv , orm , fields

class hr_sd5(osv.osv):
    _inherit='hr.contract'
    
    def a5_selection(self,cr,uid,context=None):
        a5=(('01','01 - priėmimas į darbą (pagal darbo sutartį)'),('03','03 - reorganizavimas'),('05','05 - socialinė apsauga pagal Europos Sąjungos Reglamentus'),('06','06 - socialinė apsauga pagal dvišalę sutartį'),('07','07 - valstybės tarnautojo perkėlimas (kitoje valstybėje)'),('08','08 - valstybės tarnautojo perkėlimas (Lietuvoje)'),('09','09 - valstybės lėšomis draudžiamas sutuoktinis'),('10','10 - darbo biržos siųstas praktikantas'),('11','11 - švietimo įstaigos praktikantas'),('12','12 - dvasininkas'),('13','13 - privalomoji pradinė karo tarnyba'),('14','14 - perkėlimas į kitą struktūrinį padalinį'),('15','15 - priėmimas į pareigas valstybės tarnyboje'),('99','99 - kiti atvejai'))
        return a5
    
    def a7_selection(self,cr,uid,context=None):
        a7=(('IE','IE - Airija'),('AT','AT - Austrija'),('BY','BY - Baltarusija'),('BE','BE - Belgija'),('BG','BG - Bulgarija'),('CZ','CZ - Čekija'),('DK','DK - Danija'),('GB','GB - Didžioji Britanija'),('EE','EE - Estija'),('GR','GR - Graikija'),('IS','IS - Islandija'),('ES','ES - Ispanija'),('IT','IT - Italija'),('US','US - JAV'),('CA','CA - Kanada'),('CY','CY - Kipras'),('LV','LV - Latvija'),('PL','PL - Lenkija'),('LI','LI - Lichtenšteinas'),('LT','LT - Lietuva'),('LU','LU - Liuksemburgas'),('MT','MT - Malta'),('NL','NL - Nyderlandai'),('NO','NO - Norvegija'),('PT','PT - Portugalija'),('FR','FR - Prancūzija'),('RO','RO - Rumunija'),('RU','RU - Rusija'),('SK','SK - Slovakija'),('SI','SI - Slovėnija'),('FI','FI - Suomija'),('SE','SE - Švedija;'),('CH','CH - Šveicarija'),('UA','UA - Ukraina'),('HU','HU - Vengrija'),('DE','DE - Vokietija'))
        return a7
    
    def a5_selection_2(self,cr,uid,context=None):
        a5=(('02','02 - atleidimas iš darbo (pagal darbo sutartį)'),('03',' 03 - reorganizavimas'),('04','04 - pertvarkymas'),('05','05 - socialinė apsauga pagal Europos Sąjungos Reglamentus'),('06','06 - socialinė apsauga pagal dvišalę sutartį'),('07','07 - valstybės tarnautojo perkėlimas (kitoje valstybėje)'),('08','08 - valstybės tarnautojo perkėlimas (Lietuvoje)'),('09','09 - valstybės lėšomis draudžiamas sutuoktinis'),('10','10 - darbo biržos siųstas praktikantas'),('11','11 - švietimo įstaigos praktikantas'),('12','12 - dvasininkas'),('13','13 - privalomoji pradinė karo tarnyba'),('14','14 - perkėlimas į kitą struktūrinį padalinį'),('16','16 - atleidimas iš pareigų valstybės tarnyboje'),('99','99 - kiti atvejai.'))
        return a5
        
    
    _columns={'company':fields.many2one('res.company'),
              'sodra':fields.many2one('sodra.config'),
              'a5':fields.selection(a5_selection,'A5 - pranešimo pateikimo priežasties kodas'),
              'a6':fields.char('A6 - pranešimo pateikimo priežastis',size=65),
              'a7':fields.selection(a7_selection,'A7 - pranešimo pateikimo priežasties patikslinimo kodas'),
              'a8':fields.char('A8 - pranešimo pateikimo priežasties patikslinimas',size=58),
              
              'a5_2':fields.selection(a5_selection_2,'A5 - pranešimo pateikimo priežasties kodas'),
              'a6_2':fields.char('A6 - pranešimo pateikimo priežastis',size=65),
              'a7_2':fields.selection(a7_selection,'A7 - pranešimo pateikimo priežasties patikslinimo kodas'),
              'a8_2':fields.char('A8 - pranešimo pateikimo priežasties patikslinimas',size=58),
              'a30':fields.char('A30 - teisės akto straipsnis',size=5),
              'a31':fields.char('A31 - teisės akto straipsnio dalis;',size=1),
              'a32':fields.char('A32 - teisės akto straipsnio dalies punktas',size=2),
              'a33':fields.char('A33 - už kiek mėnesių vidutinio darbo užmokesčio dydžio išeitinė išmoka arba išeitinė kompensacija apskaičiuota',size=2),
              'p5_2':fields.float('P5 Iš viso pranešime pajamų, nuo kurių skaičiuojamos įmokos, suma Lt',size=11),
              'p6_2':fields.float('P6 Iš viso pranešime įmokų suma Lt',size=11),
              }
    
       
    _defaults={'company':lambda self,cr,uid,c:self.pool.get('res.users').browse(cr,uid,uid).company_id.id,
               
               }
    
    
    def onchange_a5(self,cr,uid,id,a5,context=None):
        a=self.a5_selection(cr,uid)
        for i in a:
            if i[0]==a5:
                b=i[1][5:]
                return {'value':{'a6':b}}
        return {'value':{'a6':False}}
        
        
    def onchange_a7(self,cr,uid,id,a7,context=None):
        a=self.a7_selection(cr,uid)
        for i in a:
            if i[0]==a7:
                b=i[1][5:]
                return {'value':{'a8':b}}
        return {'value':{'a8':False}}
        
    def onchange_a5_2(self,cr,uid,id,a5_2,context=None):
        a=self.a5_selection_2(cr,uid)
        for i in a:
            if i[0]==a5_2:
                b=i[1][5:]
                return {'value':{'a6_2':b}}
        return {'value':{'a6_2':False}}
        
        
    def onchange_a7_2(self,cr,uid,id,a7_2,context=None):
        a=self.a7_selection(cr,uid)
        for i in a:
            if i[0]==a7_2:
                b=i[1][5:]
                return {'value':{'a8_2':b}}
        return {'value':{'a8_2':False}}
    
    
    
    def write(self,cr,uid,id,vals,context=None):
        user_id=self.pool.get('sodra.config').search(cr,uid,[])
        if len(user_id)!=0:
            vals['sodra']=user_id[0]
        return super(hr_sd5,self).write(cr,uid,id,vals,context)
    
    def create(self,cr,uid,vals,context=None):
        user_id=self.pool.get('sodra.config').search(cr,uid,[])
        if len(user_id)!=0:
            vals['sodra']=user_id[0]
        else:
            raise osv.except_osv(('ERROR !'), ('Please set Sodra Report Settings'))
        return super(hr_sd5,self).create(cr,uid,vals,context)
        
    

class sodra_config(osv.osv):
    _name='sodra.config'
    
    def _address1(self,cr,uid,ids,name,arg,context=None):
        company_id=self.pool.get('res.users').browse(cr,uid,uid).company_id.id
        obj=self.pool.get('res.company').browse(cr,uid,company_id)
        string=(obj.street or '')+' '+(obj.city or '')+' '+(obj.state_id.name or '')
        res={}
        for task in self.browse(cr, uid, ids):
            res[task.id]=string
        return res
    
    def _name1(self,cr,uid,ids,name,arg,context=None):
        company_id=self.pool.get('res.users').browse(cr,uid,uid).company_id.id
        res={}
        for task in self.browse(cr, uid, ids):
            res[task.id]=self.pool.get('res.company').browse(cr,uid,company_id).name
        return res
    
    def _registry1(self,cr,uid,ids,name,arg,context=None):
        company_id=self.pool.get('res.users').browse(cr,uid,uid).company_id.id
        res={}
        for task in self.browse(cr, uid, ids):
            res[task.id] =self.pool.get('res.company').browse(cr,uid,company_id).company_registry
        return res
    
    def _phone1(self,cr,uid,ids,name,arg,context=None):
        company_id=self.pool.get('res.users').browse(cr,uid,uid).company_id.id
        res={}
        for task in self.browse(cr, uid, ids):
            res[task.id]=self.pool.get('res.company').browse(cr,uid,company_id).phone
        return res
    
    
    _columns={'name':fields.function(_name1,string='3 - draudėjo pavadinimas',type='char'),
              'sodra_no':fields.char('4 - draudėjo kodas',size=7),
              'registry':fields.function(_registry1,string='5 - juridinio asmens kodas',type='char'),
              'phone':fields.function(_phone1,string='6 - tel. nr',type='char'),
              'address':fields.function(_address1,string='7 - adresas',type='char'),
              'p1':fields.float('P1 draudėjui',digits=(4,2),size=5),
              'p2':fields.float('P2 apdraustajam',digits=(4,2),size=5),
              'p3':fields.float('P3 bendras (P1+P2)',digits=(4,2),size=5),
              'k6':fields.char('K6 - apdraustojo profesija pagal Lietuvos profesijų klasifikatorių.',size=4),
              'f11':fields.many2one('res.partner','11 - vadovo ar įgalioto asmens pareigų pavadinimas'),
              'f13':fields.many2one('res.partner','13 - vadovo ar įgalioto asmens vardas, pavardė'),
              
              'name_2':fields.function(_name1,string='3 - draudėjo pavadinimas',type='char'),
              'sodra_no_2':fields.char('4 - draudėjo kodas',size=7),
              'registry_2':fields.function(_registry1,string='5 - juridinio asmens kodas',type='char'),
              'phone_2':fields.function(_phone1,string='6 - tel. nr',type='char'),
              'address_2':fields.function(_address1,string='7 - adresas',type='char'),
              'p1_2':fields.float('P1 draudėjui',digits=(4,2),size=5),
              'p2_2':fields.float('P2 apdraustajam',digits=(4,2),size=5),
              'p3_2':fields.float('P3 bendras (P1+P2)',digits=(4,2),size=5),
              'f11_2':fields.many2one('res.partner','11 - vadovo ar įgalioto asmens pareigų pavadinimas'),
              'f13_2':fields.many2one('res.partner','13 - vadovo ar įgalioto asmens vardas, pavardė'),
              
              }
    
    
    
    def onchange_p3(self,cr,uid,ids,p1,p2):
        p3=p1+p2
        if p3>100:
            return {'value':{'p3':100},'warning':{'title':'warning','message':'(sum of P1 and P2) Percent cannot be greater than hundred'}}
        return {'value':{'p3':p3}}
    
    def onchange_p3_2(self,cr,uid,ids,p1_2,p2_2):
        p3_2=p1_2+p2_2
        if p3_2>100:
            return {'value':{'p3_2':100},'warning':{'title':'warning','message':'(sum of P1 and P2) Percent cannot be greater than hundred'}}
        return {'value':{'p3_2':p3_2}}
    
    '''_defaults={#'name':_name1,
               #'registry':_registry1,
               #'phone':_phone1,
               'address':_address1,
               }'''
    
    def create(self,cr,uid,vals,context=None):
        #print('5555555555555',type(self.pool.get('account.period').browse(cr,uid,5).date_start))
        id=[]
        id=self.search(cr,uid,[])
        if (len(id)>=1):
            raise osv.except_osv(('ERROR !'), ('Only one set of settings allowed'))
            #return super(vat_report_form,self).create(cr,uid,vals,context=context)
        else:
            return super(sodra_config,self).create(cr,uid,vals,context=context)