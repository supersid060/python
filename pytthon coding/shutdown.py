import os
import platform
import sys

def shutdown(confirm=True):
    """
    Shutdown the computer safely.
    :param confirm: If True, asks for user confirmation before shutdown.
    """
    try:
        
        if confirm:
            user_input = input("Are you sure you want to shut down the computer? (yes/no): ").strip().lower()
            if user_input not in ("yes", "y"):
                print("Shutdown cancelled.")
                return

        
        current_os = platform.system()

        if current_os == "Windows":
            os.system("shutdown /s /t 1")  # /s = shutdown, /t 1 = 1 second delay
        elif current_os == "Linux" or current_os == "Darwin":  
            os.system("sudo shutdown now")
        else:
            print(f"Unsupported operating system: {current_os}")
    except Exception as e:
        print(f"Error while attempting shutdown: {e}")
        sys.exit(1)


if __name__ == "__main__":
    shutdown(confirm=True)
