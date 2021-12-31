from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class logowner_table(models.Model):
	"""real name of the model"""
	_name = "logowner.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "This is a table for People used a laptop"

	laptop_id = fields.Many2one('laptopsys.model', string="laptopsys_id")
	Name= fields.Char(tracking=True, string='Name',required=True)
	phoneNum=fields.Char(string="Contact Number")
	dateRec=fields.Date(tracking=True,string="Start Date")
	dateEnd=fields.Date(tracking=True,string="End Date")
	departmen= fields.Char(required=True, string="Department")
	address=fields.Text(string="Address")
	reason=fields.Text(tracking=True,string="Reason")

