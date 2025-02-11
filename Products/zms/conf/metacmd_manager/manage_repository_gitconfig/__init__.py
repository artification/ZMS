class manage_repository_gitconfig:
	"""
	python-representation of manage_repository_gitconfig
	"""

	# Acquired
	acquired = 0

	# Action
	action = "%smanage_executeMetacmd?id=manage_repository_gitconfig"

	# Description
	description = ""

	# Execution
	execution = 0

	# Icon_clazz
	icon_clazz = "fas fa-cogs"

	# Id
	id = "manage_repository_gitconfig"

	# Meta_types
	meta_types = ["ZMS"]

	# Name
	name = "TAB_CONFIGURATION"

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
	title = "Git-Configuration"

	# Impl
	class Impl:
		manage_repository_gitconfig = {"id":"manage_repository_gitconfig"
			,"type":"External Method"}
