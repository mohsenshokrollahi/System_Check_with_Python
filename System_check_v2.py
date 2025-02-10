import psutil

def get_system_info():
    # Get CPU information
    cpu_info = psutil.cpu_times_percent(interval=1, percpu=False)
    
    # Get memory information
    memory_info = psutil.virtual_memory()
    
    # Get disk usage information
    disk_info = psutil.disk_usage('/')
    
    # Format the information into a readable format
    system_info = f"""
    System Information:
    -------------------
    CPU Usage:
        User: {cpu_info.user}%
        System: {cpu_info.system}%
        Idle: {cpu_info.idle}%
    
    Memory Usage:
        Total: {memory_info.total / (1024 ** 3):.2f} GB
        Available: {memory_info.available / (1024 ** 3):.2f} GB
        Used: {memory_info.used / (1024 ** 3):.2f} GB
        Percentage: {memory_info.percent}%
    
    Disk Usage:
        Total: {disk_info.total / (1024 ** 3):.2f} GB
        Used: {disk_info.used / (1024 ** 3):.2f} GB
        Free: {disk_info.free / (1024 ** 3):.2f} GB
        Percentage: {disk_info.percent}%
    """
    
    return system_info

# Fetch and print the system information
print(get_system_info())