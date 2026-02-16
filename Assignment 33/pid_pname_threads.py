import psutil
import datetime

def log_thread_monitoring(filename="process_log.txt"):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open(filename, "a") as f:
            f.write(f"--- Scan at {timestamp} ---\n")
            
            # Iterate through all running processes
            for proc in psutil.process_iter(['pid', 'name', 'num_threads']):
                try:
                    # Fetch process info
                    pinfo = proc.info
                    name = pinfo['name']
                    pid = pinfo['pid']
                    threads = pinfo['num_threads']
                    
                    # Format and write to file
                    log_entry = f"PID: {pid} | Name: {name} | Threads: {threads}\n"
                    f.write(log_entry)
                    
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # These errors occur if a process closes while we are scanning
                    continue
            
            f.write("\n")
        print(f"Log successfully updated at {timestamp}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    log_thread_monitoring()