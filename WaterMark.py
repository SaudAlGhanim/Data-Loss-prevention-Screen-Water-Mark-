import getpass
import pywintypes
import socket
import tkinter
import win32api
import win32con
import win32ui
import win32gui


def userdata():
    x = socket.gethostbyname(socket.gethostname())
    y = getpass.getuser()
    i = '@'
    u = y + i + x
    return u


def main():
    hInstance = win32api.GetModuleHandle()
    className = 'MyWindowClassName'

    wndClass = win32gui.WNDCLASS()
    wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
    wndClass.hInstance = hInstance
    wndClass.hCursor = win32gui.LoadCursor(None, win32con.IDC_ARROW)
    wndClass.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
    wndClass.lpszClassName = className
    # win32gui does not support RegisterClassEx
    wndClassAtom = win32gui.RegisterClass(wndClass)

    #  using: WS_EX_COMPOSITED, WS_EX_LAYERED, WS_EX_NOACTIVATE, WS_EX_TOOLWINDOW, WS_EX_TOPMOST, WS_EX_TRANSPARENT
    # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT

    # Consider using: WS_DISABLED, WS_POPUP, WS_VISIBLE
    style = win32con.WS_DISABLED | win32con.WS_POPUP | win32con.WS_VISIBLE

    hWindow = win32gui.CreateWindowEx(
        exStyle,
        wndClassAtom,
        None, # WindowName
        style,
        0, # x
        0, # y
        win32api.GetSystemMetrics(win32con.SM_CXSCREEN), # width
        win32api.GetSystemMetrics(win32con.SM_CYSCREEN), # height
        None, # hWndParent
        None, # hMenu
        hInstance,
        None # lpParam
    )


def label_run():
    z = 'SATORP USE ONLY'
    label = tkinter.Label(text=userdata(), font=('Times New Roman', '80'), bg='white')
    label.master.overrideredirect(True)
    label.master.geometry("+600+350")
    label.master.lift()

    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparent", "white")
    label.master.wm_attributes("-alpha", "0.2")
    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
    # The WS_EX_TRANSPARENT flag makes events fall through the window.
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)


    label.pack()
    label.mainloop()


label_run()
