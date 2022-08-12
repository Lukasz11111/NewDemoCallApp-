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
from time import time, sleep
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
        # page.move_to_account()
        # page.move(page.account, page.about)
        # page.move(page.about, page.header, subpoints=4, time=0) and sleep(0.5)
        # page.move(page.header, page.select) and sleep(1)
        page.moveToRegion()
        page.move(page.region, page.select,subpoints=4, time=0) and sleep(1)

        page.select_region("Japan")

        page.select_many_times_options()
        page.move(page.select, page.number_input) and sleep(1)
        page.click()
        page.fill_number()
        page.move(page.number_input, page.button, subpoints=3, time=0)
        page.click()
        page.move(page.button, page.header, subpoints=3, time=0)
    end = time()
    log.debug(F"generate_trace({url} end at {start} in {end - start}")
    return {"url": url, "time": end - start}


@app.get("/generate_trace_django/")
async def generate_trace_django(url: Optional[str] = DEFAULT_URL):
    start = time()
    log.debug("generate_trace({url} start at {start}", url=url, start=start)
    with Page(url) as page:
        page.move_to_account()
        page.move(page.account, page.about)
        page.move(page.account, page.select) and sleep(1)
        
        page.select_region("Pacific")

        
        page.select_many_times_options()
        page.move(page.select, page.number_input) and sleep(1)
        page.click()
        page.fill_number()
        page.move(page.number_input, page.button, subpoints=3, time=0)
        page.click()
        page.move(page.button, page.header, subpoints=3, time=0)
    end = time()
    log.debug(F"generate_trace({url} end at {start} in {end - start}")
    return {"url": url, "time": end - start}


@app.get("/", include_in_schema=False)
async def root():
    """Documentation"""
    return RedirectResponse("/docs")
