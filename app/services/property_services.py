from fastapi import APIRouter, HTTPException

from typing import Union

from app.models.property import PropertyModel

router = APIRouter(
	prefix="/properties",
	responses={404: {"description": "Not found"}},
)

@router.get("/filter")
async def properties_filters(year = None, city = None, status = None):
	filter = {"year": year, "city": city, "status": status}
	data_filters = PropertyModel().filters(filter)
	if len(data_filters) == 0 :
		raise HTTPException(status_code=404, detail="Item not found")
	return data_filters

@router.get("/")
async def properties_all():
	properties = PropertyModel().available()
	if len(properties) == 0:
		raise HTTPException(status_code=404, detail="Item not found")
	return properties
