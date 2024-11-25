from Application.Interfaces.ILoggerCoreApplication import ILoggerCoreApplication
from Domain.Commons.DependencyContainer import get_dependency
from Domain.Entities.CoreLoggerEntity import CoreLoggerEntity
from Domain.Interfaces.ILoggerInfraestructure import ILoggerInfraestructure

class LogUsecase(ILoggerCoreApplication):
    def __init__(self) -> None:                    
        self.__Mongo:ILoggerInfraestructure = get_dependency(ILoggerInfraestructure)

    async def open_log(self,cApi:str, cOperation:str, cJsonRequest:str) -> str:
        # Hacer validaciones AQUI
        return await self.__Mongo.open_log(cApi, cOperation, cJsonRequest)

    async def close_log(self,id:str, cJsonResponse:str) -> None:
        await self.__Mongo.close_log(id, cJsonResponse)

    async def close_with_error_log(self,id:str, cJsonResponse:str) -> None:
        await self.__Mongo.close_with_error_log(id, cJsonResponse)
    
    async def get_log(self,id:str) -> CoreLoggerEntity | None:
        return await self.__Mongo.get_log(id)