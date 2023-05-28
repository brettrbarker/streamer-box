import mpv
import time
import logging
import os

# Create the logs directory if it doesn't exist
if not os.path.exists('mpv-logs'):
    os.makedirs('mpv-logs')


# Setup Logging
logging.basicConfig(filename='mpv-logs/current.log', 
                    encoding='utf-8', 
                    level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    datefmt='%Y-%m-%dT%H:%M:%S%z')

# Log the start of the script
logging.info('Starting MPV Streaming Script')

# Define the URL of the stream
stream_url = ""
# Check if the stream URL is empty
if stream_url == "":
    # If the stream URL is empty, ask for it
    stream_url = input("Enter the stream URL: ")
    if stream_url == "":
        # If the stream URL is still empty, exit
        print("Stream URL cannot be empty. Exiting...")
        exit()

logging.info("Stream URL: " + stream_url)

# Create an MPV player instance
player = mpv.MPV()

# Uncomment the following line to enable fullscreen
# player.fullscreen = True

# Load the stream URL
player.play(stream_url)

# Set the initial playback time
lastPlaybackTime = 0

# Set time to wait while frozen before restarting
maxFrozenTime = 10

# Allow stream 10 seconds to start before checking
logging.debug("Waiting 10 seconds for stream to start...")
time.sleep(10)

# Loop indefinitely
while True:
    logging.debug("Playback time: " + str(player.playback_time))
    # Wait for a short time
    time.sleep(0.5)

    # Check if the stream is frozen
    logging.debug("Comparing last playback time: " + str(lastPlaybackTime) + " to current playback time: " + str(player.playback_time))
    if lastPlaybackTime == player.playback_time:
        logging.warning("Stream is frozen. Monitoring for Restart.")
        for i in range(0, maxFrozenTime):
            # Wait for a short time
            time.sleep(1)
            # Check if the stream is still frozen
            if lastPlaybackTime == player.playback_time:
                logging.warning("Stream is still frozen. Restarting in " + str(maxFrozenTime - i) + " seconds...")
                if i == maxFrozenTime - 1:
                    logging.warning("Stream is still frozen. Restarting now...")
                    # restart stream
                    player.play(stream_url)
                    # Sleep for 10 seconds to allow stream to start
                    time.sleep(10)
            else:
                logging.warning("Stream is no longer frozen. Continuing...")
                break

    # Update the last playback time
    logging.debug("Updating last playback time to: " + str(player.playback_time))
    lastPlaybackTime = player.playback_time