kb_name = "restaurant-assistant"
dynamodb = boto3.resource("dynamodb")
smm_client = boto3.client("ssm")
table_name = smm_client.get_parameter(
    Name=f"{kb_name}-table-name", WithDecryption=False
)
table = dynamodb.Table(table_name["Parameter"]["Value"])
kb_id = smm_client.get_parameter(Name=f"{kb_name}-kb-id", WithDecryption=False)
print("DynamoDB table:", table_name["Parameter"]["Value"])
print("Knowledge Base Id:", kb_id["Parameter"]["Value"])
