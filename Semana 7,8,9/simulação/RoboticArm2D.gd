extends Node2D

enum Space { JOINT, GLOBAL }

# Configuration of the robotic arm
var segments = []
var segment_name = ["Base"] # Add the name of the segment of the node

# Gets the name of the segment and associates with the node of the scene in godot
func _ready():
	for name in segment_name:
		var segment = get_node(name)
		segments.append(segment)

# Movements the body of the sprite based on the numbers the user insert on the interface
func move_body(pos, scale):
	move(0,pos, scale, Space.GLOBAL)
	print(pos)


func move(segment_index, target_position, scale, space = Space.JOINT):
	if segment_index < 0 or segment_index >= len(segments):
		print("Invalid segment index.")
		return

# Match the type of movement and the object in the array
	match space:

		Space.GLOBAL:
			if segment_index == 0:
				segments[segment_index].position = target_position
				var sprite = segments[segment_index].get_node("BaseSprite") # Change the values for the sprite in the object
				sprite.scale = Vector2(scale, scale)
