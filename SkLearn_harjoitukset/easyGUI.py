import easygui

#easygui.msgbox('How you doing!', title='Haista paska painu helvettiin siitä!',
#              ok_button='Paina')
def ikkuna(kuva):
    easygui.buttonbox('Mitä mieltä olet tästä?', title='Kyssäri',
                      choices=['Tykkään', 'En tykkää'], image=kuva)
    easygui.buttonbox('Valitse jotain',
                      choices=['Kissa', 'Koira', 'Niilo22'],
                      title='Otsikko')

ikkuna()

