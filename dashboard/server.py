from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

from dashboard.routes import router

app = FastAPI()

templates = Jinja2Templates(directory="dashboard/templates")


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


app.include_router(router)