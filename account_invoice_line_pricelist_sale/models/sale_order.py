# Copyright 2022 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def _prepare_invoice_line(self, qty):
        """Make sure pricelist_id is set on invoice."""
        self.ensure_one()
        val = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        if self.pricelist_id:
            val.update({
                'pricelist_id': self.pricelist_id.id,
            })
        return val
