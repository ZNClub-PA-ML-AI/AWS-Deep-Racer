<pre>
[
  '{{repeat(4)}}',
  {
    all_wheels_on_track: '{{bool()}}',
    is_crashed: '{{bool()}}',

    is_left_of_center: '{{bool()}}',

    is_offtrack: '{{bool()}}',

    is_reversed: '{{bool()}}',

    heading: '{{floating(-180, 179, 2, "0.00")}}',
    steering_angle: '{{floating(-180, 179, 2, "0.00")}}',
    speed: '{{floating(0, 4, 2, "0.00")}}',
    progress: '{{floating(0, 100, 2, "0.00")}}',
    track_length: 100.0,
    track_width: 10.0,
    steps: '{{index()}}'
  }
]
</pre>
