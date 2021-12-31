from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class main_hosptial(models.Model):
	"""real name of the model"""
	_name = "main_hosp.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "Main Model for hosptial manangment"
	_order="id,age"


	name = fields.Char(required=True ,string="Name")
	age= fields.Integer(tracking=True)
	#sqeunce number
	reference=fields.Char(string="Reference",tracking=True,readonly=True,required=True,copy=False,
							default=lambda self: _('New'))
	gender=fields.Selection(
        string='Gender',
        required=True,
        default='male',
        selection=[
        ('male','Male'),
        ('female','Female'),
        ('other','other')])
	state=fields.Selection(
        string='Status',
        default='draft',
        selection=[
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('done','Done'),
        ('cancel','Cancelled')])

	responsible_id=fields.Many2one('res.partner',string="Responsible")
	appointement_ids=fields.One2many('appointment.model','patient_id',string="appointment")

	
	note=fields.Text(string="Description")
	appoint_count = fields.Integer(compute="_cal_appoint", string="Appointment Times")
	image=fields.Binary(string="Patient Image")
	#using for looops saves from singleton

	def _cal_appoint(self):
		for rec in self:
			ap_count=self.env['appointment.model'].search_count([('patient_id','=',rec.id)])
			rec.appoint_count=ap_count


	def action_confirm(self):
		self.state='confirm'
		for rec in self:
			#search fucctiojn crud
			patience=self.env["main_hosp.model"].search([('gender','=','female')])
			print('patience-------------------------' ,patience)
			#search with or notation
			#patience=self.env["main_hosp.model"].search(['|',('gender','=','female')])

			#search odoo count
			patience_count = self.env["main_hosp.model"].search_count([('gender', '=', 'female')])
			print('patience-------------------------', patience_count)

			#reference in odoo ????
			re_patience = self.env.ref("hospital.patient_form")
			print(re_patience.id)


	def action_done(self):
		self.state='done'

	def action_draft(self):
		self.state='draft'

		#copy function
		record_to_copy=self.env['main_hosp.model'],browse(3)
		#add records in copy funvtion to make changesas you copy
		record_to_copy.copy()

		# unlick  function it deletes functions
		# record_to_unlick = self.env['main_hosp.model'], browse(3)
		# record_to_copy.unlink()


	def action_cancelled(self):
		self.state='cancel'
		#browser fuction
		browse_r = self.env["main_hosp.model"].browse(3)
		print("browse_result--------------------------------",browse_r)
		#exsits method
		if browse_r.exists():
			print("tiriko wanku ---------------------------")
		else:
			print("hazviko ----------------------------------")
		vals={
			'name':"icho created",
			'age':90,
			}
		# create record
		self.env["main_hosp.model"].create(vals)

		#update
		record_to_update=self.env["main_hosp.model"].browse(1)
		if record_to_update.exists():
			vali = {
				'name': "Real Name",
				'age': 12,
			}
			record_to_update.write(vali)

	#this methodes ovride whrn you create new fields  in interfwce

	@api.model
	def create(self,vals):
		if not vals.get('note'):
			vals['note']='New Patient'
		if vals.get('reference', _('New')) == _('New'):
			vals['reference']=self.env['ir.sequence'].next_by_code('hosp_patience.seq') or _('New')
		res= super(main_hosptial,self).create(vals)
		return res

	@api.model
	def default_get(self, fields):
		vals = super(main_hosptial, self).default_get(fields)
		#if not res.get('gender'):
		#	vals['gender']='other'	
		return vals

	# check for condtions and constraints on specific field
	# @api.constrains('name')
	# def _validate_name_exist(self):
	# 	for rec in self:
	# 		patients=self.env['main_hosp.model'].search([('name','=!',rec.name),('id','=!',rec.id)])
	# 		if patients:
	# 			raise ValidationError(_("Name %s Already Exisit"% rec.name))

	#check for condtions and constraints on specific field
	@api.constrains('age')
	def _validate_age(self):
		for rec in self:
			if rec.age==0:
				raise ValidationError(_("Age cannot be Zero"))

	#for having more deatils in many2 one fields dropdown
	def name_get(self):
		result=[]
		for rec in self:
			name = rec.reference + ' ' + rec.name
			result.append((rec.id, name))
		return result

	#name get
	#name search

	#open oppoinrmtnes from smart buttons
	def action_open_appointments(self):
		
		return{
			'type':'ir.actions.act_window',
			'name':'Appointments',
			'res_model':'appointment.model',
			'domain':[('patient_id','=',self.id)],
			'context':[('default_patient_id','=',self.id)],
			'view_mode':'tree,form',
			'target':'current',
		}