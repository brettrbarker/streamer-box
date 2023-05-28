import mpv
import time

# Set to True to enable debug output
debug = True

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

if debug:
    print("Stream URL: " + stream_url)

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
time.sleep(10)

# Loop indefinitely
while True:
    if debug:
        print("Playback time: " + str(player.playback_time))
    # Wait for a short time
    time.sleep(0.5)

    # Check if the stream is frozen
    if debug:
        print("Comparing last playback time: " + str(lastPlaybackTime) + " to current playback time: " + str(player.playback_time))
    if lastPlaybackTime == player.playback_time:
        if debug:
            print("Stream is frozen. Restarting...")
        for i in range(0, maxFrozenTime):
            # Wait for a short time
            time.sleep(1)
            # Check if the stream is still frozen
            if lastPlaybackTime == player.playback_time:
                if debug:
                    print("Stream is still frozen. Restarting in " + str(maxFrozenTime - i) + " seconds...")
                if i == maxFrozenTime - 1:
                    if debug:
                        print("Stream is still frozen. Restarting now...")
                    # restart stream
                    player.play(stream_url)
                    # Sleep for 10 seconds to allow stream to start
                    time.sleep(10)
            else:
                if debug:
                    print("Stream is no longer frozen. Continuing...")
                break

    # Update the last playback time
    if debug:
        print("Updating last playback time to: " + str(player.playback_time))
    lastPlaybackTime = player.playback_time