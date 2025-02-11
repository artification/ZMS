class manage_repository_gitstatus:
	"""
	python-representation of manage_repository_gitstatus
	"""

	# Acquired
	acquired = 0

	# Action
	action = "%smanage_executeMetacmd?id=manage_repository_gitstatus"

	# Description
	description = ""

	# Execution
	execution = 0

	# Icon_clazz
	icon_clazz = "fas fa-bullhorn"

	# Id
	id = "manage_repository_gitstatus"

	# Meta_types
	meta_types = ["ZMS"]

	# Name
	name = "Git Status"

	# Nodes
	nodes = "{$}"

	# Package
	package = "com.zms.foundation.metacmd.gitbridge"

	# Revision
	revision = "5.0.2"

	# Roles
	roles = ["ZMSAdministrator"]

	# Stereotype
	stereotype = "repository"

	# Title
	title = "Show Git Status"

	# Impl
	class Impl:
		manage_repository_gitstatus = {"id":"manage_repository_gitstatus"
			,"type":"External Method"}
