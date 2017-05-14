#
# == Behavior ==
#

UNAME := $(shell uname)

#
# == Paths & Directories ==
#

VENV_DIR          := .virtualenv

#
# == Commands ==
#

VIRTUALENV := virtualenv
PIP        := $(VENV_DIR)/bin/pip

#
# == Targets ==
#

default: dependencies

dependencies: python-dependencies

.SILENT: env
env:
	env | grep -E '^PINGBOARD' | sort

#
# == Dependencies ==
#

python-dependencies: $(VENV_DIR)
	$(PIP) install -r requirements.txt

$(VENV_DIR):
	$(VIRTUALENV) --prompt='(pingboard_ldap) ' $(VENV_DIR)
