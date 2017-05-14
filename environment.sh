#
# This script sets up the local shell environment.
#

#
# Do NOT run this script (`./environment.sh` or `bash
# environment.sh`); instead source it (`source environment.sh`).
# 
SCRIPT_NAME=$(basename "$0")
SOURCE_NAME=$(basename "$BASH_SOURCE")
if [ "$SCRIPT_NAME" = "$SOURCE_NAME" ]; then
    echo 'ERROR: Do not execute (`bash environment.sh`) this script! Source it instead (`source environment.sh`)' >&2
    exit 1
fi

#
# Python virtualenv
#

VENV_DIR=`pwd`/.virtualenv
if [ -d "$VENV_DIR" ]; then
    echo "[virtualenv] Entering Python virtualenv at ${VENV_DIR}" >&2
    . "${VENV_DIR}/bin/activate"
else
    echo "ERROR: Python virtualenv directory (${VENV_DIR}) does not exist.  Did you run `make` yet?" >&2
fi

#
# PYTHONPATH
#

LIB_DIR=`pwd`/lib
if [ -z $(echo $PYTHONPATH | grep "$LIB_DIR") ]; then
    echo "[pythonpath] Adding $LIB_DIR to PYTHONPATH (${PYTHONPATH})"
    export PYTHONPATH="${PYTHONPATH}:${LIB_DIR}"
else
    echo "[pythonpath] $LIB_DIR already on PYTHONPATH (${PYTHONPATH})"
fi
