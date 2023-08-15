##################################################
# custom function with boto3 (AWS custom module) #
##################################################

import boto3
ssm_client = boto3.client('ssm')

def get_ssm_parameter(parameter_name):
    response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
    parameter_value = response['Parameter']['Value']
    print(parameter_value)

get_ssm_parameter("amiid-nova")
get_ssm_parameter("amiid-ohio")
get_ssm_parameter("amiid-oregon")
get_ssm_parameter("/JJTech/immersionb/public")
get_ssm_parameter("/JJTech/immersionb/keyname")
get_ssm_parameter("/JJTech/immersionb/default")
get_ssm_parameter("/JJTech/immersionb/al2")
get_ssm_parameter("/JJTech/immersionb/admin")


print()
##################################
# custom function created by ME  #
##################################

def greetings(name, country):
    print("yo yo yo,,,,", name)
    print("whats cooking dawg")
    print("being a while")
    print("have you gotten a job in", country,"?")

greetings("Mike", "Canada")