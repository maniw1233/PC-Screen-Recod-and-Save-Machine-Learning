import cv2
import numpy as np
import pyautogui
import time

def record_screen(region, output_file, fps=20):
    """
    Records a specified screen region and saves it to a video file.
    Recording continues until the user presses 'q'.

    Parameters:
    - region (tuple): The region to capture as (x, y, width, height).
    - output_file (str): The path to the output video file.
    - fps (int): Frames per second for the video.
    """

    # Get the screen width and height from the region
    width, height = region[2], region[3]

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print("Press 'q' to stop recording...")

    while True:
        # Capture the screen region
        img = pyautogui.screenshot(region=region)

        # Convert the image to an array
        frame = np.array(img)

        # Convert RGB to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Check for user input to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything
    out.release()
    cv2.destroyAllWindows()
    print("Recording finished and saved to", output_file)

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Define the region as the entire screen
region = (0, 0, screen_width, screen_height)

# Path to save the video
output_file = "window_record.avi"

# Record the screen
record_screen(region, output_file)
