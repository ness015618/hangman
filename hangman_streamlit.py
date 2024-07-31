import streamlit as st
import random


def button_click(letter):
    st.session_state.clicked_buttons[letter] = True
    st.session_state.suggested_letters.append(letter)
    st.session_state.nb_trials -= 1
    

def display_word():
    st.session_state.guessed_word = ""
    for letter in st.session_state.secret_word:
        if st.session_state.clicked_buttons[letter] == True:
            st.session_state.guessed_word += letter
        else:
            st.session_state.guessed_word += '\_ '
            
    if '_ ' not in st.session_state.guessed_word:
        st.session_state.is_word_found = True        
    
    return st.session_state.guessed_word


def main():

    st.title("Hangman game")

    possible_words = ['python', 'hangman', 'computer', 'keyboard', 'programming', 'algorithm', 'function', 'variable', 'syntax', 'debugging', 'compiler', 'software', 'hardware', 'network', 'database', 'interface', 'becode', 'learning', 'mathematics', 'sessions']
    
    if 'secret_word' not in st.session_state:
        st.session_state.secret_word = possible_words[random.randint(0,19)].upper()
    
    if 'nb_trials' not in st.session_state:
        st.session_state.nb_trials = len(st.session_state.secret_word) + 5
        
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    
    if 'nb_rounds' not in st.session_state:
        st.session_state.nb_rounds = 0    
    
    if 'is_word_found' not in st.session_state:
        st.session_state.is_word_found = False
    
    if 'clicked_buttons' not in st.session_state:
        st.session_state.clicked_buttons = {letter: False for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        
    if 'suggested_letters' not in st.session_state:
        st.session_state.suggested_letters = []
    
            
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13 = st.columns(13)
    
    with col1:
        st.button("A", disabled=st.session_state.clicked_buttons["A"], on_click=button_click, args=("A",))
        st.button("N", disabled=st.session_state.clicked_buttons["N"], on_click=button_click, args=("N",))

    with col2:
        st.button("B", disabled=st.session_state.clicked_buttons["B"], on_click=button_click, args=("B",))
        st.button("O", disabled=st.session_state.clicked_buttons["O"], on_click=button_click, args=("O",))

    with col3:
        st.button("C", disabled=st.session_state.clicked_buttons["C"], on_click=button_click, args=("C",))
        st.button("P", disabled=st.session_state.clicked_buttons["P"], on_click=button_click, args=("P",))

    with col4:
        st.button("D", disabled=st.session_state.clicked_buttons["D"], on_click=button_click, args=("D",))
        st.button("Q", disabled=st.session_state.clicked_buttons["Q"], on_click=button_click, args=("Q",))

    with col5:
        st.button("E", disabled=st.session_state.clicked_buttons["E"], on_click=button_click, args=("E",))
        st.button("R", disabled=st.session_state.clicked_buttons["R"], on_click=button_click, args=("R",))

    with col6:
        st.button("F", disabled=st.session_state.clicked_buttons["F"], on_click=button_click, args=("F",))
        st.button("S", disabled=st.session_state.clicked_buttons["S"], on_click=button_click, args=("S",))

    with col7:
        st.button("G", disabled=st.session_state.clicked_buttons["G"], on_click=button_click, args=("G",))
        st.button("T", disabled=st.session_state.clicked_buttons["T"], on_click=button_click, args=("T",))

    with col8:
        st.button("H", disabled=st.session_state.clicked_buttons["H"], on_click=button_click, args=("H",))
        st.button("U", disabled=st.session_state.clicked_buttons["U"], on_click=button_click, args=("U",))

    with col9:
        st.button("I", disabled=st.session_state.clicked_buttons["I"], on_click=button_click, args=("I",))
        st.button("V", disabled=st.session_state.clicked_buttons["V"], on_click=button_click, args=("V",))

    with col10:
        st.button("J", disabled=st.session_state.clicked_buttons["J"], on_click=button_click, args=("J",))
        st.button("W", disabled=st.session_state.clicked_buttons["W"], on_click=button_click, args=("W",))

    with col11:
        st.button("K", disabled=st.session_state.clicked_buttons["K"], on_click=button_click, args=("K",))
        st.button("X", disabled=st.session_state.clicked_buttons["X"], on_click=button_click, args=("X",))

    with col12:
        st.button("L", disabled=st.session_state.clicked_buttons["L"], on_click=button_click, args=("L",))
        st.button("Y", disabled=st.session_state.clicked_buttons["Y"], on_click=button_click, args=("Y",))

    with col13:
        st.button("M", st.session_state.clicked_buttons["M"], on_click=button_click, args=("M",))
        st.button("Z", disabled=st.session_state.clicked_buttons["Z"], on_click=button_click, args=("Z",))
    

 
    
    if not st.session_state.game_over:
        st.write("Trials remaining : ",st.session_state.nb_trials)  
        
        st.subheader(display_word())
        
        if st.session_state.nb_trials == 0 :
            st.session_state.game_over = True
            st.write(f"Word was : {st.session_state.secret_word}")
            
        if st.session_state.is_word_found:
            st.session_state.game_over = True
            st.write("Congratulations! You found the word.")
    
if __name__ == "__main__":
    main()