class Hint:
  '''params
  {
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center
}
  '''
  def __init__(params: dict):
    self.position = (params['X'], params['Y'])
    self.speed = params['speed']
    self.heading = params['heading']
    self.steering = params['steering_angle']
    self.progress = params['progress']
    self.center_distance = params['distance_from_center'] * (1 if params['is_left_of_center'] else -1)
    self.is_negative_state = any([params['is_offtrack'], params['is_reversed'], params['is_crashed'], not params['all_wheels_on_track']]) 
  
  def is_fast_at_curve(self)-> bool:
    '''to do'''
    return True
  
  def get_heading_direction(direction: float)-> bool:
    '''
    The heading parameter describes the orientation of the vehicle in degrees, measured counter-clockwise from the X-axis of the coordinate system.
    '''
    directions = {'UP': (5.0, 85.0), 'DOWN': (-5.0, -85.0), }
    result = 'ANY'
    for direction, coverage in directions.items(): 
      if coverage[0] < direction or direction < coverage[1]:
        result = direction
    return result
  

  
 
     
