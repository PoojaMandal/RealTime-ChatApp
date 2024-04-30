import json

def convert_data(data):
    try:
        post_data = data.decode('utf8')
        post_data = json.loads(post_data)
    except Exception as e:
        print(e)
        post_data = None
    return post_data
