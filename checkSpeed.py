import speedtest
import datetime
import os
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="Check Internet Speed Utility",
    description="Check internet speed and log results to a CSV file.",
    epilog="Example usage: python checkSpeed.py cisu_output.csv",
)

parser.add_argument(
    "filePath",
    nargs="?",
    default="cisu_output.csv",
    help="Path to the output CSV file (default: cisu_output.csv)",
)

filePath = parser.parse_args().filePath

print(datetime.datetime.now().strftime("%H:%M:%S") + " starting... ")

existed = os.path.exists(filePath)

with open(filePath, "a") as f:
    if not existed:
        f.write("Date, Time, Server, Download (Mbps), Upload (Mbps), Ping (ms)\n")

    st = speedtest.Speedtest()
    date = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    download = st.download() / 1_000_000
    print("download")
    upload = st.upload() / 1_000_000
    print("upload")
    ping = st.results.ping
    print("ping")
    server = '"' + st.results.server["name"] + '"'
    print("server")

    f.write(f"{date}, {time}, {server}, {download}, {upload}, {ping}\n")

print("done " + datetime.datetime.now().strftime("%H:%M:%S") + "\n")
