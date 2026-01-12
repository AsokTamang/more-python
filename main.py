import logging
logging.basicConfig(  #here we are logging the logging message as well as the time based on the INFO level
filename='app.log',level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.warning('gotta make it quicker')

