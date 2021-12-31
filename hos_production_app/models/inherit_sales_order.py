from odoo import fields, models, api ,_

class add_into_order_line(models.Model):
	"""real name of the model"""
	_inherit ="sale.order.line"
	_description="Moddification of order sales table"

	line_marking=fields.Text(string='Line Making')
	prods_id=fields.Many2one('prod_order.model', string="Production_id")
	prod_ist=fields.Text(string='Product Instruction')
	delivered=fields.Monetary( string='Delivered')
	invoiced=fields.Monetary( string='Invoiced')
	lineDiscount=fields.Integer( string='Line Discount %')
	disAmount=fields.Integer( string='line Amount' )
	delivered_Qty = fields.Integer(string="Delivered Quantity.")


	@api.onchange("lineDiscount")
	def _onchange_lineDiscount(self):
		self.disAmount = self.lineDiscount/100 * self.price_subtotal
		temp=self.price_subtotal
		self.price_subtotal=temp-self.disAmount





