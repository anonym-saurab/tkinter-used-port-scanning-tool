import socket                        # 'socket' is a module that is capable to provide all low-level-network functionalities
import tkinter as tk                 # Here 'tkinter' is the standerd python interface for tkinter GUI ttoolkit
from tkinter import messagebox       # 'messagebox' provides the way to create dailog boxes

def scan_port(target, port):         # Defining the function 'scan_port'
    try:                             #Here 'try' is basically used to defing some exceptions (i.e., body of 'try' may arrise some exceptions)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Here 'socket.socket' is an object that contains parameters
                                                                 # 'AF_INET' is indicates the IPv4 protocol
                                                                 # 'SOCK_STREAM' is indicates the TCP protocol(will be used for TCP connections)
        sock.settimeout(1)              # Setting a timeout (i.e., if the connection takes more tham 1 sec then an exception will be raised)
        sock.connect((target, port))    # This sets a connection to the target & the port.(if it is successfull then the port is open)
        open_ports.append(port)         # If the port is open then, this line adds the port to the 'open_ports' list
        sock.close()                    # This line closes the socket connection    
    except socket.error:            # If there 'socket.error' occurs(indicating the port is closed or error connecting),
                                        # then this line just simply passes the compiler & do nothing just to ensure that the ode do not terminates
            pass        # Port is closed or error connecting *** DO NOTHING *        

def scan_port():        # Defining the function 'scan_port()'
    # We are taking the imputs from the user in the GUI 
    # Here we are extracting the values of the user into 'target_entry', 'start_port_entry' & 'end_port_entry'
    # Converting them into integer and assigning them into 'target_host', 'start_port', 'end_port'
    target_host = target_entry.get()
    start_port = int(start_port_enrty.get())
    end_port = int(end_port_entry.get())      

    global open_ports  #Here a global variable is defined & it can be used in any line of the program
    open_ports = []    #It initializes the variable with an empty list ([]). That means the variable initially contains no elements & can be added when needed

    for port in range(start_port, end_port + 1):    #Here the function 'range' fun scans the ports between 'start_port' & the 'end_port' including the 'end_port' (+ means it includes the 'end_port')
        scan_port(target_host, port)

    if open_ports:
        messagebox.showinfo("Open Ports", f"Open Ports: {', '.join(map(str, open_ports))}")
    else:
        messsagebox.showinfo("No OpeN Ports", "No Open Ports found.")


# Creating the GUI     #This creates the main Tkinter application window and sets the title
root = tk.Tk()
root.title("Port Scanner")

# Creating Labels & Entries    # This creates a label & entry field for the target host input 
tk.Label(root, text="Target Host/IP:").grid(row=0, column=0)
target_entry = tk.Entry(root)
target_entry.grid(row=0, column=1)

tk.Label(root, text="Start Port:").grid(row=1, column=0)
start_port_enrty = tk.Entry(root)
start_port_enrty.grid(row=1, column=1)

tk.Label(root, text="End Port:").grid(row=2, column=0)
end_port_enrty = tk.Entry(root)
end_port_enrty.grid(row=2, column=1)


# Scan button       # This creates a button that will trigger the 'port_scan' function when clicked
port_scan = []
scan_button = tk.Button(root, text="Scan Ports", command= port_scan)
scan_button.grid(row=3, column=0, columnspan=2)


# Run the main event loop
root.mainloop()      # This starts the main loop for the GUI, allowing the program to respond to the users interaction