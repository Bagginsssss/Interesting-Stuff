def mylittleproject():
    import tkinter
    from tkinter import ttk, OptionMenu
    from translate import Translator

    Screen = tkinter.Tk()
    Screen.title("English to Arabic")
    Screen.geometry("450x200")

    InputLanguageChoice = tkinter.StringVar()
    TranslateLanguageChoice = tkinter.StringVar()

    LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Spansih', 'Arabic'}
    InputLanguageChoice.set('English')
    TranslateLanguageChoice.set('Arabic')

    def Translate():
        translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=TranslateLanguageChoice.get())
        Translation = translator.translate(TextVar.get())
        OutputVar.set(Translation)

    InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
    tkinter.Label(Screen, text="Choose a Language").grid(row=0, column=1)
    InputLanguageChoiceMenu.grid(row=1, column=1)

    NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
    tkinter.Label(Screen, text="Translated Language").grid(row=0, column=3)
    NewLanguageChoiceMenu.grid(row=1, column=3)

    tkinter.Label(Screen, text="Enter Text").grid(row=2, column=0)
    TextVar = tkinter.StringVar()
    TextBox = tkinter.Entry(Screen, textvariable=TextVar).grid(row=2, column=1)

    tkinter.Label(Screen, text="Translated Text").grid(row=2, column=2)
    OutputVar = tkinter.StringVar()
    TextBox = tkinter.Entry(Screen, textvariable=OutputVar).grid(row=2, column=3)

    # Button for calling function
    B = tkinter.Button(Screen, text="Translate", command=Translate, relief=tkinter.GROOVE).grid(row=3, column=1, columnspan=3)

    tkinter.mainloop()
    
mylittleproject()


