import psutil
import sys
import os
import time
import schedule

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def MarvellousMail(LogFileName, ReceiverMail, Data):
    # Credentials
    Sender_Email = "anushree.python.test@gmail.com"
    App_Password = "lqhb jula twvi gbbx"
    
    # Generate Summary for email body text
    total_p = len(Data)
    Data.sort(key = lambda x : x['cpu_percent'], reverse = True)
    top_cpu = Data[:5]

    body = "Jay Ganesh...\n\n"
    body = body + "This is a system surveillance report.\n"
    body = body + "Total Processes: " + str(total_p) + "\n\n"
    body = body + "Top 5 CPU Consuming Processes:\n"
    for p in top_cpu:
        body = body + p['name'] + " : " + str(p['cpu_percent']) + "%\n"
    
    body = body + "\nPlease find the detailed log attached.\n\nRegards,\nMarvellous Infosystems"

    msg = MIMEMultipart()
    msg['From'] = Sender_Email
    msg['To'] = ReceiverMail
    msg['Subject'] = "Marvellous System Report"
    msg.attach(MIMEText(body, 'plain'))

    # Attach Log File using basic open/read
    f = open(LogFileName, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(f.read())
    f.close()

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(LogFileName))
    msg.attach(p)

    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(Sender_Email, App_Password)
        smtp.send_message(msg)
        smtp.quit()
        print("Marvellous Mail Sent Successfully to: " + ReceiverMail)
    except Exception as e:
        print("Unable to send mail: ", e)

def CreateLog(FolderName, ReceiverMail):
    Border = "_"*50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)
    print("Log File created: ", FileName)

    fobj = open(FileName, "w")
    
    fobj.write(Border + "\n")
    fobj.write("---- Marvellous Platform Surveillance System ----\n")
    fobj.write("Log created at: " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    # System Report
    fobj.write("CPU Usage: " + str(psutil.cpu_percent()) + " %\n")
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage: " + str(mem.percent) + " %\n")
    fobj.write(Border + "\n")

    # Process Scan
    Data = ProcessScan()

    # --- SUMMARY SECTION (using fobj.write) ---
    fobj.write("\n-------------------- SUMMARY REPORT --------------------\n")
    fobj.write("Total Processes: " + str(len(Data)) + "\n\n")

    # Top CPU
    Data.sort(key=lambda x: x['cpu_percent'], reverse=True)
    fobj.write("Top 5 CPU Usage Processes:\n")
    for p in Data[:5]:
        fobj.write(p['name'] + " : " + str(p['cpu_percent']) + "%\n")
    
    # Top Memory
    Data.sort(key=lambda x: x['memory_percent'], reverse=True)
    fobj.write("\nTop 5 Memory Usage Processes:\n")
    for p in Data[:5]:
        fobj.write(p['name'] + " : " + str(round(p['memory_percent'], 2)) + "%\n")

    # Top Threads
    Data.sort(key=lambda x: x['num_threads'], reverse=True)
    fobj.write("\nTop 5 Thread Count Processes:\n")
    for p in Data[:5]:
        fobj.write(p['name'] + " : " + str(p['num_threads']) + "\n")

    fobj.write("--------------------------------------------------------\n\n")

    # --- DETAILED PROCESS LOG ---
    for info in Data:
        fobj.write("PID: " + str(info.get("pid")) + "\n")
        fobj.write("Name: " + str(info.get("name")) + "\n")
        fobj.write("Threads: " + str(info.get("num_threads")) + "\n")
        fobj.write("Open Files: " + str(info.get("open_files_count")) + "\n")
        fobj.write("RSS (Actual RAM): " + str(round(info.get("rss"), 2)) + " MB\n")
        fobj.write("VMS (Virtual Memory): " + str(round(info.get("vms"), 2)) + " MB\n")
        fobj.write("CPU %: " + str(info.get("cpu_percent")) + "\n")
        fobj.write("Memory %: " + str(round(info.get("memory_percent"), 2)) + "\n")
        fobj.write(Border + "\n")

    fobj.write("\n---------------- End Of Log File ----------------\n")
    fobj.close()

    # Send Mail
    MarvellousMail(FileName, ReceiverMail, Data)

def ProcessScan():
    listprocess = []
    # Warm up
    for proc in psutil.process_iter():
        try: proc.cpu_percent()
        except: pass
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time", "num_threads", "memory_info"])
            
            # Memory Allocation Logic
            mem_info = info.get("memory_info")
            if mem_info:
                info["rss"] = mem_info.rss / (1024 * 1024)
                info["vms"] = mem_info.vms / (1024 * 1024)
            else:
                info["rss"] = 0
                info["vms"] = 0

            # Open Files Logic
            try:
                info["open_files_count"] = len(proc.open_files())
            except (psutil.AccessDenied):
                info["open_files_count"] = "Access Denied"
            except:
                info["open_files_count"] = 0
            
            info["cpu_percent"] = proc.cpu_percent(interval=None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "--h":
            print("Usage: Script.py FolderName ReceiverEmail Interval")
            return

    elif len(sys.argv) == 4:
        FolderName = sys.argv[1]
        ReceiverEmail = sys.argv[2]
        Interval = int(sys.argv[3])

        print("Automation started. Press Ctrl+C to stop.")
        schedule.every(Interval).minutes.do(CreateLog, FolderName, ReceiverEmail)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Arguments. Use --h for help.")

if __name__ == "__main__":
    main()