from tkinter import *
import requests
import bs4

# In the part below, we're creating the GUI with all these functions and his Design.
root = Tk()
root.title("Ouriel's Weather Info")

canvas = Canvas(root, height=600, width=800)
canvas.pack()

img = PhotoImage(file='weather_main_pic.png')
L = Label(root, image=img)
L.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#787871', bd=6)
frame.place(relx=0.5, rely=0.1, relwidth=0.92, relheight=0.1, anchor='n')

frame1 = Frame(root, bg='#787871', bd=6)
frame1.place(relx=0.5, rely=0.22, relwidth=0.92, relheight=0.1, anchor='n')

l = Label(frame1, text="Select  Day From Here ->", font=('calibre', 16, 'italic'), bg='white')
l.place(relwidth=0.75, relheight=1)

s = Spinbox(frame1, values=('Now', 'Today', "Tomorrow", 'Day After Tomorrow'), fg='blue', width=4,
            font=('calibre', 16, 'italic'),
            justify=CENTER)
s.place(relx=0.7, relheight=1, relwidth=0.3)

e1 = Entry(frame, font=('calibre', 16, 'italic'), justify=CENTER)
e1.place(relwidth=0.75, relheight=1)
e1.insert(0, "Enter City Name Here")

frame2 = Frame(root, bg='#787871', bd=8)
frame2.place(relx=0.5, rely=0.34, relwidth=0.92, relheight=0.6, anchor='n')

l2 = Label(frame2, text="", fg='blue', font=('calibre', 15, 'bold'), bg='white', justify=LEFT, anchor='c')
l2.place(relwidth=0.55, relheight=1)

lw = Label(frame2, text="", fg='blue', bg='white', anchor='c')
lw.place(relx=0.5, relwidth=0.5, relheight=1)


# Here I make my variables, each one with his function and his text.
def weather():
    global l2
    global cityname
    global days
    global lw
    cityname = e1.get()

    if cityname == '':
        print("Enter city name")
    else:
        if (s.get() == 'Today'):
            days = "Today"
        elif (s.get() == 'Tomorrow'):
            days = "Tomorrow"
        elif (s.get() == 'Day After Tomorrow'):
            days = "Day After Tomorrow"
        elif (s.get() == 'Now'):
            days = "Now"
        else:
            days = s.get()

        # I'm joining the url of the "site" that I want to scrap weather data.
        url = 'https://www.google.com/search?q=%s+weather+%s' % (cityname, days)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        css = '#wob_tm'

        request = requests.get(url, headers=headers)
        request.raise_for_status()
        soup = bs4.BeautifulSoup(request.text, "html.parser")

        temperature = soup.select('#wob_tm')
        timedate = soup.select('#wob_dts')
        location = soup.select('#wob_loc')
        weatherCondition = soup.select('#wob_dc')

        l = location[0].text
        t = timedate[0].text
        w = weatherCondition[0].text
        temp = temperature[0].text

        a = "Location: %s\n\nDay: %s\n\nWeather: %s\n\nTemperature: %s °C\n\n" % (l, t, w, temp)
        l2.config(text=a)
        print(a)

        # The part below have for function to join a picture to each weather category.
        if w == 'Sunny':
            img2 = PhotoImage(file="sunny.png")
        elif w == 'Mostly sunny' or w == 'Mostly cloudy' or w == 'Partly sunny' or w == 'Partly Sunny':
            img2 = PhotoImage(file="mostlysunny.png")
        elif w == 'Thunderstorm' or w == 'Isolated thunderstorms' or w == 'Scattered thunderstorms':
            img2 = PhotoImage(file="thunderstorms.png")
        elif w == 'Haze':
            img2 = PhotoImage(file="fog.png")
        elif w == 'Rain' or w == 'Light rain showers':
            img2 = PhotoImage(file="download.png")
        else:
            img2 = PhotoImage(file="def.png")

        lw = Label(frame2, image=img2, bg='white', anchor='c')
        lw.image = img2
        lw.place(relx=0.5, relwidth=0.5, relheight=1)


# In the part below we're making a Button to get weather after I choose location.
button = Button(frame, text="Click to Get Weather", fg='blue', font=('calibre', 16, 'italic'), command=weather)
button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()
