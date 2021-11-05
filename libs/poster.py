import logging, os
"""Custom logger to log for console """
logging.basicConfig(
        format="%(asctime)s : %(levelname)s : [%(filename)s:%(lineno)s - %(funcName)10s()] : %(message)s"
  )
poster = logging.getLogger("poster")
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
poster.setLevel(logging.LOGLEVEL)