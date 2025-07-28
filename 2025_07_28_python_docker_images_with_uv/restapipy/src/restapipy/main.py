import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/pythonic_breakfast")
def _() -> str:
    return "spam ham eggs"


def generate_openapi_json() -> None:
    openapi_dict = app.openapi()
    openapi_json = json.dumps(openapi_dict, indent=4)

    with open("openapi.json", "w") as f:
        f.write(openapi_json)
