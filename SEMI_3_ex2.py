import tkinter as tk
import os

# EXERCICE 2
# ref: https://stackoverflow.com/questions/51611929/saving-a-optionmenu-input-tkinter
if __name__ == '__main__':
    video = 'BBB_1_min.mp4'

    # definim la finestra
    win = tk.Tk()
    win.geometry("300x150")
    win.title("Video Converter Program")

    resolution = ['720p', '480p', '360x240', '160x120']
    codec = ['vp8', 'vp9', 'h265', 'av1']

    var1 = tk.StringVar(win)
    var2 = tk.StringVar(win)

    # creem el widget per escollir la resolucio
    popupMenu = tk.OptionMenu(win, var1, *resolution)
    tk.Label(win, text='Choose a video resolution: ').grid(row=5, column=1, sticky=tk.W)
    popupMenu.grid(row=5, column=2, sticky=tk.W)

    # creeem el widget per escollir el codec
    popupMenu = tk.OptionMenu(win, var2, *codec)
    tk.Label(win, text="Choose a video codec: ").grid(row=6, column=1, sticky=tk.W)
    popupMenu.grid(row=6, column=2, sticky=tk.W)


    def conversion():
        arx = ['mkv', 'mp4', 'mp4', 'mkv']
        c = ['libvpx', 'libvpx-vp9', 'libx265', 'libaom-av1']
        res = var1.get()
        cod = var2.get()

        # definim i i cc per tal d'agafar la terminació de cada codec i el format
        i = arx[codec.index(cod)]
        cc = c[codec.index(cod)]

        # fem diferencia per la resolucio si es 720p o 480p que s'escriu diferent
        if res == resolution[0] or res == resolution[1]:
            com = 'ffmpeg -i ' + video + ' -vf scale=-1:' + res + ' -c:v ' + cc + ' BBB_{0}_{1}.{2}'.format(res, cod, i)
            os.system(com)
        else:
            com = 'ffmpeg -i ' + video + ' -vf scale=' + res + ' -c:v ' + cc + ' BBB_{0}_{1}.{2}'.format(res, cod, i)
            os.system(com)


    button = tk.Button(win, text="Start Conversion", command=conversion, bg='red', fg='white', activebackground='green',
                       activeforeground='white').grid(row=7, column=1, sticky=tk.W)

    win.mainloop()

    # mostrem el resultat
    print("resolution = {}, \ncodec = {}".format(var1.get(), var2.get()))
