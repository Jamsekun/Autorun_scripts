
import subprocess
import time


def main():

    # change this variables BEFORE YOU START
    local_ip = '192.168.1.4'
    dashboard_port: str = '8100'
    admin_api_port = '8000'
    environment_name = 'jamsenv'

    # Change directory to the specified path of your repo
    dashboard_path = r'C:\Jamsekun_DomainExpansion\Programming_Dungeon\FrontEnd_cell\Hiraya-Practice-main\Bucal_onprem\on_prem_dashboard'
    plc_opcua_path = r'C:\Jamsekun_DomainExpansion\Programming_Dungeon\FrontEnd_cell\Hiraya-Practice-main\Bucal_onprem\on_prem_plc_opcua'
    rtap_admin_api_path = r'C:\Jamsekun_DomainExpansion\Programming_Dungeon\FrontEnd_cell\Hiraya-Practice-main\Bucal_onprem\on_prem_rtap_admin_api'

    # Change directory to the specified path
    subprocess.Popen(['cmd.exe', '/k', 'cd', '/d',
                     plc_opcua_path, '&&', 'npm', 'run', 'backup'])
    time.sleep(1)

    subprocess.Popen(['cmd.exe', '/k', 'cd', '/d',
                     rtap_admin_api_path, '&&', f'.\\{environment_name}\\Scripts\\activate', '&&', 'python', 'manage.py', 'runserver', f'{local_ip}:{admin_api_port}'])

    time.sleep(1)

    subprocess.Popen(['cmd.exe', '/k', 'cd', '/d',
                      dashboard_path, '&&', 'set', 'NODE_OPTIONS=--max-old-space-size=8192', '&&', 'ionic', 'serve', '--host', local_ip, '--port', dashboard_port, '--disable-host-check', '--public-host', local_ip])
    # subprocess.Popen(['cmd.exe', '/k', '.'])
    # Run 'ionic serve' within the same command prompt
    # subprocess.Popen(['cmd.exe', '/k', 'npm', 'run', 'backup'])
    # presses any key after 20 sec
    # time.sleep(20)
    # subprocess.Popen(['cmd.exe', '/k', '.'])


if __name__ == "__main__":
    main()
