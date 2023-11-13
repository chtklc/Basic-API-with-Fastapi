from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

cars = {
    1: {"make": "Toyota", "model": "Camry", "year": 2005},
    2: {"make": "Honda", "model": "Civic", "year": 2014},
    3: {"make": "Ford", "model": "Mustang", "year": 2022},
}

class CarModel(BaseModel):
    make: str = Field(description="Make of the car", example="Toyota")
    model: str = Field(description="Model of the car", example="Camry")
    year: int = Field(description="Year of the car", example=2020)

@app.get("/cars", response_model=list[CarModel])
def get_cars():
    """Get the list of all cars."""
    return list(cars.values())

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    car = cars.get(car_id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail="Car not found")

@app.post("/cars")
def add_car(car: CarModel):
    car_id = max(cars.keys()) + 1 if cars else 1
    cars[car_id] = car.dict()
    return {"message": f"Car added with ID {car_id}"}

@app.put("/cars/{car_id}")
def update_car(car_id: int, updated_car: CarModel):
    if car_id not in cars:
        raise HTTPException(status_code=404, detail="Car not found")
    else:
        car = cars[car_id]
        car["make"] = updated_car.make
        car["model"] = updated_car.model
        car["year"] = updated_car.year
    return {"message": f"Car with ID {car_id} updated"}

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    if car_id not in cars:
        raise HTTPException(status_code=404, detail="Car not found")
    else:
        del cars[car_id]
    return {"message": f"Car with ID {car_id} deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
