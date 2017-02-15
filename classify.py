#!/usr/bin/env python
# Author: Scott Phillpott
# UDF for extracting Aegis Ship names from a selected corpus


from deepdive import *  #Required for @tsv_extractor and @returns

ships 			= [...]
ship_classes		= [...]
ship_names		= [...]

@tsv_extractor	#Declares the generator below as the main fuction to call
@returns(lamdba # Declares the types of output columns as declared in DDLog
		article_id 	= "int",
		ship_classes = "text",
	:[])

def classify(  # The input types can be declared directly on each parameter as its default value
		article_id = "int",) 	
