from fastapi import FastAPI, HTTPException
from routes import router
from connection import init_database, myclient

app = FastAPI()
app.include_router(router)


@app.get('/health')
def healthcheck():
    return {'message' : 'healthy'}


@app.get('/create-connection')
def create_connection():
    try:
        init_database()
        return {'message' : 'MongoDB is connected'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/check_connection')
def check_connection():
    try:
        myclient.admin.command('ping')
        return {'message': 'successfully connected to MongoDB!'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)