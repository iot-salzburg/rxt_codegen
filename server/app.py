from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)
swagger_url = '/codegen/swagger-ui.html'

# enable file access to yaml
@app.route(f"{swagger_url}/api")
@app.route(f"/{swagger_url}/api/<path:path>")
def send_api(path):
	return send_from_directory("api", path)

api_url = 'api/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(swagger_url, api_url, config={'app_name': "Swagger UI Codegenerator API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)
app.logger.info("Starting the platform.")

@app.route("/codegen/")
def hello():
    return "CodeGen is working."

########################################################
################# register swagger ui ##################
########################################################
@app.route(f"/codegen/<string:inputFileName>/<string:outputFileName>/<string:bIsSimulEnv>", methods=['POST', 'PUT'])
def generate_executable_code(inputFileName, outputFileName, bIsSimulEnv):
	#if not os.access(inputFileName, os.R_OK): # check if inputFile is readable by system
	#	print('Codegen called with incorrect program argument. [strInputFile] is not readable!')
	#	print('Program execution will stop now...')
	#if not os.access(outputFileName, os.W_OK): # check if outputFile is writable by system	
	#	print('Codegen called with incorrect program argument. [strOutputFile] is not writable!')
	#	print('Program execution will stop now...')
	#	sys.exit()

	xml_parser = codegen_xml_reader.XML_BlocklyProject_Parser(inputFileName)
	xml_parser.readAssets()
	
	# check if real robot mode or simulated OPCUA mode
	# creates either ROS action clients for every found asset OR
	# creates OPCUA agent for every found asset
	if bIsSimulEnv == 'false':
		ros_gen = codegen_generator_ros.ROSGeneratorClass('_client_py', xml_parser.getList())
		ros_gen.dump_all(outputFileName)
		print ("-----------------------------------------------------")
		print ("Generation of ROS action client files succesfull!")
		print ("-----------------------------------------------------")
	elif bIsSimulEnv == 'true':
		ros_gen = codegen_generator_opcua.OPCUAGeneratorClass('_client_py', xml_parser.getList())
		ros_gen.dump_all(outputFileName)
		print ("-----------------------------------------------------")
		print ("Generation of OPCUA agent files succesfull!")
		print ("-----------------------------------------------------")
	else:
		print('Codegen called with incorrect program argument. [bSimulEnv] is not a boolean!')
		print('Program execution will stop now...')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
