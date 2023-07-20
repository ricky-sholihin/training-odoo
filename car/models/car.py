from odoo import api, fields, models


class Car(models.Model):
    _name = "car.car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name", required=True)
    production_date = fields.Date("Production Date")
    brand = fields.Selection([("hyundai", "Hyundai"),("toyota", "Toyota"), ("tesla", "Tesla")], string="Brand", default="hyundai")
    miles = fields.Integer("Mile")
    picture = fields.Binary(string="Car Picture")
    price = fields.Float(string="Price")
    rented = fields.Boolean(string="Rented", readonly=True) 
