import asyncio
from logging import setLogRecordFactory
import robXTask.rxtx_helpers as rxtx_helpers

async def startRobXTask():
    # This is the automatically generated main-code with the start message to begin workflow
    print("*** startRobXTask")
    await rxtx_helpers.sleep(5)
    await rxtx_helpers.log(rxtx_helpers.enLogType.INFO,"agent_01_Controller - First Log")
    await rxtx_helpers.sendMessage("TestCamera", "[Empty Message Content]")

async def on_rxte__message__WorkflowEnded__rxtx_helpers(messages):
    async for message in messages:
        await rxtx_helpers.logMessageReceived(message)
        print("*** on_rxte__message__Ur10Tested__rxtx_helpers()")
        sMsg = str(message.payload.decode("utf-8")).strip()
        print("Total Workflow was Tested: " + sMsg)
        await rxtx_helpers.stop()

rxtx_helpers.startAsync()
