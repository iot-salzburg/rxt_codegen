import asyncio
from logging import setLogRecordFactory
import robXTask.rxtx_helpers as rxtx_helpers

import rxta_UCI2Camera as rxta_UCI2Camera

async def on_rxte__message__TestCamera__rxtx_helpers(messages):
    async for message in messages:

        # ----------------------------------
        # This is the automatically generated message execution code
        # ----------------------------------
        await rxtx_helpers.logMessageReceived(message)
        print("*** on_rxte__message__TestCamera__rxtx_helpers()")
        sMessage = str(message.payload.decode("utf-8")).strip()
        print("got Message: " + sMessage)

        # ----------------------------------
        # Trying to invoke skill: DetectObject
        # ----------------------------------
        await rxtx_helpers.logSkillCall("DetectObject","Part_Cube")
        await rxta_UCI2Camera.DetectObject("Part_Cube")
        bResOk = await rxta_UCI2Camera.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"DetectObject - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"DetectObject - NOK :-)")
            sErrCode = await rxta_UCI2Camera.GetData(rxta_UCI2Camera.enVariables.StatusDetectObject_ErrorCode)
            sErrMsg = await rxta_UCI2Camera.GetData(rxta_UCI2Camera.enVariables.StatusDetectObject_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"DetectObject - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to invoke skill: DetectObject
        # ----------------------------------
        await rxtx_helpers.logSkillCall("DetectObject","Part_Cylinder")
        await rxta_UCI2Camera.DetectObject("Part_Cylinder")
        bResOk = await rxta_UCI2Camera.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"DetectObject - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"DetectObject - NOK :-)")
            sErrCode = await rxta_UCI2Camera.GetData(rxta_UCI2Camera.enVariables.StatusDetectObject_ErrorCode)
            sErrMsg = await rxta_UCI2Camera.GetData(rxta_UCI2Camera.enVariables.StatusDetectObject_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"DetectObject - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to send message 
        # ----------------------------------
        await rxtx_helpers.sendMessage("TestUR10", "[Empty Message Content]")
        await rxtx_helpers.stop()

rxtx_helpers.startAsync()
