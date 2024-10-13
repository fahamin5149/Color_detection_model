- **Color Masking**: Utilizes a custom function, `get_limits`, to define the lower and upper HSV limits for the target color, creating a binary mask that highlights areas of interest.

- **Bounding Box**: When the specified color is detected, a bounding box is drawn around it, visually indicating the detected area in the video feed.

- **Real-Time Processing**: Continuously captures frames until the user presses 'q', providing immediate feedback on color detection.
