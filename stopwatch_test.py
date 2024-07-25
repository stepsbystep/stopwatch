import streamlit as st
from datetime import datetime as dt
import datetime

from stopwatch import stopwatch

import streamlit as st
import datetime
from datetime import datetime as dt



if "final_started" not in st.session_state:
    st.session_state.final_started=False
    st.session_state.final_loop=True

if True:
    reportContainer = st.container(border=True)
    
    if st.session_state.final_loop:
        with reportContainer:
            # big display of elapsed time
            if "elapsedTime" not in st.session_state:
                ET=dt.now()-dt.now()
            else:
                ET=st.session_state.elapsedTime
            print("ET new:", ET)
            time60=(dt.min+datetime.timedelta(seconds=1+60*ET.total_seconds())).time()
            time60upd = st.time_input("Entered time may be updated", time60, step=60, key="002")
            td_time60upd = datetime.timedelta(seconds=((dt.combine(dt.min,time60upd)-dt.min).total_seconds())/60)
            # display in widget
            if "elapsedTime" not in st.session_state:
                ET=dt.now()-dt.now()
            else:
                ET=st.session_state.elapsedTime
            print("time60upd: ", time60upd, td_time60upd)
            #print("ETz now: ", st.session_state.elapsedTime)
            #st.rerun()
            col1, col2 = st.columns(2)

            with col1:
                if st.button("Start"):
                    #st.session_state.makeFinal=False
                    print("launch stopwatch. ET:", ET)
                    print("return. ET:", ET)
                    st.session_state.final_started=True
                    #st.rerun()
                if st.session_state.final_started==True:
                    ET=stopwatch()
            with col2:
                if st.button("Exit"):
                    st.session_state.final_loop=False
                    st.rerun()

