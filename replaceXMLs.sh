#! /bin/bash
#
#
#

rm /home/yosemit1/minustide_scripts/*.xml


# get Kahului XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Kahului.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=1615680'

# get Kihei XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Kihei.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=TPT2797'

# get Lahina XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Lahina.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=TPT2799'

# get Makena XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Makena.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=1615202'

# get SantaCruz XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/SantaCruz.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=9413450'

# get Seattle XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Seattle.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=9447130'

# get Bolinas XML
/usr/bin/curl -o /home/yosemit1/minustide_scripts/Bolinas.xml 'http://tidesandcurrents.noaa.gov/noaatidepredictions/NOAATidesFacade.jsp?datatype=Annual+XML&Stationid=9414958'
