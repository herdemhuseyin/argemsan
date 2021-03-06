# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "argemsan"
app_title = "Argemsan"
app_publisher = "Frappe"
app_description = "Argemsan için yazılan Custom Kodlar"
app_icon = "icon-book"
app_color = "grey"
app_email = "herdemhuseyin@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/argemsan/css/argemsan.css"
# app_include_js = "/assets/argemsan/js/argemsan.js"

# include js, css files in header of web template
# web_include_css = "/assets/argemsan/css/argemsan.css"
# web_include_js = "/assets/argemsan/js/argemsan.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
	"Purchase Order": "public/js/purchase_order.js",
	"Purchase Receipt": "public/js/purchase_receipt.js",
	"Stock Entry": "public/js/stock_entry.js",
	"Stock Reconciliation": "public/js/stock_reconciliation.js"
}


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "argemsan.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "argemsan.install.before_install"
# after_install = "argemsan.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "argemsan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Asagidaki satirdan uygulama gelistirmeye basla 
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method",
#		"Validate": "herdem_test.sales_order_custom.calculate_total_alan"
#	}
# }

# Asagidaki satirdan uygulama gelistirmeye basla 
#doc_events = {
#	"Purchase Order": {
#		"validate": "argemsan.lgd_utils.sasiparisi_test"
#	}
# }



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"argemsan.tasks.all"
# 	],
# 	"daily": [
# 		"argemsan.tasks.daily"
# 	],
# 	"hourly": [
# 		"argemsan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"argemsan.tasks.weekly"
# 	]
# 	"monthly": [
# 		"argemsan.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "argemsan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "argemsan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "argemsan.task.get_dashboard_data"
# }

