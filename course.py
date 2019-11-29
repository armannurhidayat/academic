from odoo import api, fields, models

class Course(models.Model):
	_name = 'academic.course' # Name untuk model

	name = fields.Char("Name", size=100)
	title = fields.Char(
	    string='Number',
	    default='New',
	    readonly=True, 
	)
	description = fields.Text(string="Description")
	responsible_id = fields.Many2one(comodel_name="res.users", string="Responsible", required=True)
	session_ids = fields.One2many(comodel_name="academic.session", inverse_name="course_id", string="Sessions", required=False, ondelete="cascade")

	# Untuk validasi unique
	_sql_constraints = [
		('cek_name_desc', 'CHECK(name <> description)', 'Field name dan description tidak boleh sama'),
		('cek_unik_name', 'UNIQUE(name)', 'Name harus unik')
	]

	@api.model
	def create(self, vals):
		if not vals.get('title', False) or vals['title'] == 'New':
			vals['title'] = self.env['ir.sequence'].next_by_code('academic.course') or 'Error Number!!!'
		return super(Course, self).create(vals) # Course dari Class