from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
		"""
		This is more like cpp struct NOT class.
		
		Enum ModelName says 'these are the only model 
		names possible. Nothing else is considered a model name'.
		model names can only and only be -
		1. ModelName.alexnet
		2. ModelName.resnet
		3. ModelName.lenet
		4. ModelName.}permitted_path4
		
		If we give a path input which isnt listed in key's values below,
		in dev envt, it returns expected path input
		"""
		
		alexnet = "alexnet"
		resnet = "resnet"
		lenet = "lenet"
		permitted_path4 = "path4" # "path4" is excepted not "permitted_path4" in url field


app = FastAPI()


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
	
		# compare keys (members of enum) `instance.key`
    if model_name == ModelName.alexnet:
        return {
        	"model_name": model_name, 
        	"message": "Deep Learning FTW!",
        }
    
    # compare values using  `instance.value`
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    # return enum retated opns.
    return {"model_name": model_name, "message": "Have some residuals"}