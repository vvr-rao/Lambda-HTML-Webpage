import json

def lambda_handler(event, context):
    # TODO implement
    content = """
<html>
<body>

<h1>Chatbot</h1>

<form action="/action_page.php">
  <label for="fname">Chat: </label>
  <br>
  <body>
	<div style = "width: 450px; height: 150px; line-height: 3em; overflow:scroll; border: thin #000 solid; padding: 5px;">
    
Human: Hello, who are you?<br>

AI: I am an AI created by OpenAI. How can I help you today?<br>

Human: Hi, I am Bob<br>

AI: I will have to get back to you on that.<br>

Human: Hi, I am Paul<br>

AI: Hi Paul! I am here to help you with anything you need!<br>

Human: When will my item be shipped?<br>
    
    </div>
   <br><br><br>
  <label for="lname">Human: </label><br>
  <input type="text" style = "width: 450px" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>

<p>Click on the submit button to submit the form.</p>

</body>
</html>
    """
    response =  {
        'statusCode': 200,
        'body': content,
        "headers": {"Content-Type":"text/html"}
    }
    
    return response
