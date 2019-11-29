{
	"name"			: "Latihan Addons Academic Odoo",
	"version"		: "1.0",
	"depends"		: [
						"base"
					],
	"author"		: "Arman",
	"category"		: "Education",
	"website"		: "vitraining.com",
	"description"	: "Sistem Education Version 1",
	"data"	: [
				"menu.xml",
				"course.xml",
				"session.xml",
				"attendee.xml",
				"partner.xml",
				"data/squence.xml",
				"security/ir.model.access.csv",
				"security/group.xml",
				"wizard/create_attendee_view.xml"
			],

	"installable": True,
	"auto_install": False,
	"application": True,
}