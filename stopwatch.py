
def stopwatch():

    import streamlit as st
    import asyncio
    from datetime import datetime as dt
    import datetime

    print("start stopwatch")
    if "showWatch" not in st.session_state:
        st.session_state.showWatch=True
        st.session_state.pause=False
        st.session_state.restart=False
        st.session_state.updateTime=False
        st.session_state.stopwatchRunning=False
        st.session_state.elapsedTime = datetime.timedelta(microseconds=0)
        st.session_state.makeFinal=False
        st.session_state.runLoop=True
        st.session_state.EXIT=False
        print("init!")

    # css
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

    # async function
    async def watch(test):
        while st.session_state.runLoop:
            if st.session_state.updateTime:
                st.session_state.elapsedTime=dt.now()-st.session_state.startTime
                ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
                print("ET now:", ET)
            ET=st.session_state.elapsedTime-datetime.timedelta(microseconds=st.session_state.elapsedTime.microseconds)
            test.markdown(
                f"""
                <p class="time">
                    {str(ET)}
                </p>
                """, unsafe_allow_html=True)
            print("stopwatch running!")
            await asyncio.sleep(0.993)
        
        #if st.session_state.runLoop==False:

    #internal stopwatch function
    def theStopWatch():

        if st.session_state.showWatch:
            with st.popover("Press to show/hide stopwatch"): 
                test = st.empty()
                if st.session_state.stopwatchRunning==False:
                    print("showWatch initialization!")
                    st.session_state.stopwatchRunning=True
                    st.session_state.startTime=dt.now()
                    st.session_state.start=True
                    st.session_state.updateTime=False
                    #st.session_state.update=False
        
                if st.button("Start/Reset"):
                    st.session_state.startTime=dt.now()
                    st.session_state.updateTime=True
                    st.session_state.pause=False
                    print("start/reset")
                    asyncio.run(watch(test))
                    
                if st.button("Pause/Resume"):
                    # pause
                    if st.session_state.updateTime==True:
                        st.session_state.updateTime=False
                        st.session_state.pause=True
                        st.session_state.pauseTime=dt.now()
                        st.session_state.elapsedTime=dt.now()-st.session_state.startTime                
                        print("pause")
                    # resume
                    else:
                        st.session_state.pause=False
                        st.session_state.updateTime=True
                        st.session_state.startTime=dt.now()-st.session_state.elapsedTime
                        print("resume")    
                    asyncio.run(watch(test))

                if st.button("Stop"):
                    if st.session_state.pause==True:
                        st.session_state.startTime=dt.now()-st.session_state.elapsedTime
                        st.session_state.pause=False
                    st.session_state.start=False
                    st.session_state.updateTime=False
                    st.session_state.makeFinal=True
                    st.session_state.elapsedTime=dt.now()-st.session_state.startTime
                    st.session_state.showWatch=False
                    st.session_state.EXIT=True
                    print("stop")
                    st.rerun()
                 
        # exit when done!
        if st.session_state.EXIT==True:    
            print("internal function exit. time", st.session_state.elapsedTime)
            #st.rerun()
            return(st.session_state.elapsedTime)

    # call internal function
    theTime=theStopWatch()
    print("internal function return. time", theTime )
    # return main function
    return(theTime)


