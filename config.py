# Zoom API credentials.
ACCOUNT_ID = R"rPRuPZ98RSKxykB2rtPVNA"
CLIENT_ID = R"tKuPUEzQRt6HGkvldgh8yg"
CLIENT_SECRET = R"RtIDfgJFk24BTd9TC3TZ4kJAM1CTK0iN"


# Insert non ready files flag here, if it's true only files that were not ready during last runtime will be downloaded.
NOT_READY_FILES_ONLY = False


# Put your own download path here, no need to escape backslashes but avoid ending with one.
OUTPUT_PATH = R"16Zoom/"


# Date range (inclusive) for downloads, None value for Days gets replaced by first/last day of the month.
START_DAY, START_MONTH, START_YEAR = None, 12, 2024
END_DAY, END_MONTH, END_YEAR = None, 1, 2025

# Put here emails of the users you want to check for recordings. If empty, all users under the account will be checked.
USERS = [
    # R"####@####.####",
    # R"####@####.####",
]

# Put here the topics of the meetings you wish to download recordings for. If empty, no topic filtering will happen.
TOPICS = [
    # R"############",
    # R"############"
]

# Put here the file types you wish to download. If empty, no file type filtering will happen.
RECORDING_FILE_TYPES = [
    R"MP4",            # Video file of the recording.
    # R"M4A",            # Audio-only file of the recording.
    R"TIMELINE",       # Timestamp file of the recording in JSON file format.
    R"TRANSCRIPT",     # Transcription file of the recording in VTT format.
    R"CHAT",           # A TXT file containing in-meeting chat messages that were sent during the meeting.
    R"CC",             # File containing closed captions of the recording in VTT file format.
    R"CSV",            # File containing polling data in CSV format.
#     R"SUMMARY",        # Summary file of the recording in JSON file format.
]

# If True, recordings will be grouped in folders by their owning user.
GROUP_BY_USER = True

# If True, recordings will be grouped in folders by their topics.
GROUP_BY_TOPIC = True

# If True, each instance of recording will be in its own folder (which may contain multiple files).
# Note: One "meeting" can have multiple recording instances.
GROUP_BY_RECORDING = False

# If True, participant audio files will be downloaded as well.
# This works when "Record a separate audio file of each participant" is enabled.
INCLUDE_PARTICIPANT_AUDIO = True

# Set to True for more verbose output.
VERBOSE_OUTPUT = True

# Constants used for indicating size in bytes.
B = 1
KB = 1024 * B
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

# Minimum free disk space in bytes for downloads to happen, downloading will be stalled if disk space is
# expected to get below this amount as a result of the new file.
MINIMUM_FREE_DISK = 1 * GB

# Tolerance for recording files size mismatch between the declared size in Zoom Servers and the files
# actually downloaded from the server.
# This was observed to happen sometimes on google drive mounted storage (mismatches of < 300 KBs).
# Note: High tolerance might cause issues like corrupt downloads not being recognized by script.
FILE_SIZE_MISMATCH_TOLERANCE = 100 * KB
