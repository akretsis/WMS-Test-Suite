########## Required Parameters #############

# User VO
VO=""

# WMS used in the test 
WMS=""

# LB used in the test
LB="" 

# Log level used during the test, default level is INFO. For extra output,set to DEBUG or TRACE.
# (possible values: NONE FAIL WARN INFO DEBUG TRACE)
LOG_LEVEL="INFO"

######### Optional Parameters ###############

#MyProxyServer used in the test
MYPROXYSERVER=""

#  
WMS_USERNAME=""

##
WMS_PASSWORD=""

##Absolute path
YAIM_FILE=""


# Default requirements
### SOS use only ' not "
DEFAULTREQ='other.GlueCEStateStatus == "Production"'

# Default delegation option
DELEGATION_OPTIONS="-a"

# Number of retrievals before to stop test (timeout)
NUM_STATUS_RETRIEVALS=120

# Seconds between two retreivals
SLEEP_TIME=30
