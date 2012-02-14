#
# Bug:73715
# Title: Missing ReallyRunning event from LogMonitor
# Link: https://savannah.cern.ch/bugs/?73715
#
#

import logging

from libutils.Exceptions import *
from libutils import Job_utils

def run(utils):

    bug='73715'

    logging.info("Start regression test for bug %s"%(bug))
    
    # we need to test both lcg CE and CREAM CE
    
    for dest in ("/cream-", "2119/jobmanager") :
    
        logging.info("Prepare jdl file for submission to a ce like %s"%(dest))

        # Necessary to avoid overwrite of the external jdls
        utils.use_utils_jdl()
        utils.set_jdl(utils.get_jdl_file())
        utils.set_destination_ce(utils.get_jdl_name(), dest)
  
        JOBID=Job_utils.submit_wait_finish(utils, dest)
        utils.job_status(JOBID)
        
        if utils.JOBSTATUS.find('Done (Success)') != -1 :

            logging.info("Look for the ReallyRunning events in the logging info")

            result=utils.run_command_continue_on_error("glite-wms-job-logging-info -v 3 --event ReallyRunning %s"%(JOBID))
    
            if result.find("Wn seq") == -1:
                logging.error("WN sequence code not found")
                raise GeneralError("Check ReallyRunning events","WN sequence code not found")        
            else:
                logging.info("Found ReallyRunning events as expected. Test PASS")
                
        else:
            logging.error("Job not finished successfully. Retry the test.")
            raise RetryError("Check job final status","Job not finished successfully.") 

    logging.info("End of regression test for bug %s"%(bug))
