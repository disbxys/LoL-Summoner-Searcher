import tkinter

from api import RiotAPI
import config as Consts


# Variables
WINDOW_TITLE = TITLE_TEXT = 'LoL Summoner Searcher'

DESTROY_TEXT = 'END ME!'

class AppGUI():
    def __init__(self, window=tkinter.Tk()):
        # Create a root window
        self.root_window = window

        # Create Left Frame
        self.root_left = tkinter.Frame(master=self.root_window)

        # Create Right Frame
        self.root_right = tkinter.Frame(master=self.root_window)
        

        # Create a root menu
        self.root_menu = tkinter.Menu()


        # Associate root_menu with root_window
        self.root_window.config(menu=self.root_menu)


        # Set the title of the window
        self.root_window.title('Sample Program')


        # Create the label(s)
        self.title_label = tkinter.Label(
            master=self.root_window,
            text=TITLE_TEXT,
            fg="light green", bg="indigo"
            )
        self.title_label.grid(row=0,columnspan=5,
                              sticky="ew")


        # Create the exit button
        self.quit_button = tkinter.Button(
            master=self.root_window,
            text='Quit', bg="red",
            command=self.root_window.destroy
            )


        # Create the file menus
        self.region_menu = tkinter.Menu(self.root_menu)
        self.root_menu.add_cascade(label="Regions", menu=self.region_menu)
        self.display_regions()


        # Create and grid the entry box(es)
        self.create_entry_boxes()


        # Create the search button
        self.search_button = tkinter.Button(
            master=self.root_window,
            text="Search",
            command=self.search)
        self.search_button.grid(row=4, sticky=tkinter.W)


        # Create the result text box
        self.result_box = tkinter.Text(self.root_window,
                                       width=25, height=5)
        self.result_box.grid(row=5, column=3)



    def _create_region_box(self) -> None:
        self.region_label = tkinter.Label(self.root_window, text="Region:")
        self.region_label.grid(row=2, sticky="w")


        self.re = tkinter.StringVar() # Creates an object to store entries
        self.region_entry = tkinter.Entry(self.root_window,
                                          textvariable=self.re)
        self.region_entry.grid(row=2, column=2, sticky="w")


    def _create_summoner_box(self) -> None:
        self.summoner_label = tkinter.Label(self.root_window, text="Summoner:")
        self.summoner_label.grid(row=3, sticky="w")


        self.se = tkinter.StringVar() # Creates an object to store entries
        self.summoner_entry = tkinter.Entry(self.root_window,
                                            textvariable=self.se)
        self.summoner_entry.grid(row=3, column=2, sticky="w")


    def _insert_region(self, region: str) -> 'function':
        ''' Insert info '''
        def print_region() -> None:
            self.re.set('')
            self.re.set(region)

        return print_region


    def display_regions(self) -> None:
        '''Displays the regions from the config file'''
        for region in Consts.REGIONS.keys():
            self.region_menu.add_command(label=region,
            command=self._insert_region(region))


    def create_entry_boxes(self) -> None:
        '''
        Creates two pairs of label, each followed
        by boxes for input
        '''

        self._create_region_box()
        self._create_summoner_box()

    
    def run(self) -> None:
        '''Stores the call to start the app'''

        # Prevent the window from changing size
        self.root_window.resizable(0, 0)

        self.root_window.mainloop()


    def search(self):
        '''
        Take the input from the Region box and
        Summoner box and process them through
        the api.
        '''

        api = RiotAPI(Consts.API_KEY, Consts.REGIONS[self.re.get()])
        api_response = api.get_summoner_by_name(self.se.get())

        self.result_box.delete('1.0', tkinter.END)
        self.result_box.insert(
            '1.0',
            f"Name: {api_response['name']}\n"\
            f"Level: {api_response['summonerLevel']}"
        )