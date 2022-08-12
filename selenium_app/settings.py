from twiggy import levels

DEFAULT_URL: str = "http://3.249.139.90/"
REMOTE_DRIVER_IP: str = "selenium-standalone-chrome"
REMOTE_DRIVER_PORT: int = 4444
REMOTE_DRIVER: str = F"http://{REMOTE_DRIVER_IP}:{REMOTE_DRIVER_PORT}/wd/hub"
VERSION: str = "1.0.0"
ENDING_SLEEPING_TIME: int = 15  # Time for recorder to send record to server
LOG_LEVEL: levels.LogLevel = levels.INFO
