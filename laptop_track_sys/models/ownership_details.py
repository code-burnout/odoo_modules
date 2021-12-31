from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class ownership_table(models.Model):
	"""real name of the model"""
	_name = "curownership.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "This is a laptop Tracking System for BakerTilly"

	laptopSYS_id = fields.Many2one('laptopsys.model', string="laptopsys_id")
	ownerName= fields.Char(related='laptopSYS_id.currentOnwer',tracking=True, string='Current Owner Name',required=True, )
	phoneNo=fields.Char(string="Contact Number")
	issuedDate=fields.Date(string="laptop Issued Date")
	department = fields.Char(required=True, string="Department")
	address=fields.Text(string="Address")


