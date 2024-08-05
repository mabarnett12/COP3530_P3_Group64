from tkinter import *
import time


def a1_button_clicked():
    start_time1 = time.time()
    path_list = ["aman.com", "apple.com", "chase.com", "disney.com", "facebook.com", "getbootstrap.com",
                 "github.com", "instagram.com", "microsoft.com", "mozilla.org",
                 "openai.com", "pcbuildinguf.com", "python.org", "reactjs.org", "roblox.com", "samsung.com",
                 "stackoverflow.com", "twitter.com", "ufl.edu", "weather.com", "youtube.com", "zoom.us"]
    populate_listbox(path_list)
    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    elapsed_time_label1 = Label(main, text=f"Run Time for Algorithm 1: {elapsed_time1:.6f}",
                                font=('calibre', 10, 'bold'))
    elapsed_time_label1.grid(row=9, column=1)

    '''
    # test for user input, displayed to window temporarily
    begin_page_display_label = Label(main, text=f"Begin Page: {begin_page.get()}",
                                     font=('calibre', 10, 'bold'))
    begin_page_display_label.grid(row=12, column=1)
    end_page_display_label = Label(main, text=f"End Page: {end_page.get()}",
                                   font=('calibre', 10, 'bold'))
    end_page_display_label.grid(row=13, column=1)
    print(begin_page.get())
    print(end_page.get())
    '''

def a2_button_clicked():
    start_time2 = time.time()
    path_list = ["aman.com", "apple.com", "chase.com", "disney.com", "facebook.com", "getbootstrap.com", "github.com",
                 "instagram.com", "microsoft.com", "mozilla.org",
                 "openai.com", "pcbuildinguf.com", "python.org", "reactjs.org", "roblox.com", "samsung.com",
                 "stackoverflow.com", "twitter.com", "ufl.edu", "weather.com", "youtube.com", "zoom.us"]
    populate_listbox(path_list)
    end_time2 = time.time()
    elapsed_time2 = end_time2 - start_time2
    elapsed_time_label2 = Label(main, text=f"Run Time for Algorithm 2: {elapsed_time2:.6f}",
                                font=('calibre', 10, 'bold'))
    elapsed_time_label2.grid(row=10, column=1)


# Function to populate the listbox with the list of path strings
def populate_listbox(strings):
    for item in strings:
        path_listbox.insert(END, item)


# if __name__ == '__main__':


# create main display window
main = Tk()
main.geometry("800x900")

# Add Wikipedia logo to window
original_wiki_logo = PhotoImage(file='wikipedia.logo.png')
wiki_logo = original_wiki_logo.subsample(1, 1)
logo_label = Label(image=wiki_logo)
logo_label.grid(row=0, column=0)

# add title to window
title_label = Label(main, text="WikiRacer Algorithm Tester", font=16)
title_label.grid(row=0, column=1)

# add description to window
desc_text = Message(main, text="Compare Algorithms to see which one will help you find the shortest path between "
                               "WikiPedia pages the fastest!", width=300, justify=CENTER)
desc_text.grid(row=1, column=1)

# set up variable to receive user input for begin and end page and display fields
begin_page = StringVar()
end_page = StringVar()

begin_page_label = Label(main, text='Begin Page', font=('calibre',10, 'bold'))
begin_page_entry = Entry(main, textvariable=begin_page, font=('calibre',10,'normal'), width=75)

end_page_label = Label(main, text='End Page', font=('calibre',10, 'bold'))
end_page_entry = Entry(main, textvariable=end_page, font=('calibre',10,'normal'), width=75)

begin_page_label.grid(row=2, column=0, pady=5)
begin_page_entry.grid(row=2, column=1, pady=5)
end_page_label.grid(row=3, column=0, pady=5)
end_page_entry.grid(row=3, column=1, pady=5)


# add run buttons to window
run_A1_button = Button(main, text="Run Algorithm 1", fg="gold", bg="black", command=a1_button_clicked)
run_A1_button.grid(row=6, column=1)

run_A2_button = Button(main, text="Run Algorithm 2", fg="gold", bg="black", command=a2_button_clicked)
run_A2_button.grid(row=7, column=1, pady=10)


# Create a listbox to display pages in shortest path
path_listbox = Listbox(main, width=50, height=15,
                       bg="grey",
                       activestyle='dotbox',
                       font="Helvetica",
                       fg="yellow")
path_listbox.grid(row=8, column=1)

# Create a scrollbar for the listbox
scrollbar = Scrollbar(main, orient="vertical", troughcolor="gold")
scrollbar.config(command=path_listbox.yview)
scrollbar.grid(row=8, column=2, sticky='ns', pady=10)

# Attach the scrollbar to the listbox
path_listbox.config(yscrollcommand=scrollbar.set)

main.mainloop()