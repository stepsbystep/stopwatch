import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode, StreamlitFlowEdge

st.header("Streamlit Flow Sub Node Example Illustrating Text Alignment and Edge Issues")

# 'output', 'top', 'left',
nodes = [
        StreamlitFlowNode(id='10', pos=(90, 90), data={'content': "Node 1-0"},  node_type='input', source_position='left', draggable=False,
                          width=120, height=220),
        StreamlitFlowNode(id='11', pos=(100, 100), data={'content': "Node 1-1"},  node_type='input', source_position='right', draggable=False,
                          width=100, height=50),
        StreamlitFlowNode('12', (100, 150), {'content': 'Node 1-2'}, 'input', 'right', draggable=False,
                          width=100, height=50),
        StreamlitFlowNode('13', (100, 200), {'content': 'Node 1-3'}, 'input', 'right', draggable=False,
                          width=100, height=50, style={'width': '50px'}),
        StreamlitFlowNode('14', (100, 250), {'content': 'Node 1-4'}, 'output', target_position='right', draggable=False,
                          width=100, height=50),

    StreamlitFlowNode(id='20', pos=(290, 90), data={'content': "Node 2-0"},  node_type='input', source_position='left', draggable=False,
                          width=120, height=220),
        StreamlitFlowNode(id='21', pos=(300, 100), data={'content': "Node 2-1"},  node_type='input', source_position='left', draggable=False,
                          width=100, height=25),
        StreamlitFlowNode('22', (300, 150), {'content': 'Node 2-2'}, 'input', 'left', draggable=False,
                          width=100, height=25),
        StreamlitFlowNode('23', (300, 200), {'content': 'Node 2-3'}, 'input', 'left', draggable=False,
                          width=100, height=25, style = {'padding-top' : 0}),
        StreamlitFlowNode('24', (300, 250), {'content': 'Node 2-4'}, 'output', target_position='left', draggable=False,
                          width=100, height=25, style = {'padding-top' : -100})
                          ]

# , 'text-align' : 'top'
# 'margin-top' : 0, 
# , style = {"font-size" : 10, "fontWeight": 400}
# "margin-left": 10, "margin-top": 10, 
# , 'fontSize': '8px', , 'height': '-250px'
        
edges0=[]
edges = [
        StreamlitFlowEdge('14-21', '14', '21', animated=True),
        StreamlitFlowEdge('11-23', '11', '23', animated=True),
        StreamlitFlowEdge('12-21', '12', '21', animated=True),
        StreamlitFlowEdge('13-24', '13', '24', animated=True)
        ]

selected_id = streamlit_flow('ret_val_flow',
                nodes,
                edges,
                fit_view=True,
                get_node_on_click=True,
                get_edge_on_click=True)

st.write(f"Clicked on: {selected_id}")