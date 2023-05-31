import platform
import os

class SystemInfoLogger:
    def __init__(self, output_file="C:/RepoClone/PythonProject_ext/Project_defMain/Classes/SystemData.txt"):
        self.output_file = output_file

    def get_system_info(self):
        system_info = []
        system_info.append("System Information:")
        system_info.append(f"Operating System: {platform.system()} {platform.release()}")
        system_info.append(f"Architecture: {platform.machine()}")
        system_info.append(f"Processor: {platform.processor()}")
        system_info.append(f"Python Version: {platform.python_version()}")
        return "\n".join(system_info)

    def write_to_file(self):
        system_info = self.get_system_info()
        try:
            with open(self.output_file, "w") as file:
                file.write(system_info)
            print(f"Systeeminformatie is succesvol opgeslagen in {os.path.abspath(self.output_file)}.")
        except Exception as e:
            print(f"Fout bij het opslaan van de systeeminformatie: {str(e)}")

# Gebruik van de klasse
#logger = SystemInfoLogger()
#logger.write_to_file()
