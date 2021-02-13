# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPickingExt(models.Model):
    _inherit="stock.picking"

    address = fields.Text(string="العنوان")



class StockMoveLineExt(models.Model):
    _inherit="stock.move.line"

    notes = fields.Char(string="الملاحظات")
