
import subprocess
import time


def main():
    time.sleep(0.5)
    # Change directory to the specified path
    subprocess.Popen(['cmd.exe', '/k', 'cd',
                     'D:\\Downloads\\Ongoing_Ass\\TUP_4th_yr\\UPDATE_onprem_bucal\\on_prem_dashboard'])

    # Run 'ionic serve' within the same command prompt
    subprocess.Popen(['cmd.exe', '/k', 'ionic', 'serve'])
    # presses any key after 20 sec
    time.sleep(20)
    subprocess.Popen(['cmd.exe', '/k', '.'])


if __name__ == "__main__":
    main()
