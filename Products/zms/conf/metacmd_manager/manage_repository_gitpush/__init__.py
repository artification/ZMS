class manage_repository_gitpush:
	"""
	python-representation of manage_repository_gitpush
	"""

	# Acquired
	acquired = 0

	# Action
	action = "%smanage_executeMetacmd?id=manage_repository_gitpush"

	# Description
	description = ""

	# Execution
	execution = 0

	# Icon_clazz
	icon_clazz = "fas fa-forward"

	# Id
	id = "manage_repository_gitpush"

	# Meta_types
	meta_types = ["ZMS"]

	# Name
	name = "BTN_GITPUSH"

	# Nodes
	nodes = "{$}"

	# Package
	package = "com.zms.foundation.metacmd.gitbridge"

	# Revision
	revision = "5.0.1"

	# Roles
	roles = ["ZMSAdministrator"]

	# Stereotype
	stereotype = "repository"

	# Title
	title = "Git Push"

	# Impl
	class Impl:
		manage_repository_gitpush = {"id":"manage_repository_gitpush"
			,"type":"External Method"}
