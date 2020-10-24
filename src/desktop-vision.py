import sys

LINUX_OS = "linux"
WINDOWS_OS = "win32"
MAC_OS = "darwin"

# TODO define interface and implement 3 separate classes. One for each OS
class DesktopVision:

  def __init__(self):
    self.__user_os: str = sys.platform

  
  def get_window_in_focus(self):
    if self.__user_os == LINUX_OS:
      return self.__get_window_in_focus_lnx()

    if self.__user_os == WINDOWS_OS:
      pass

    if self.__user_os == MAC_OS:
      pass
    
    raise Exception("OS detected is not supported: ", self.__user_os)
    

  def __get_window_in_focus_lnx(self) -> str:
    return("code")
  

def main():
  desktop_vision = DesktopVision()
  print("window in focus: ", desktop_vision.get_window_in_focus())
  

if __name__ == "__main__":
  main()