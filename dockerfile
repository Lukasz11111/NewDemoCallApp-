FROM  python:3.9

WORKDIR /app

RUN pip install requests \
    pip install asyncio  \
    pip install aiohttp
CMD python app.py
