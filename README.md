# rxt_codegen
- Generates Python Action Clients for ROBxTASK control from Blockly XML files
- Generates OPCUA Simulator Client for ROBxTASK simulation environment
- Call this program with three command line arguments: [inputFile][outputFile][bIsSimulatedEnv]

For directories of files please use input folder for input files and output folder for output files. 
Example usage in console: 

```python
python codegen_main.py ../input/example_2.xml ../output/generated_results/ false
```

Example "launch.json" file for debuuging with visual code / visual studio:

```python
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Aktuelle Datei",
            "type": "python",
            "request": "launch",
            "program": "./source/codegen_main.py",
            "console": "integratedTerminal",
            "args": ["./input/example_3.xml", "./output/generated_results/", "false"]
        }
    ]
}
```
