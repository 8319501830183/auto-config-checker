import subprocess
from pathlib import Path


dir = Path(__file__).resolve().parent
config_list_path = dir / "config-list.txt"
checker_path = dir / "xray-checker.exe"
try:
    with open(config_list_path, "r") as file:
        urls = file.readlines()
        cmd = [checker_path,]
        for url in urls:
            cmd.append(f"--subscription-url={url}")
        print("Metrics: http://0.0.0.0:2112/")
        print("Press Ctrl+C to exit")

        out = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

except KeyboardInterrupt:
    print("Exitting..")
    
except Exception as e:
    print(e)
