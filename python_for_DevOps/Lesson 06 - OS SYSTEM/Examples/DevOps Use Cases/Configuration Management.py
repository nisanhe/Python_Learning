import configparser

# Read a configuration file
config = configparser.ConfigParser()
config.read("config.ini")

# Access configuration values
host = config["DEFAULT"]["host"]
port = config["DEFAULT"]["port"]

# Write to a configuration file
config["DEFAULT"]["new_value"] = "new_value"
with open("config.ini", "w") as config_file:
    config.write(config_file)