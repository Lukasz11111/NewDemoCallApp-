# Call apps
1. Pull repo
    ```
    git clone https://gitlab.com/revdebug/python/scratchpad/newdemocallapp.git
    ```

2. Go to CallApp/ rename endpoints-template.json to endpoints.json

3. endpoint.json options:

    ```
    #Call time is randomized between the ranges:
    "minTimeSleep": 200,
    "maxTimeSleep": 320,

    #Number of randomly called endpoints from given ranges:
    "callCount": 20,
    "callCountLong": 4,

    #Hours when traffic will be increased
     "increasedTrafficHours": [
        3,
        13,
        15,
        18,
        6
    ]
    ```
    endpoints and longEndpoints are sections where you specify endpoints to be called randomly. It is recommended to leave the data-generation endpoints as it is a python application that creates artificial motion in trace. It is recommended to replace url-azure-demo-app with azure-demo address.
    The Const section contains endpoints that will always be called. They will be called last. i.e. in apm trace they will be on the first page (the last endpoint in the list will be the first one visible in trace)
    By putting the \$$id$$ tag in the endpoint, it will be changed to a random value from the "id" list

