from odoo import fields, models , api ,_
from datetime import datetime

class add_into_sales(models.Model):
	"""real name of the model"""
	_inherit ="sale.order"
	_description = "Moddification of sales table"

	price_list=fields.Many2one('product.pricelist',string="Price list")
	total_dis=fields.Monetary(compute="_cal_discount", string='Total Discount')
	total_dis_line=fields.Monetary( string='Total Line Discount')
	client_order_ref2 = fields.Char(string='Customer Reference 2', copy=False)
	delive_date = fields.Date( string="Delivery_Date")
	orde_date = fields.Date(string="Order_Date")

	# add this line


	def _cal_discount(self):
		for record in self:
			record.total_dis= record.amount_undiscounted - record.amount_untaxed


	@api.onchange("date_order")
	def _onchange_orde_date(self):
		self.orde_date = self.date_order.date()

	def action_confirm(self):
		self.state=""
		for record in self:
			created_all = self.env["prod_order.model"].search_count([('main_sales_id', '=', record.id)])
			if created_all == 0:
				self.env["prod_order.model"].create(
					{
						"main_sales_id": record.id,
					}
				)
			else:
				pass
		return super().action_confirm()



