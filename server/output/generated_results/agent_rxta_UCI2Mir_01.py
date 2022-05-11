import asyncio
from logging import setLogRecordFactory
import robXTask.rxtx_helpers as rxtx_helpers

import rxta_UCI2Mir as rxta_UCI2Mir

async def on_rxte__message__TestMIR__rxtx_helpers(messages):
    async for message in messages:

        # ----------------------------------
        # This is the automatically generated message execution code
        # ----------------------------------
        await rxtx_helpers.logMessageReceived(message)
        print("*** on_rxte__message__TestMIR__rxtx_helpers()")
        sMessage = str(message.payload.decode("utf-8")).strip()
        print("got Message: " + sMessage)

        # ----------------------------------
        # Trying to invoke skill: MoveToLocation
        # ----------------------------------
        await rxtx_helpers.logSkillCall("MoveToLocation","LocA")
        await rxta_UCI2Mir.MoveToLocation("LocA")
        bResOk = await rxta_UCI2Mir.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - NOK :-)")
            sErrCode = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_ErrorCode)
            sErrMsg = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"MoveToLocation - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to invoke skill: MoveToLocation
        # ----------------------------------
        await rxtx_helpers.logSkillCall("MoveToLocation","LocB")
        await rxta_UCI2Mir.MoveToLocation("LocB")
        bResOk = await rxta_UCI2Mir.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - NOK :-)")
            sErrCode = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_ErrorCode)
            sErrMsg = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"MoveToLocation - ERROR (" + sErrCode + ") - " + sErrMsg)
        
        # ----------------------------------
        # Trying to invoke skill: MoveToLocation
        # ----------------------------------
        await rxtx_helpers.logSkillCall("MoveToLocation","LocC")
        await rxta_UCI2Mir.MoveToLocation("LocC")
        bResOk = await rxta_UCI2Mir.getResultBool()
        if (bResOk):
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - OK :-)")
        else:
            await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"MoveToLocation - NOK :-)")
            sErrCode = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_ErrorCode)
            sErrMsg = await rxta_UCI2Mir.GetData(rxta_UCI2Mir.enVariables.StatusMoveToLocation_StatusMessage)
            await rxtx_helpers.log(rxtx_helpers.enLogType.ERROR,"MoveToLocation - ERROR (" + sErrCode + ") - " + sErrMsg)
        
rxtx_helpers.startAsync()
