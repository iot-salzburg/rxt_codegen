# rxt_codegen
- Generates Python Action Clients for ROBxTASK control from Blockly XML files

- Generates OPCUA Simulator Client for ROBxTASK simulation environment

call this program with three command line arguments: [inputFile][outputFile][bIsSimulatedEnv]

for directories of files please use input folder for input files and output folder for output files.

Example call: python codegen_main.py ../input/example_2.xml ../output/auto_generated.py false
