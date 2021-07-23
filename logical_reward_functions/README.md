# All Stategies for Deep Racer


x and y	The position of the vehicle on the track
heading	Orientation of the vehicle on the track
waypoints	List of waypoint coordinates
closest_waypoints	Index of the two closest waypoints to the vehicle
progress	Percentage of track completed
steps	Number of steps completed
track_width	Width of the track
distance_from_center	Distance from track center line
is_left_of_center	Whether the vehicle is to the left of the center line
all_wheels_on_track	Is the vehicle completely within the track boundary?
speed	Observed speed of the vehicle
steering_angle	Steering angle of the front wheels

1) all_wheels_on_track -> reward = false <<<<<< true | penalize
2) distance_from_center -> reward = trackwidth/2 < x < 0
3) closest_waypoints, waypoints, heading -> track_direction - heading = direction_diff



Solution Ideas

1) Distance from center strategy
2) Waypoint vs heading direction
3) 1+2
4) Sectorization + Intersections + caution points <
5) Gradient in all above
6) Steps (TBD)


Questions

> waypoints

1) If we are to stay on straight path, how do we find it
2) how to find the points areound which we need to curve 
