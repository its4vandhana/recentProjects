import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    try:
        if http_method == 'POST':
            # CREATE a student
            student = json.loads(event['body'])
            table.put_item(Item=student)
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Student added successfully'})
            }
        
        elif http_method == 'GET':
            # Check if path parameter exists
            if 'pathParameters' in event and event['pathParameters'] and 'studentId' in event['pathParameters']:
                # GET specific student
                student_id = event['pathParameters']['studentId']
                response = table.get_item(Key={'studentId': student_id})
                if 'Item' in response:
                    return {
                        'statusCode': 200,
                        'body': json.dumps(response['Item'])
                    }
                else:
                    return {
                        'statusCode': 404,
                        'body': json.dumps({'message': 'Student not found'})
                    }
            else:
                # GET all students
                response = table.scan()
                return {
                    'statusCode': 200,
                    'body': json.dumps(response['Items'])
                }

        elif http_method == 'PUT':
            student_id = event['pathParameters']['studentId']
            student_data = json.loads(event['body'])

            update_expression = "set "
            expression_attribute_values = {}
            update_parts = []

            for key in ['name', 'age', 'course']:
                if key in student_data:
                    update_parts.append(f"{key} = :{key}")
                    expression_attribute_values[f":{key}"] = student_data[key]

            if not update_parts:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'No valid fields provided for update'})
                }

            update_expression += ", ".join(update_parts)

            response = table.update_item(
                Key={'studentId': student_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Student updated successfully',
                    'updatedAttributes': response['Attributes']
                })
            }

        elif http_method == 'DELETE':
            student_id = event['pathParameters']['studentId']
            response = table.delete_item(
                Key={'studentId': student_id},
                ReturnValues='ALL_OLD'
            )

            if 'Attributes' in response:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'message': 'Student deleted successfully'})
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({'message': 'Student not found'})
                }

        else:
            return {
                'statusCode': 405,
                'body': json.dumps({'message': 'Method not allowed'})
            }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }