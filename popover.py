import streamlit as st
import asyncio
from datetime import datetime as dt
import datetime

st.markdown(
    """
    <style>
    .time {
        font-size: 64px !important;
        font-weight: 200 !important;
        color: #ec5953 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# initializations
if "showWatch" not in st.session_state:
    st.session_state.showWatch=True
    st.session_state.pause=False
    st.session_state.restart=False
    st.session_state.updateTime=False
    st.session_state.stopwatchRunning=False
    st.session_state.elapsedTime = datetime.timedelta(microseconds=0)
    st.session_state.makeFinal=False
    st.session_state.runLoop=True
    print("init!")

async def watch(test):
    while st.session_state.runLoop:
        if st.session_state.updateTime:
            st.session_state.elapsedTime=dt.now()-st.session_state.startTime
            ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
            print("ET:", ET)
        ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
        test.markdown(
            f"""
            <p class="time">
                {str(ET)}
            </p>
            """, unsafe_allow_html=True)
        print("async running!")
        await asyncio.sleep(0.993)


#def runPopover(sync):
if st.session_state.showWatch:
    with st.popover("Press to show/hide stopwatch"): #popup:
        test = st.empty()
        if st.session_state.stopwatchRunning==False:
            print("set watch running!")
            st.session_state.stopwatchRunning=True
            st.session_state.startTime=dt.now()
            st.session_state.start=True
            st.session_state.updateTime=False
            #st.session_state.update=False

        if st.button("Start/Reset"):
            st.session_state.startTime=dt.now()
            st.session_state.updateTime=True
            print("start/reset")
            asyncio.run(watch(test))
        if st.button("Pause/Resume"):
            # pause
            if st.session_state.updateTime==True:
                st.session_state.updateTime=False
                st.session_state.pauseTime=dt.now()
                print("pause")
            # resume
            else:
                st.session_state.updateTime=True
                st.session_state.startTime=dt.now()-st.session_state.elapsedTime
                print("resume")    
            asyncio.run(watch(test))
        # not needed
        #if st.button("Reset"):
        #    st.session_state.startTime=dt.now()
        #    print("reset")
            asyncio.run(watch(test))
        if st.button("Stop"):
            st.session_state.start=False
            st.session_state.updateTime=False
            st.session_state.makeFinal=True
            st.session_state.elapsedTime=dt.now()-st.session_state.startTime
            ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
            #st.session_state.elapsedTime = ET - datetime.timedelta(microseconds=ET.microseconds)
            st.session_state.showWatch=False
            print("stop")
            st.rerun()

reportContainer = st.container(border=True)

if st.session_state.makeFinal:
    st.session_state.showWatch=True
    #st.session_state.makeFinal=False
    st.session_state.stopwatchRunning=False
    st.session_state.updateTime=True
    ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
    with reportContainer:
        st.markdown(
            f"""
            <p class="time">
                Elapsed time: {str(ET)}
            </p>
            """, unsafe_allow_html=True)
        time60=(dt.min+datetime.timedelta(seconds=60*ET.total_seconds())).time()
        time60upd = st.time_input("Entered time may be updated", time60, step=60)
    if st.button("Restart"):
        st.session_state.makeFinal=False
        st.rerun()
        
        

