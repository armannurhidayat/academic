from odoo import api, fields, models

class Attendee(models.Model):
	_name = 'academic.attendee'

	name = fields.Char("Name", required=True, size=100)
	session_id = fields.Many2one(comodel_name="academic.session", string="Session", required=False)
	partner_id = fields.Many2one(comodel_name="res.partner", string="Partner", required=True)

	# Untuk validasi unique
	_sql_constraints = [
		('partner_session_unique', 'UNIQUE(partner_id,session_id)', 'You cannot insert the same attendee multiple times!'),
	]

	course_id = fields.Many2one(comodel_name="academic.course", string="Course", required=False, related="session_id.course_id", store=True)