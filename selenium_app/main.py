"""
<img src='https://revdebug.com/wp-content/themes/RevDeBug/dist/images/logo.svg' width="25%" height="25%">
<br>
<h1>Tool for generating traffic in demo app.</h1>
<p>
Docker with selenium driver have to be running. For example:
</p>
<code>docker run -it -p {REMOTE_DRIVER_PORT}:{REMOTE_DRIVER_PORT} -p 7900:7900 --shm-size="2g"  
selenium/standalone-chrome</code>
"""
from time import time
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from twiggy import quick_setup, log

from page import Page
from settings import DEFAULT_URL, REMOTE_DRIVER_PORT, VERSION, LOG_LEVEL

app = FastAPI(title="RevDebug",
              description=__doc__.format(REMOTE_DRIVER_PORT=REMOTE_DRIVER_PORT),
              version=VERSION)

quick_setup(LOG_LEVEL)
log.info("Server started with version {VERSION}", VERSION=VERSION)


@app.get("/generate_trace/")
async def generate_trace(url: Optional[str] = DEFAULT_URL):
    start = time()
    log.debug("generate_trace({url} start at {start}", url=url, start=start)
    with Page(url) as page:
        page.x()
        page.y()
    end = time()
    log.debug(F"generate_trace({url} end at {start} in {end - start}")
    return {"url": url, "time": end - start}


@app.get("/", include_in_schema=False)
async def root():
    """Documentation"""
    return RedirectResponse("/docs")
