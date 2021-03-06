from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId


retval = api.campaignUnschedule(cid)
if api.errorCode:
	print "Unable to load campaignUnschedule()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Campaign Unscheduled!"
