#!/usr/bin/env python
# coding=utf-8
import os, sys
import codegen_xml_reader
import codegen_generator_ros
import codegen_generator_opcua

# imports for flask server
import requests
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

prefix = "/codegenerator"  # url_prefix="/codegenerator/")
api_codegenerator = Blueprint("api_codegenerator", __name__)


########################################################
################## create flask app ####################
########################################################
def create_app():

	load_dotenv() # load environment variables automatically from a .env file in the same directory
	app = Flask(__name__) # Create Flask app and load configs

	# Register modules as blueprint
	#app.register_blueprint(home_bp)
	#app.register_blueprint(auth)
	#app.register_blueprint(company)
	#app.register_blueprint(system)
	#app.register_blueprint(client_app)
	#app.register_blueprint(stream_app)
	#app.register_blueprint(thing)

	# Register api as blueprint
	#app.register_blueprint(api_system)
	#app.register_blueprint(api_stream_app)
	#app.register_blueprint(api_stream_app_controller)
	#app.register_blueprint(api_client_app)
	#app.register_blueprint(api_thing)
	#app.register_blueprint(api_datastreams)
	#app.register_blueprint(api_subscriptions)

	return app


########################################################
################# register swagger ui ##################
########################################################
def register_swagger_UI(app):
	
	swagger_url = '/codegenerator/swagger-ui.html'

	# Register the Swagger ui as blueprint
	@app.route(f"{swagger_url}/api")
	@app.route(f"/{swagger_url}/api/<path:path>")
	def send_api(path):
		return send_from_directory("api", path)

	api_url = 'api/swagger.yaml'
	swaggerui_blueprint = get_swaggerui_blueprint(swagger_url, api_url, config={'app_name': "Swagger UI Codegenerator API"})
	app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)
	app.logger.info("Starting the platform.")

	return app


########################################################
################# register swagger ui ##################
########################################################
@api_codegenerator.route(f"{prefix}/codegenerator/<string:inputFileName>/<string:outputFileName>/<bool:bIsSimulEnv>", methods=['POST', 'PUT'])
def generate_executable_code(inputFileName, outputFileName, bIsSimulEnv):

	# check for correct program inputs via command line
	# only valid call if args = [strInputFile][strOutputFile][bSimulEnv]
	# sample call e.g. "python codegen_main.py ../input/example_2.xml ../output/generated_results/ false"
	#print ("-----------------------------------------------------")
	#print ('Codegen started with argument List:\n', str(sys.argv))
	#print ("-----------------------------------------------------")

	#if len(sys.argv) != 4:
	#	print('Codegen called with incorrect number of program arguments.')
	#	print('Try use the following syntax: python codegen_main.py [strInputFile][strOutputFile][bSimulEnv]')
	#	print('Program execution will stop now...')
	#	sys.exit()
	
	# trying to parser read blocks from XML project file
	# will create a list of blocks for every detected asset (SetAsset)
	#inputFileName = sys.argv[1]
	#outputFileName = sys.argv[2]
	#bIsSimulEnv = sys.argv[3].lower()

	if not os.access(inputFileName, os.R_OK): # check if inputFile is readable by system
		print('Codegen called with incorrect program argument. [strInputFile] is not readable!')
		print('Program execution will stop now...')
		sys.exit()
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
		sys.exit()

#--------------------------------------------
# main entry point for blockly codegen
#--------------------------------------------
# Author: SRFG, Mathias Schmoigl-Tonis
# Project: ROBxTASK
# Date: Q1-Q2 2022
#--------------------------------------------
if __name__== "__main__":

	# Run application
	app_basic = create_app()
	app_with_swagger = register_swagger_UI(app_basic)
	app_with_swagger.run(debug=app_with_swagger.config["DEBUG"], host="0.0.0.0", port=1908)

	