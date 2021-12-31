from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class logowner_table(models.Model):
	"""real name of the model"""
	_name = "mantainance.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "this is for logging maintance"

	laptopDetails= fields.Many2one('laptopsys.model', string="laptopsys_id")
	Problem= fields.Char(tracking=True, string='Problem',required=True)
	dateDis=fields.Date(string="Date Problem Discovered")
	datefix=fields.Date(tracking=True,string="Date Problem Fixed")
	cost=fields.Float(string="Cost $")
	where=fields.Text(tracking=True,string="Service Recieved From")

