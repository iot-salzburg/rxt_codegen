import asyncio
from logging import setLogRecordFactory
import robXTask.rxtx_helpers as rxtx_helpers

import rxta_UCI2Ur10 as rxta_UCI2Ur10

async def on_rxte__message__TestUR10__rxtx_helpers(messages):
    async for message in messages:

        # ----------------------------------
        # This is the automatically generated message execution code
        # ----------------------------------
        await rxtx_helpers.logMessageReceived(message)
        print("*** on_rxte__message__TestUR10__rxtx_helpers()")
        sMessage = str(message.payload.decode("utf-8")).strip()
        print("got Message: " + sMessage)

        # ----------------------------------
        # Trying to invoke skill: GrabObject
        # ----------------------------------
        await rxtx_helpers.logSkillCall("GrabObject","1")
        await rxta_UCI2Ur10.GrabObject("Part_Cube", 1)
        bResOk = await rxta_UCI2Ur10.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"GrabObject - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"GrabObject - NOK :-)")
            sErrCode = await rxta_UCI2Ur10.GetData(rxta_UCI2Ur10.enVariables.StatusGrabObject_ErrorCode)
            sErrMsg = await rxta_UCI2Ur10.GetData(rxta_UCI2Ur10.enVariables.StatusGrabObject_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"GrabObject - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to invoke skill: GrabObject
        # ----------------------------------
        await rxtx_helpers.logSkillCall("GrabObject","2")
        await rxta_UCI2Ur10.GrabObject("Part_Cylinder", 2)
        bResOk = await rxta_UCI2Ur10.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"GrabObject - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"GrabObject - NOK :-)")
            sErrCode = await rxta_UCI2Ur10.GetData(rxta_UCI2Ur10.enVariables.StatusGrabObject_ErrorCode)
            sErrMsg = await rxta_UCI2Ur10.GetData(rxta_UCI2Ur10.enVariables.StatusGrabObject_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"GrabObject - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to send message 
        # ----------------------------------
        await rxtx_helpers.sendMessage("TestMIR", "[Empty Message Content]")
        await rxtx_helpers.stop()

rxtx_helpers.startAsync()
