from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
import io
import scipy.stats as stats

app = FastAPI()

@app.post("/generateReport")
async def generate_report(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    report = {}
    
    for column in numeric_columns:
        column_data = df[column]
        report[column] = {
            "min": float(column_data.min()),
            "max": float(column_data.max()),
            "mean": float(column_data.mean()),
            "std": float(column_data.std()),
            "kurtosis": float(stats.kurtosis(column_data))
        }
    
    return JSONResponse(content=report)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)