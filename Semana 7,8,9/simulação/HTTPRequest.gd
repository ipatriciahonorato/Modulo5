extends HTTPRequest
signal move_object(position)


# Variables
var update_interval = 1.0  # Time interval between requests (in seconds)
var url = "http://127.0.0.1:3000/pos"  # URL of the API

# Function _ready
func _ready():
	set_process(true)  # Enable node processing
	self.request_completed.connect(self._on_request_completed) # Connects the on request_completed to the http event
	# Start the update loop
	request_positions()

# Function _process
func _process(delta): #Indicates the time interval between http requests
	update_interval -= delta
	if update_interval <= 0: # in the value 0, the fuction will run and return the value to 1.0
		update_interval = 1.0 
		request_positions()

# Function to trigger the request http
func request_positions():
	request(url)

func _on_request_completed(result, response_code, headers, body):
	if response_code == 200: # Check if the response is valid (HTTP status 200)
		var js = JSON.new()  # Create a JSON instance
		js.parse(body.get_string_from_utf8())  # Use the parse() method on the instance
		handle_response(js.data)
	else:
		print("Erro na requisição HTTP:", response_code)
		
# Function to get the position from the responde
func handle_response(data):
	var position = Vector2(data.x, data.y) # get the positions of the axles X an Y
	var object_node = get_node("/root/RoboticArm2D") # get the main node of the scene in godot 
	object_node.move_body(position, data.z) # move the body based on the position
	
