from odoo import fields, models, api , _
from odoo.exceptions import  ValidationError

class laptop_sys(models.Model):
	"""real name of the model"""
	_name = "laptopsys.model"
	_inherit =["mail.thread","mail.activity.mixin"]
	_description = "This is a laptop Tracking System for BakerTilly"
	_rec_name="modelName"

	ownership_ids = fields.One2many('curownership.model', 'laptopSYS_id', string="ownership deatils")
	log_owner_ids = fields.One2many('logowner.model', 'laptop_id', string="log_onwnership")
	laptop_maintain_ids = fields.One2many('mantainance.model', 'laptopDetails', string="mantainance_ids")


	modelName = fields.Char(required=True ,string="Brand Name" ,default="eg: Dell yyy")
	serialNum = fields.Char(required=True ,string="Serial Number" ,default="")
	laptopImage = fields.Binary(string="laptop Photo")
	processor = fields.Text(required=True ,string="Processor" ,default="")
	ramSize = fields.Char(required=True ,string="Ram Size", default="")
	currentOnwer = fields.Char(string="Current Owner")
	osInstalled = fields.Char(string="OS Installed")
	totalMaintaince = fields.Float(string="Total Maintaince Cost $",compute="_cal_totalcosts")
	priceBought = fields.Float(string="Price Bought $")
	repairs_count = fields.Integer(compute="_repairs_count", string="Appointment Times")

	# usinf f=or looops saves from singleton
	def _repairs_count(self):
		for rec in self:
			rep_count = self.env['mantainance.model'].search_count([('laptopDetails', '=', rec.id)])
			rec.repairs_count = rep_count

	# usinf f=or looops saves from singleton
	def _cal_totalcosts(self):
		total=0
		for rec in self:
			rep_count = self.env['mantainance.model'].search([('laptopDetails', '=', rec.id)])
			for reco in rep_count:
				current = reco.cost
				total=total+current
			rec.totalMaintaince=total

	ownership = fields.Selection(
		string='Owned By',
		tracking=True,
		default='bakerTilly',
		selection=[
			('bakerTilly', 'BakerTilly'),
			('rental', 'Q Rent'),])

	state = fields.Selection(
		string='Status',
		tracking=True,
		default='new',
		selection=[
			('new', 'Good Condition'),
			('under_service', 'Under Service'),
			('terminated', 'Terminated'),])

	# @api.depends('laptop_maintain_ids','totalMaintaince')
	# def _amount_al(self):
	# 	"""
    #     Compute the total amounts of the SO.
    #     """
	# 	for order in self:
	# 		for line in order.laptop_maintain_ids:
	# 			totalMaint += line.cost
	# 			print("++++++)))))))))))))))))))))))))"+totalMaint)