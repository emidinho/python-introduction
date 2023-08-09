# import boto3
# ssm_client = boto3.client('ssm')


# def get_ssm_parameter(parameter_name):
#     response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
#     parameter_value = response['Parameter']['Value']
#     print(parameter_value)

# get_ssm_parameter("AMIID")


def greetings(name, country):
    print("yo yo yo,,,,", name)
    print("whats cooking dawg")
    print("being a while")
    print("have you gotten a job in", country,"?")

greetings("Mike", "Canada")