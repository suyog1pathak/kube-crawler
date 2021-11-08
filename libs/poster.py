import logging, os
"""Custom logger to log for console """
logging.basicConfig(     
  format="%(asctime)s : %(levelname)s : [%(filename)s:%(lineno)s - %(funcName)10s()] : %(message)s"
)
poster = logging.getLogger("poster")
poster.setLevel(logging.os.environ.get('LOGLEVEL', 'INFO').upper())